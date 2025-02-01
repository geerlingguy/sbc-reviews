from pyinfra import local

local.include("tasks/setup.py")
local.include("tasks/basics.py")
local.include("tasks/tinymembench.py")
local.include("tasks/geekbench.py")
local.include("tasks/disk-benchmark.py")
local.include("tasks/top500.py")
local.include("tasks/ollama-benchmark.py")
local.include("tasks/sbc-general-benchmark.py")
