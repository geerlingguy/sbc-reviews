import subprocess
from pyinfra import host, logger
from pyinfra.facts.hardware import Memory
from pyinfra.facts.server import Home
from pyinfra.operations import files, git, python, server

host_ram_size=host.get_fact(Memory)
working_dir=host.get_fact(Home) + "/Downloads"
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

# Check if Ollama is already installed.
# TODO: This is checking on my local Mac. Need to check on the host!
rc = subprocess.call(['which', 'ollama'])
if rc == 1:
    server.shell(
        name="Run Ollama Install Script",
        commands="sh {}/install.sh".format(working_dir),
    )

git.repo(
    name="Clone ollama-benchmark with git.",
    src="https://github.com/geerlingguy/ollama-benchmark.git",
    dest="{}/ollama-benchmark".format(working_dir),
)

# Callback
def callback():
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
            commands="{}/ollama-benchmark/obench.sh -m {} -c 3 --markdown".format(working_dir, model),
        )

        logger.info(f"\n{ollama_benchmark_result.stdout}\n\n")

python.call(
    name="Execute Ollama loop",
    function=callback,
)
