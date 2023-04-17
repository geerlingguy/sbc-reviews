---
name: SBC Board
about: Standard data required for an SBC benchmark and review
title: SBC Name Here
labels: ''
assignees: ''

---

[comment]: # (If desired, delete this line and add an image of the board here)

## Basic information

  - Board URL (official): TODO
  - Board purchased from: TODO
  - Board purchase date: TODO
  - Board specs (as tested): TODO
  - Board price (as tested): TODO

## Linux/system information

```
# output of `neofetch`
PASTE_HERE

# output of `uname -a`
PASTE_HERE
```

## Benchmark results

### CPU

  - Geekbench: (TODO single / TODO multi - PASTE_URL)
  - TODO Gflops ([geerlingguy/top500-benchmark](https://github.com/geerlingguy/top500-benchmark) HPL result)

### Power

  - Idle power draw (at wall): TODO W
  - Maximum simulated power draw (`stress-ng --matrix 0`): TODO W
  - During Geekbench multicore benchmark: TODO W
  - During `top500` HPL benchmark: TODO W

### Disk

#### MANUFACTURER_AND_MODEL_OF_DISK_HERE

[comment]: # (Run `lsblk -o NAME,FSTYPE,LABEL,MOUNTPOINT,SIZE,MODEL` to get model)

| Benchmark | Result |
| --- | --- |
| fio 1M sequential read | TODO MB/s |
| iozone 1M random read | TODO MB/s |
| iozone 1M random write | TODO MB/s |
| iozone 4K random read | TODO MB/s |
| iozone 4K random write | TODO MB/s |

`curl https://raw.githubusercontent.com/geerlingguy/pi-cluster/master/benchmarks/disk-benchmark.sh | sudo bash`

Run benchmark on any attached storage device (e.g. eMMC, microSD, NVMe, SATA) and add results under an additional heading. Download the script with `curl -o disk-benchmark.sh [URL_HERE]` and run `sudo DEVICE_UNDER_TEST=/dev/sda DEVICE_MOUNT_PATH=/mnt/sda1 ./disk-benchmark.sh` (assuming the device is `sda`).

Also consider running [PiBenchmarks.com script](https://www.jeffgeerling.com/blog/2023/using-pibenchmarkscom-sbc-disk-performance-testing).

### Network

`iperf3` results:

  - `iperf3 -c $SERVER_IP`: TODO Mbps
  - `iperf3 --reverse -c $SERVER_IP`: TODO Mbps
  - `iperf3 --bidir -c $SERVER_IP`: TODO Mbps up, TODO Mbps down

(Be sure to test all interfaces, noting any that are non-functional.)

## GPU

  - TODO: Haven't determined standardized benchmark yet. See [Issue #2](https://github.com/geerlingguy/sbc-reviews/issues/2).

## Memory

  - TODO: Haven't determined standardized benchmark yet. See [Issue #2](https://github.com/geerlingguy/sbc-reviews/issues/2).
