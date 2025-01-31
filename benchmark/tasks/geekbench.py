import os
from pyinfra import logger
from pyinfra.operations import files, python, server

working_dir=os.path.expanduser("~") + "/Downloads"
# TODO: Use `host.get_fact(Arch)` to pick file?
#   - Arm: https://cdn.geekbench.com/Geekbench-6.4.0-LinuxARMPreview.tar.gz
#   - RISC-V: https://cdn.geekbench.com/Geekbench-6.4.0-LinuxRISCVPreview.tar.gz
#   - AMD64: https://cdn.geekbench.com/Geekbench-6.4.0-Linux.tar.gz
download_file="Geekbench-6.4.0-Linux.tar.gz"

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

def callback():
    logger.info(f"\n```\n{geekbench_result.stdout}\n```")

python.call(
    name="Print Geekbench result",
    function=callback,
)
