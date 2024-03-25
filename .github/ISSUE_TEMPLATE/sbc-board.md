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

  - Geekbench 6: (TODO single / TODO multi - PASTE_URL)
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

`glmark2-es2` results:

```
1. Install glmark2-es2 with `sudo apt install -y glmark2-es2`
2. Run `glmark2-es2`
3. Replace this block of text with the results.
```

Note: This benchmark requires an active display on the device. Not all devices may be able to run `glmark2-es2`, so in that case, make a note and move on!

TODO: See [this issue](https://github.com/geerlingguy/sbc-reviews/issues/2) for discussion about a full suite of standardized GPU benchmarks.

## Memory

`tinymembench` results:

<details>
<summary>Click to expand memory benchmark result</summary>

```
# Run the two commands below, then replace this code block with the full result.
git clone https://github.com/rojaster/tinymembench.git && cd tinymembench && make
./tinymembench
```
</details>

## `sbc-bench` results

Run sbc-bench and paste a link to the results here:

```
wget https://raw.githubusercontent.com/ThomasKaiser/sbc-bench/master/sbc-bench.sh
sudo /bin/bash ./sbc-bench.sh -r
```

## Phoronix Test Suite

Results from [pi-general-benchmark.sh](https://gist.github.com/geerlingguy/570e13f4f81a40a5395688667b1f79af):

  - pts/encode-mp3: TODO sec
  - pts/x264 4K: TODO fps
  - pts/x264 1080p: TODO fps
  - pts/phpbench: TODO
  - pts/build-linux-kernel (defconfig): TODO sec
