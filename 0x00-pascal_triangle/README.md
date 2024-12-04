# Pascal's Triangle

## Description
This project implements a Python function to generate Pascal's Triangle up to a given number of rows. Pascal's Triangle is a triangular array of the binomial coefficients. Each number in the triangle is the sum of the two numbers directly above it.

## Requirements
- Python 3.4.3 or later
- All files must be executable
- Code should follow PEP 8 (version 1.7)

## Usage
The function `pascal_triangle` generates Pascal's Triangle up to `n` rows.

### Function Prototype
```python
def pascal_triangle(n):
    """
    Generate Pascal's Triangle of size n.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list of list of ints: Pascal's Triangle up to n rows.
    """
