import sys
import time
from pyinfra import host, local, logger
from pyinfra.operations import python

# See: https://github.com/geerlingguy/sbc-reviews/issues/67
sys.setrecursionlimit(2000)

pause_seconds = 60
tasks = [
    'tinymembench.py',
    'geekbench.py',
    'disk-benchmark.py',
    'top500.py',
    'ollama-benchmark.py',
    'sbc-general-benchmark.py',
]

local.include("tasks/setup.py")
local.include("tasks/basics.py")


def task_callback():
    for task in tasks:
        logger.info("\n\nPausing {} seconds for cooldown...\n".format(pause_seconds))
        time.sleep(pause_seconds)
        local.include("tasks/{}".format(task))


python.call(
    name="Execute task loop",
    function=task_callback,
)
