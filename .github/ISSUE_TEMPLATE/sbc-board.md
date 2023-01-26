---
name: SBC Board
about: Standard data required for an SBC benchmark and review
title: SBC Name Here
labels: ''
assignees: ''

---

### Basic information

  - Board specs (as tested): TODO
  - Board URL (official): TODO
  - Board purchased from: TODO

### Linux/system information

```
# output of `uname -a`
PASTE_HERE

# output of `neofetch`
PASTE_HERE
```

### Benchmark results

#### CPU

  - Geekbench: (TODO single / TODO multi - PASTE_URL)
  - TODO Gflops ([geerlingguy/top500-benchmark](https://github.com/geerlingguy/top500-benchmark) HPL result)

### Disk

`curl https://raw.githubusercontent.com/geerlingguy/pi-cluster/master/benchmarks/disk-benchmark.sh | sudo bash` (or download script and run `sudo DEVICE_UNDER_TEST=/dev/sda1 DEVICE_MOUNT_PATH=/mnt/sda1 ./disk-benchmark.sh`

| Benchmark | Result |
| --- | --- |
| fio 1M sequential read | TODO MB/s |
| iozone 1M random read | TODO MB/s |
| iozone 1M random write | TODO MB/s |
| iozone 4K random read | TODO MB/s |
| iozone 4K random write | TODO MB/s |

Run this on any attached storage device (e.g. eMMC, microSD, NVMe, SATA). Also consider running [PiBenchmarks.com script](https://www.jeffgeerling.com/blog/2023/using-pibenchmarkscom-sbc-disk-performance-testing).

### Network

`iperf3` results:

  - `iperf3 -c [ip of server]`: TODO Mbps
  - `iperf3 --reverse -c [ip of server]`: TODO Mbps
  - `iperf3 --bidir -c [ip of server]`: TODO Mbps

(Be sure to test all interfaces, noting any that are non-functional.)

### GPU

  - TODO: Haven't determined standardized benchmark yet. See [Issue #2](https://github.com/geerlingguy/sbc-reviews/issues/2).

### Memory

  - TODO: Haven't determined standardized benchmark yet. See [Issue #2](https://github.com/geerlingguy/sbc-reviews/issues/2).
