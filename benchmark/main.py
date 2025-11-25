import sys
import time
from pyinfra import host, local, logger
from pyinfra.operations import python

# Minimum Python version: 3.10.
assert sys.version_info >= (3, 10)

pause_seconds = 60
tasks = [
    'tinymembench.py',
    'geekbench.py',
    'disk-benchmark.py',
    'top500.py',
    'sbc-general-benchmark.py',
    'ai-benchmark.py',
]

local.include("tasks/setup.py")
local.include("tasks/basics.py")


def task_callback():
    for i, task in enumerate(tasks):
        if i != 0:
            logger.info("\n\nPausing {} seconds for cooldown...\n".format(pause_seconds))
            time.sleep(pause_seconds)
        local.include("tasks/{}".format(task))


python.call(
    name="Execute task loop",
    function=task_callback,
)
