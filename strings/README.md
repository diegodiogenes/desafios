# String Formatter

## About the project

This project was implemented to ID Wall Challenge, with purpose to create a Formatter String that wrap and align string 
and save the result on file.

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

2. Build and Run the Docker container:

```bash
make run
python main.py --input input.txt --path inputs --align justify
```

Documentation:
```bash
input: Filename or string to format
path: path with the file to read string
align: the type of align text (justify)
```

3. Run the tests:

```bash
make test
```

4. Run the example of usage

```bash
make example
```