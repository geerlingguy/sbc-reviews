from pyinfra import host, logger
from pyinfra.operations import files, python, server
from pyinfra.facts.server import Arch, Home

working_dir=host.get_fact(Home) + "/Downloads"

# Pick the proper download based on host architecture.
host_arch = host.get_fact(Arch)
match host_arch:
    case 'x86_64':
        download_file="Geekbench-6.5.0-Linux.tar.gz"
    case 'aarch64':
        download_file="Geekbench-6.5.0-LinuxARMPreview.tar.gz"
    case 'riscv64':
        download_file="Geekbench-6.5.0-LinuxRISCVPreview.tar.gz"
    case _:
        python.raise_exception(
            name="Raise host not supported exception",
            exception=NotImplementedError,
            message="Host architecture {} is not supported yet.".format(host_arch),
        )

files.download(
    name="Download Geekbench",
    src="https://cdn.geekbench.com/{}".format(download_file),
    dest="{}/{}".format(working_dir, download_file),
)

server.shell(
    name="Extract Geekbench",
    commands="tar -xvzf {}/{} -C {}".format(working_dir, download_file, working_dir),
)

geekbench_result = server.shell(
    name="Run Geekbench",
    commands="{}/{}/geekbench6".format(working_dir, download_file.replace('.tar.gz', '')),
)

def geekbench_result_callback():
    logger.info(f"\n```\n{geekbench_result.stdout}\n```")

python.call(
    name="Print Geekbench result",
    function=geekbench_result_callback,
)
