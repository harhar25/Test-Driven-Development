# Test-Driven-Development

# 🧪 Test-Driven Development in Python: Factorial Function

This is a simple demonstration of **Test-Driven Development (TDD)** using Python's built-in `unittest` framework. The project includes:

- Writing tests **first** (RED)
- Creating the minimum code to pass the tests (GREEN)
- Refactoring and improving the code (REFACTOR)

## 📁 Project Structure


## 🧠 About the Project

This project implements a basic factorial function using recursion, developed using the TDD workflow. 

### Features

- Calculates factorial of a number
- Handles edge case: `0! = 1`
- Raises `ValueError` for negative inputs
- Uses `unittest` for testing

## 🔬 How TDD Was Applied

1. **RED**: Wrote failing tests first in `test_factorial.py`
2. **GREEN**: Created `factorial.py` to make the tests pass
3. **REFACTOR**: Improved readability and handling of edge cases

## ✅ How to Run the Tests

Make sure you're in the project directory, then run:


python test_factorial.py

def test_factorial_of_zero(self):
    self.assertEqual(factorial(0), 1)

def test_factorial_of_positive_number(self):
    self.assertEqual(factorial(5), 120)

def test_factorial_of_negative_number(self):
    with self.assertRaises(ValueError):
        factorial(-1)

## 🔧 Requirements

- Python 3.x  
- No external libraries required

## 👤 Author

[@harhar25](https://github.com/harhar25)

