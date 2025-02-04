from pyinfra import host, logger
from pyinfra.operations import files, python, server
from pyinfra.facts.server import Home

php_version="8.3"
working_dir=host.get_fact(Home) + "/Downloads"

disk_info = server.shell(
    name="Retrieve disk info",
    commands="lsblk -o NAME,FSTYPE,LABEL,MOUNTPOINT,SIZE,MODEL",
)

def disk_callback():
    logger.info(f"\n{disk_info.stdout}\n")

python.call(
    name="Print disk info",
    function=disk_callback,
)

files.download(
    name="Download disk-benchmark script",
    src="https://raw.githubusercontent.com/geerlingguy/pi-cluster/master/benchmarks/disk-benchmark.sh",
    dest="{}/disk-benchmark.sh".format(working_dir),
)

disk_benchmark_result = server.shell(
    name="Run disk-benchmark.sh",
    commands="sh {}/disk-benchmark.sh".format(working_dir),
    _env={
        'MOUNT_PATH': '/',
        'TEST_SIZE': '1g'
    },
    _sudo=True,
)

def disk_benchmark_callback():
    logger.info(f"\n{disk_benchmark_result.stdout}\n")

python.call(
    name="Print disk-benchmark.sh result",
    function=disk_benchmark_callback,
)
