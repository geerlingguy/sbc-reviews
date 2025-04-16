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
# output of `screenfetch`
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

| Benchmark                  | Result |
| -------------------------- | ------ |
| iozone 4K random read      | TODO MB/s |
| iozone 4K random write     | TODO MB/s |
| iozone 1M random read      | TODO MB/s |
| iozone 1M random write     | TODO MB/s |
| iozone 1M sequential read  | TODO MB/s |
| iozone 1M sequential write | TODO MB/s |

```
wget https://raw.githubusercontent.com/geerlingguy/pi-cluster/master/benchmarks/disk-benchmark.sh
chmod +x disk-benchmark.sh
sudo MOUNT_PATH=/ TEST_SIZE=1g ./disk-benchmark.sh
```

Run benchmark on any attached storage device (e.g. eMMC, microSD, NVMe, SATA) and add results under an additional heading.

Also consider running [PiBenchmarks.com script](https://www.jeffgeerling.com/blog/2023/using-pibenchmarkscom-sbc-disk-performance-testing).

### Network

`iperf3` results:

  - `iperf3 -c $SERVER_IP`: TODO Mbps
  - `iperf3 -c $SERVER_IP --reverse`: TODO Mbps
  - `iperf3 -c $SERVER_IP --bidir`: TODO Mbps up, TODO Mbps down

(Be sure to test all interfaces, noting any that are non-functional.)

## GPU

### glmark2

`glmark2-es2` / `glmark2-es2-wayland` results:

```
1. Install glmark2-es2 with `sudo apt install -y glmark2-es2`
2. Run `glmark2-es2` (with `DISPLAY=:0` prepended if running over SSH)
3. Replace this block of text with the results.
```

### vkmark

`vkmark` results:

```
1. Install vkmark with `sudo apt install -y vkmark`
2. Run `vkmark` (with `DISPLAY=:0` prepended if running over SSH)
3. Replace this block of text with the results.
```

> **Note**: `vkmark` needs to be [compiled from source](https://github.com/geerlingguy/sbc-reviews/issues/76) on Debian 12 and earlier.

### GravityMark

GravityMark results:

```
1. Download the latest version of GravityMark: https://gravitymark.tellusim.com
2. Run `chmod +x [downloaded_filename].run`
3. Run `sudo ./[downloaded_filename].run` and press `y` to accept the terms.
4. Open the link it prints, and run the Benchmark defaults, changing to 720p resolution and 50,000 asteroids.
```

Note: These benchmarks require an active display on the device. Not all devices may be able to run `glmark2-es2`, so in that case, make a note and move on!

### Ollama

`ollama` LLM model inference results:

```
# Install ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download some models
ollama pull llama3.2:3b && ollama pull llama3.1:8b

# Run benchmark
git clone https://github.com/geerlingguy/ollama-benchmark.git
cd ollama-benchmark
./obench.sh
```

Note that Ollama will run on the CPU if no valid GPU / drivers are present. Be sure to note whether Ollama runs on the CPU, GPU, or a dedicated NPU.

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
