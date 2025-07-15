## Python with Flask for Large-Scale Projects
Python with Flask is a lightweight and flexible web application framework. It's known for its simplicity, minimalism, and ease of use. It is designed as a micro-framework providing a lightweight structure which facilitates developers in building a web application quickly and easily but not compromising on the efficiency and ability to scale up from small-scale projects to larger, more complex applications.

Flask is a good choice for smaller, simpler applications. However, 'micro' has more to do with what Flask is, rather than limiting its scalability potential. Flask can be used for large-scale systems and more complex applications with attention to specific requirements and constraints, careful planning, good architecture, and modular design, but it may require more effort to manage and scale compared to more robust and feature-rich frameworks.

Its rich and robust ecosystem provides developers with tools, libraries, and functionalities to handle web development tasks such as routing, request handling, template rendering or similar tasks. Caching, load-balancing, replication and storing your data in a scalable manner can help achieve optimal results.

## Application Development lifecycle phases
1. Requirement gathering
2. Analysis
3. Design
4. Code and test
5. User and system testing
6. Production
7. Maintenance

## Maintain multiple file
- Requirements for functionalities vary
- Best Practice: Code each functionality in a seperate file
    - Make code maintainance efficient and easy
    - Helps when new functionality is added

## Using Spaces for Indentation
**PEP8 Guidelines**
- Use 4 spaces is recommended than Tab
    - for appropriate readability
- Use blank lines to seperate functions and classes
- Use spaces around operators and commas
    - improve code readability
    - make commands look spacious and discrete
- Use functions for blocks of codes
    - create seperate function for functionalities
    - increase the execution speed of the code
    - support reusability
- Naming functions and files
    - Functions: use lowercase with underscores (sample_function())
    - Package: avoid underscore (mypakage)
    - Classes - Camecase
        - well accepted in coding community
        - Distinguish between classes and functions
    - Constant - CAPITALIZE ALL WORDS

## Static code analysis
- evaluates style compliance without executing the code
    - programming errors
    - coding standard violations
    - undefined values
    - systax violations
    - security vulnabilities
- PyLint

# Unit Testing Summary

## What is Unit Testing?

Unit testing is a method to validate if units of code are operating as designed. A unit is a smaller, testable part of an application that can be tested independently.

## Testing Process Overview

The unit testing process follows these phases:

1. **Local Testing** - Test the unit on your local system
2. **Fix Issues** - If tests fail, determine the reason and fix the problem
3. **Server Testing** - Test the unit in a server environment (CI/CD test server)
4. **Integration** - Once the unit passes server tests, it's integrated into the final code base

## Creating Unit Tests

### File Structure
- **Unit file**: `mymodule.py` (contains the actual functions)
- **Test file**: `test_mymodule.py` (contains the unit tests)
- Use "test" as prefix or suffix in test file names for clear differentiation

### Basic Setup Steps

1. **Import the unittest library**
   ```python
   import unittest
   ```

2. **Import functions to test**
   ```python
   from mymodule import square, doubler
   ```

3. **Create a test class**
   ```python
   class TestMyModule(unittest.TestCase):
   ```
   - Use "Test" prefix for class names
   - Inherit from `unittest.TestCase`

4. **Create test functions**
   ```python
   def test_square(self):
   def test_doubler(self):
   ```
   - Function names must start with "test"

5. **Add assertion methods**
   ```python
   self.assertEqual(square(2), 4)
   ```

## Key Assertion Method

**assertEqual()** - Compares two values to determine if they are equal
- **First parameter**: Actual value (function call result)
- **Second parameter**: Expected value (what the function should return)

## Test Results

### Successful Test Output
- Shows number of tests run and execution time
- Displays "OK" to indicate all tests passed

### Failed Test Output
- Clearly identifies which test failed
- Shows the specific assertion that failed
- Provides detailed error information (e.g., "8 is not equal to 4")
- Enables developers to identify and correct mistakes before deployment

## Example

```python
# mymodule.py
def square(number):
    return number ** 2

def doubler(number):
    return number * 2

# test_mymodule.py
import unittest
from mymodule import square, doubler

class TestMyModule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
    
    def test_doubler(self):
        self.assertEqual(doubler(3), 6)
```

Unit testing ensures code quality and helps catch errors early in the development process before deployment to production.ity and helps catch errors early in the development process before deployment to production.
