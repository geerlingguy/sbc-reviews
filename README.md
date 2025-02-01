# SBC Reviews

Jeff Geerling's SBC (Single-Board Computer) review and benchmarking data repo.

There are many like it, but this one is mine.

## List of SBCs

All SBCs I have tested as part of this project are listed below. Click on the name of the SBC to view all the testing and benchmarking details.

| SBC Name | Year Introduced | CPU |
| --- | --- | --- |
| [Radxa Orion O6](https://github.com/geerlingguy/sbc-reviews/issues/62) | 2025 | Cix CD8180 |
| [HiFive Premier P550](https://github.com/geerlingguy/sbc-reviews/issues/65) | 2025 | ESWIN EIC7700X |
| [GMKtec NucBox G3 Plus](https://github.com/geerlingguy/sbc-reviews/issues/64) | 2025 | Intel N150 |
| [Raspberry Pi 500](https://github.com/geerlingguy/sbc-reviews/issues/60) | 2024 | Broadcom BCM2712 |
| [Raspberry Pi CM5](https://github.com/geerlingguy/sbc-reviews/issues/58) | 2024 | Broadcom BCM2712 |
| [Snapdragon Dev Kit](https://github.com/geerlingguy/sbc-reviews/issues/51) | 2024 | Snapdragon X Elite |
| [Orange Pi 5 Max](https://github.com/geerlingguy/sbc-reviews/issues/49) | 2024 | Rockchip RK3588 |
| [Radxa X4](https://github.com/geerlingguy/sbc-reviews/issues/48) | 2024 | Intel N100 |
| [Milk-V Jupiter](https://github.com/geerlingguy/sbc-reviews/issues/47) | 2024 | Spacemit X60 |
| [Milk-V Mars](https://github.com/geerlingguy/sbc-reviews/issues/46) | 2024 | StarFive JH7110 |
| [LattePanda Mu](https://github.com/geerlingguy/sbc-reviews/issues/42) | 2024 | Intel N100 |
| [Radxa Rock 5C](https://github.com/geerlingguy/sbc-reviews/issues/41) | 2024 | Rockchip RK3588S2 |
| [Radxa CM5](https://github.com/geerlingguy/sbc-reviews/issues/40) | 2024 | Rockchip RK3588S2 |
| [Lichee Console 4A](https://github.com/geerlingguy/sbc-reviews/issues/39) | 2024 | T-Head TH1520 |
| [Turing Pi RK1](https://github.com/geerlingguy/sbc-reviews/issues/38) | 2024 | Rockchip RK3588 |
| [Orange Pi Zero 2W](https://github.com/geerlingguy/sbc-reviews/issues/33) | 2023 | Allwinner H618 |
| [Luckfox Core3566](https://github.com/geerlingguy/sbc-reviews/issues/27) | 2023 | Rockchip RK3566 |
| [Orange Pi Compute Module 4](https://github.com/geerlingguy/sbc-reviews/issues/26) | 2023 | Rockchip RK3566 |
| [Milk-V Mars CM](https://github.com/geerlingguy/sbc-reviews/issues/22) | 2023 | StarFive JH7110 |
| [Raspberry Pi 5 model B](https://github.com/geerlingguy/sbc-reviews/issues/21) | 2023 | Broadcom BCM2712 |
| [Ampere Altra Developer Platform](https://github.com/geerlingguy/sbc-reviews/issues/19) | 2023 | Ampere Altra |
| [Radxa Rock 5 model B](https://github.com/geerlingguy/sbc-reviews/issues/3) | 2023 | Rockchip RK3588 |
| [Orange Pi 5](https://github.com/geerlingguy/sbc-reviews/issues/5) | 2023 | Rockchip RK3588S |
| [Banana Pi BPI-CM4](https://github.com/geerlingguy/sbc-reviews/issues/11) | 2022 | Amlogic A311D |
| [StarFive VisionFive 2](https://github.com/geerlingguy/sbc-reviews/issues/10) | 2022 | StarFive JH7110 |
| [BigTreeTech CB1](https://github.com/geerlingguy/sbc-reviews/issues/28) | 2022 | Allwinner H616 |
| [Radxa Rock 3 Compute Module](https://github.com/geerlingguy/sbc-reviews/issues/15) | 2021 | Rockchip RK3566 |
| [Pine64 SOQuartz](https://github.com/geerlingguy/sbc-reviews/issues/7) | 2021 | Rockchip RK3566 |
| [Raspberry Pi Compute Module 4](https://github.com/geerlingguy/sbc-reviews/issues/8) | 2020 | Broadcom BCM2711 |
| [Raspberry Pi 400](https://github.com/geerlingguy/sbc-reviews/issues/59) | 2020 | Broadcom BCM2711 |
| [Raspberry Pi 4 model B](https://github.com/geerlingguy/sbc-reviews/issues/4) | 2019 | Broadcom BCM2711 |
| [Raspberry Pi 3 model B+](https://github.com/geerlingguy/sbc-reviews/issues/16) | 2018 | Boardcom BCM2837B0 |
| [Libre Computer 'Le Potato'](https://github.com/geerlingguy/sbc-reviews/issues/17) | 2017 | Amlogic S905X |

This table should be ordered by the date the board was launched, in descending order. I might add a CSV file (so it's still easy to manage by hand) which could be compiled into this README at some point in the future (that would also allow putting benchmark numbers directly into the CSV...).

## Motivation

I test a _lot_ of SBCs from Raspberry Pi, Radxa, Orange Pi, Pine64, ODROID, ASUS, and more.

Until recently, I would compile all my data in a single project folder and/or [blog post](https://www.jeffgeerling.com/tags/sbc), and maybe feature a few specific benchmarks in a video on [my YouTube channel](https://www.youtube.com/c/JeffGeerling).

But I decided I'd rather have a public repository with all the test data and review notes for all the SBCs I use and test.

Unless under NDA, my plan is to compile all my data here, in real-time, as a point of reference for myself and for anyone else who runs into interesting results (e.g. the RK3588 on the Rock 5 model B benchmarking _slower_ than the RK3588S on the Orange Pi 5).

## Methodology

For every board I test or review, I will open an Issue with the name of the SBC, and begin compiling data in that issue.

If you would like to see a board added that is not already listed, **please start a new [Discussion](https://github.com/geerlingguy/sbc-reviews/discussions)**—do not open an Issue until I have confirmed I am going to acquire and test a certain board.

The primary benchmarks I run are:

  - CPU: [Geekbench 5](https://www.geekbench.com/download/)
  - CPU: [Top500 HPL](https://github.com/geerlingguy/top500-benchmark)
  - GPU: TODO
  - Memory: `tinymembench`
  - Disk: [`disk-benchmark.sh`](https://github.com/geerlingguy/pi-cluster/blob/master/benchmarks/disk-benchmark.sh)
  - Disk: [PiBenchmarks.com](https://pibenchmarks.com)
  - Network: `iperf3` (upstream, downstream, and bidirectional)

I often test a variety of other board-specific features, too, though it depends on the amount of time I'm willing to devote to a specific board, whether I'll deep-dive or just get basic numbers.

## Benchmark Scripts

The benchmark scripts are run using `pyinfra`. It can be installed with `pip3 install pyinfra`.

Inside the `benchmark` directory, modify `inventory.py` to point at the system under test, and run:

```
pyinfra inventory.py main.py -y
```

This assumes you've already configured an SSH connection to the system under test.

You can run individual benchmarks separately by calling the task files individually:

```
pyinfra inventory.py tasks/tinymembench.py -y
```

Make sure you've run at least `tasks/setup.py` prior to running any other tasks, if not running `main.py`.

> Note: There is a parallel set of benchmarking scripts in the `benchmark-ansible` folder. Right now I'm setting up both side by side to do essentially the same thing, but I wanted to give Pyinfra a try since I hadn't used it for any 'production' scenario before.

## SBC Awards

I'm considering crowning certain SBCs with awards every year, like "Fastest storage" or "least functionality." That seems like it could be a fun way to blow off steam when I'm having a terrible experience, or celebrate some truly groundbreaking new features...

## Author

This repository is maintained by [Jeff Geerling](https://www.jeffgeerling.com).
