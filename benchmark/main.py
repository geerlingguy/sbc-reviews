import sys
import time
from pyinfra import host, local, logger
from pyinfra.facts.files import File
from pyinfra.facts.server import Home
from pyinfra.operations import python, server

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

# Marker files for completed tasks are stored here on the system under test.
completed_dir = host.get_fact(Home) + "/Downloads/.benchmark-completed"
force_run = host.data.get('force_run', False)


def task_callback():
    ran_previous_task = False
    for task in tasks:
        task_name = task.removesuffix('.py')
        marker = "{}/{}".format(completed_dir, task_name)

        if not force_run and host.get_fact(File, path=marker):
            logger.info("\n\nSkipping {}: already completed successfully on a previous run ({}).\n".format(task_name, marker))
            continue

        if ran_previous_task:
            logger.info("\n\nPausing {} seconds for cooldown...\n".format(pause_seconds))
            time.sleep(pause_seconds)

        # Raises if any operation fails, so the marker below is only written on success.
        local.include("tasks/{}".format(task))
        ran_previous_task = True

        server.shell(
            name="Mark {} as completed".format(task_name),
            commands=[
                "mkdir -p {}".format(completed_dir),
                "date -u +%Y-%m-%dT%H:%M:%SZ > {}".format(marker),
            ],
        )


python.call(
    name="Execute task loop",
    function=task_callback,
)
