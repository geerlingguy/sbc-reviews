import os
from pyinfra import host, logger
from pyinfra.facts.files import File
from pyinfra.facts.hardware import Memory
from pyinfra.facts.server import Arch, Command, Home, LinuxName
from pyinfra.operations import apt, dnf, files, git, python, server
from urllib.parse import urlparse

host_ram_size=host.get_fact(Memory)
working_dir=host.get_fact(Home) + "/Downloads"

if host.data.ai_benchmark == 'llama.cpp':
    linux_name=host.get_fact(LinuxName)

    if linux_name in ["Debian", "Ubuntu"]:
        apt.packages(
            name="Ensure prerequisites are installed (Debian).",
            packages=[
                "libvulkan-dev",
                "glslc",
                "cmake",
                "libcurl4-openssl-dev",
            ],
            _sudo=True,
        )

    if linux_name in ["CentOS", "RedHat", "Fedora"]:
        dnf.packages(
            name="Ensure prerequisites are installed (RedHat).",
            packages=[
                "vulkan-loader-devel",
                "vulkan-validation-layers-devel",
                "vulkan-tools",
                "glslc",
                "cmake",
                "libcurl-devel",
            ],
            _sudo=True,
        )

    git.repo(
        name="Clone llama.cpp with git.",
        src="https://github.com/ggerganov/llama.cpp.git",
        dest="{}/llama.cpp".format(working_dir),
    )

    llama_cpp_build_opts=host.data.llama_cpp_build_opts
    num_cores = host.get_fact(Command, command="nproc --all")
    server.shell(
        name="Build llama.cpp",
        commands=[
            "cd {}/llama.cpp && cmake -B build {}".format(working_dir, llama_cpp_build_opts),
            "cd {}/llama.cpp && cmake --build build --config Release -j {}".format(working_dir, num_cores)
        ]
    )

    llama_bench_opts=host.data.llama_bench_opts
    def llama_cpp_loop_callback():
        for model, model_details in host.data.llama_cpp_models.items():
            # Accounting for multiple URL models.
            counter = 0
            total = len(model_details['urls'])

            for url in model_details['urls']:
                counter = counter + 1
                filename = os.path.basename(urlparse(url).path)
                files.download(
                    name="Downloading model: {} (file {} of {})".format(model, counter, total),
                    src=url,
                    dest="{}/llama.cpp/models/{}".format(working_dir, filename),
                )

            llama_bench_result = server.shell(
                name="Run llama-bench",
                commands="cd {}/llama.cpp && ./build/bin/llama-bench -m models/{} {}".format(working_dir, model, llama_bench_opts),
            )

            logger.info(f"\n{llama_bench_result.stdout}\n")

    python.call(
        name="Execute llama.cpp loop",
        function=llama_cpp_loop_callback,
    )

# TODO: Currently breaks, see https://github.com/pyinfra-dev/pyinfra/issues/1355
elif host.data.ai_benchmark == 'ollama':
    ollama_models={
        'llama3.2:3b': 2000,
        'llama3.1:8b': 4900,
        'llama2:13b': 7400,
        'deepseek-r1:1.5b': 1100,
        'deepseek-r1:8b': 4900,
        'deepseek-r1:14b': 9000,
        'deepseek-r1:70b': 43000,
    }

    files.download(
        name="Download Ollama Install Script",
        src="https://ollama.com/install.sh",
        dest="{}/install.sh".format(working_dir),
    )

    # Install Ollama if necessary (but not on RISC-V, for now). For RISC-V, see:
    # https://github.com/geerlingguy/sbc-reviews/issues/65#issuecomment-2637866212
    host_arch = host.get_fact(Arch)
    if not host_arch == 'riscv64':
        if not host.get_fact(File, path='/usr/local/bin/ollama'):
            server.shell(
                name="Run Ollama Install Script",
                commands="sh {}/install.sh".format(working_dir),
            )

    git.repo(
        name="Clone ai-benchmarks with git.",
        src="https://github.com/geerlingguy/ai-benchmarks.git",
        dest="{}/ai-benchmarks".format(working_dir),
    )

    def ollama_loop_callback():
        for model, model_size in ollama_models.items():
            # Skip a model if it's larger than the system RAM.
            if (host_ram_size - (host_ram_size / 8)) < model_size:
                logger.info(f"\nSkipping model {model} as it is too large.\n\n")
                continue

            server.shell(
                name="Download Ollama model: {}".format(model),
                commands="ollama pull {}".format(model),
            )

            ollama_benchmark_result = server.shell(
                name="Benchmark Ollama model: {}".format(model),
                commands="{}/ai-benchmarks/obench.sh -m {} -c 3 --markdown".format(working_dir, model),
            )

            logger.info(f"\n{ollama_benchmark_result.stdout}\n\n")

    python.call(
        name="Execute Ollama loop",
        function=ollama_loop_callback,
    )

else:
    logger.info(f"Please specify a valid ai-benchmark option.")
