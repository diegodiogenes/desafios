# Reddit Crawler

## About the project

This project was implemented to ID Wall Challenge, with purpose to create a
crawler for extract informations about subredits on old.reddit.com.

## Technology
This project was developed with the following technologies:
- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)

## Getting Started

### Prerequisites

Just have a docker on machine or Python.

### Install and Run

1. Clone this repository:
```bash
git@github.com:diegodiogenes/desafios.git
```

2. Move to crawlers folder:
```bash
cd crawlers
```

3Build and Run the Docker container:

```bash
make run
python main.py --subs "tumblr;brazil"
```

Documentation:
```bash
subs: The list of subs you want the informations such as: tumblr;brazil
```
