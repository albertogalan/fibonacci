# Fibonacci Sequence Generator

## Description
This project provides a Python script to compute the n-th Fibonacci number or the sequence up to n.

## Installation
No installation is required. Just ensure you have Python 3.x installed.

## Usage
Run the script from the command line with the following syntax:
```bash
python fibonacci.py <n> [--sequence]
```

### Examples
1. Compute the 10th Fibonacci number:
```bash
python fibonacci.py 10
```
2. Compute the Fibonacci sequence up to the 10th number:
```bash
python fibonacci.py 10 --sequence
```

## Optional Flags
- `--sequence`: If provided, returns the sequence up to the specified index.

## Error Handling
The script validates input and raises an error if the input is negative.
