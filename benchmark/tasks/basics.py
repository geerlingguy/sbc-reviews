from pyinfra import logger
from pyinfra.operations import python, server

uname_info = server.shell(
    commands=["uname -a"],
)

# TODO: Update to fastfetch, which is a little tricky on Debian < 13 and Ubuntu.
screenfetch_info = server.shell(
    commands=["screenfetch"],
)

def basic_callback():
    logger.info(f"\n```\n# output of `screenfetch`\n{screenfetch_info.stdout}\n\n# output of `uname -a`\n{uname_info.stdout}\n```")

python.call(
    name="Print basic info",
    function=basic_callback,
)
