# Python PyTest Demo

![Tests](https://github.com/optimisticwaqar/python-pytest-demo/workflows/Run%20Tests/badge.svg)

A demonstration of Python testing with PyTest and GitHub Actions.

## Features

- Math utilities with comprehensive tests
- String utilities with error handling
- Automated testing with GitHub Actions
- Test coverage reporting

## Running Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run with coverage
pytest --cov=math_utils --cov=string_utils