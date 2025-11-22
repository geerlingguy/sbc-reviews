# SBC Reviews

Jeff Geerling's SBC (Single-Board Computer) review and benchmarking data repo.

## Website

For a list of all the reviews, and all my test data, visit the site at [https://sbc-reviews.jeffgeerling.com/](https://sbc-reviews.jeffgeerling.com/).

## Motivation

I test a _lot_ of SBCs from Raspberry Pi, Radxa, Orange Pi, Pine64, ODROID, ASUS, and more.

Until recently, I would compile all my data in a single project folder and/or [blog post](https://www.jeffgeerling.com/tags/sbc), and maybe feature a few specific benchmarks in a video on [my YouTube channel](https://www.youtube.com/c/JeffGeerling).

But I decided I'd rather have a public repository with all the test data and review notes for all the SBCs I use and test.

Unless under NDA, my plan is to compile all my data here, in real-time, as a point of reference for myself and for anyone else who runs into interesting results (e.g. the RK3588 on the Rock 5 model B benchmarking _slower_ than the RK3588S on the Orange Pi 5).

## Methodology

For every board I test or review, I will open an Issue with the name of the SBC, and begin compiling data in that issue.

If you would like to see a board added that is not already listed, **please start a new [Discussion](https://github.com/geerlingguy/sbc-reviews/discussions)**—do not open an Issue until I have confirmed I am going to acquire and test a certain board.

A list of _all_ the tests I attempt to run on a board is contained in the [sbc-board.md Issue Template](/.github/ISSUE_TEMPLATE/sbc-board.md).

I often test a variety of other board-specific features, too, though it depends on the amount of time I'm willing to devote to a specific board, whether I'll deep-dive or just get basic numbers.

## Benchmark Scripts

The benchmark scripts are run using `pyinfra`. It can be installed with `pip3 install pyinfra`.

Inside the `benchmark` directory, modify `inventory.py` to point at the system under test, modify `group_data/all.py` with the variables appropriate for your system, and run:

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

## Building the Website

The website is generated with Hugo. Check out [Hugo's installation guide](https://gohugo.io/installation/).

Change directories into `web` and run `hugo server` to run to run a local development environment and preview the site.

The website is built using GitHub Actions, with the configuration stored inside `.github/workflows/hugo.yml`.

## Author

This repository is maintained by [Jeff Geerling](https://www.jeffgeerling.com).
