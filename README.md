# SBC Reviews

Jeff Geerling's little repository of SBC (Single-Board Computer) review and benchmarking data.

There are many like it, but this one is mine.

## Motivation

I test a _lot_ of SBCs from Raspberry Pi, Radxa, Orange Pi, Pine64, ODROID, ASUS, and more.

Until recently, I would compile all my data in a single project folder and/or [blog post](https://www.jeffgeerling.com/tags/sbc), and maybe feature a few specific benchmarks in a video on [my YouTube channel](https://www.youtube.com/c/JeffGeerling).

But I decided I'd rather have a public repository with all the test data and review notes for all the SBCs I use and test.

Unless under NDA, my plan is to compile all my data here, in real-time, as a point of reference for myself and for anyone else who runs into interesting results (e.g. the RK3588 on the Rock 5 model B benchmarking _slower_ than the RK3588S on the Orange Pi 5).

## Methodology

For every board I test or review, I will open an Issue on this project, and begin compiling data into it.

The primary benchmarks I run are:

  - CPU: [Geekbench 5](https://www.geekbench.com/download/)
  - CPU: [Top500 HPL](https://github.com/geerlingguy/top500-benchmark)
  - CPU: TODO
  - GPU: TODO
  - Memory: TODO
  - Disk: [`disk-benchmark.sh`](https://github.com/geerlingguy/pi-cluster/blob/master/benchmarks/disk-benchmark.sh)
  - Disk: [PiBenchmarks.com](https://pibenchmarks.com)
  - Network: `iperf3` (upstream, downstream, and bidirectional)

I often test a variety of other board-specific features, too, though it depends on the amount of time I'm willing to devote to a specific board, whether I'll deep-dive or just get basic numbers.

## List of SBCs

Currently there are no SBCs listed in this repository. But that will change as I start adding 

## Author

This repository is maintained by [Jeff Geerling](https://www.jeffgeerling.com).
