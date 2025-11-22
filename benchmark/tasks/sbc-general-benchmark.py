from pyinfra import host, logger
from pyinfra.operations import files, python, server
from pyinfra.facts.server import Home

php_version=host.data.php_version # TODO Map 8.x for different deb versions.
working_dir=host.get_fact(Home) + "/Downloads"

files.download(
    name="Download sbc-general-benchmark script",
    src="https://gist.githubusercontent.com/geerlingguy/570e13f4f81a40a5395688667b1f79af/raw/sbc-general-benchmark.sh",
    dest="{}/sbc-general-benchmark.sh".format(working_dir),
)

general_benchmark_result = server.shell(
    name="Run sbc-general-benchmark.sh",
    commands="bash {}/sbc-general-benchmark.sh".format(working_dir),
    _env={'PHP_VERSION': php_version},
    _sudo=True,
)

def sbc_general_result_callback():
    logger.info(f"\n\n{general_benchmark_result.stdout}\n")

python.call(
    name="Print sbc-general-benchmark.sh result",
    function=sbc_general_result_callback,
)
