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

# Python Modules, Packages, and Libraries Summary

## Definitions

### Python Module
A Python module is a `.py` file containing Python definitions, statements, functions, and classes. You can import a module to other scripts and notebooks.

**Example**: `module.py` with two functions:
```python
def square(number):
    return number ** 2

def doubler(number):
    return number * 2
```

**Usage**:
```python
import module
print(f"4^2 = {module.square(4)}")  # Output: 4^2 = 16
print(f"2*4 = {module.doubler(4)}")  # Output: 2*4 = 8
```

### Package
A package is a collection of Python modules into a directory with an `__init__.py` file, which distinguishes it from just a directory of Python scripts.

**Structure**:
```
my_project/
├── __init__.py
├── module1.py
└── module2.py
```

### Library
A library is a collection of packages or it can be a single package. Examples include NumPy, PyTorch, and Pandas.

**Note**: The terms "package" and "library" are often used interchangeably.

## Creating a Python Package

### Step-by-Step Process

1. **Create a folder** with the package name
2. **Create an empty `__init__.py` file**
3. **Create the required modules**
4. **In the `__init__.py` file**, add code to reference the modules needed in the package

### Example Package Structure

**Modules**:
- `module1.py` - contains `square()` and `doubler()` functions
- `module2.py` - contains `mean()` function

**`__init__.py` contents**:
```python
from . import module1
from . import module2
```

### Package Directory Structure
```
my_project/
├── __init__.py
├── module1.py
└── module2.py
```

## Verifying the Package

### Verification Steps

1. **Open a bash terminal**
2. **Navigate to the directory** where your package is located
3. **Open Python interpreter** by running `python` in the shell
4. **Import the package**: `import my_project`
5. **If no errors occur**, the package is successfully loaded

### Testing Package Functions

**General structure**:
```
package_name.module_name.function_name(parameters)
```

**Example**:
```python
my_project.module1.square(2)  # Returns 4
```

## Using the Package in Other Scripts

If the package folder is in the same directory as your script, you can import and use the functions:

**Example usage in `test.py`**:
```python
from my_project.module1 import square, doubler
from my_project.module2 import mean

print(f"4^2 = {square(4)}")           # 4^2 = 16
print(f"2*4 = {doubler(4)}")          # 2*4 = 8
print(f"(2+1+3)/3 = {mean([2,1,3])}")  # (2+1+3)/3 = 2
```

## Key Points

- **Module**: Single `.py` file with Python code
- **Package**: Directory of modules with `__init__.py` file
- **Library**: Collection of packages (or single package)
- **Import behavior**: When you import a module or package, Python creates an object of type "module"
- **File system distinction**: The difference between module and package exists only at the file system level
- **Interchangeable terms**: "Package" and "library" are often used interchangeably in practice

## Important Notes

- The `__init__.py` file is required to make a directory a package
- The package folder must be in the same directory as your script to import it directly
- Popular libraries like NumPy, PyTorch, and Pandas are also referred to as packages

# Python Libraries and Frameworks Summary

## Python Libraries

### What are Python Libraries?
Python libraries are like toolkits. Each library has specific tools to simplify and expedite certain programming tasks. These libraries save developers significant time and effort by providing pre-built functions instead of creating them from scratch.

### Popular Python Libraries

#### Mathematical and Data Analysis Libraries
- **NumPy**: Facilitates advanced mathematical calculations
- **Pandas**: Offers data manipulation and analysis capabilities
- **Matplotlib**: Simplifies data visualization

#### Web Development Libraries
- **Requests**: Simplifies the process of sending HTTP requests
- **BeautifulSoup**: Makes it easy to scrape information from web pages for iterating, searching, and modifying the parse tree
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) tool that gives application developers the full power and flexibility of SQL

#### Testing Libraries
- **PyTest**: A testing framework that allows users to create small, simple tests easily yet scales to support complex functional testing for applications and libraries

## Python Frameworks

### What are Frameworks?
Frameworks are predefined structures for application development. They provide a set of guidelines for application development and facilitate good coding practices by offering a well-defined structure for writing and organizing code.

### Popular Python Frameworks
- **Django**
- **Flask** 
- **Web2Py**

### Benefits of Using Frameworks

#### 1. Eases Development Process
- Provides pre-written code libraries and modules
- Includes developer guidelines
- Reduces development time

#### 2. Simplifies Debugging
- Comes with pre-built debugging tools
- Makes the debugging process easier for web applications

#### 3. More Functionality with Less Code
- Equipped with several pre-built libraries and modules
- Developers can leverage existing functionality
- No need to create all required functionalities from scratch

#### 4. Improves Database Management Efficiency
- Built-in database integration tools
- Enables seamless integration of database endpoints
- Facilitates efficient data transfer

#### 5. Enhanced Security
- Built-in security features and guidelines
- Helps developers enforce security measures
- Addresses key security concerns for application users

## Libraries vs Frameworks

### Key Differences

| Libraries | Frameworks |
|-----------|------------|
| Set of packages that perform specific functionality | Contains the basic flow and architecture of an application |
| Aid with specific tasks | Enable building complete applications |
| Like specialized toolkits | Predefined structures for development |
| Provide specific tools | Provide comprehensive development environment |

### Summary Points

- **Libraries**: Perform specific functionality and act as specialized toolkits
- **Frameworks**: Provide complete application structure and architecture
- **Purpose**: Libraries aid with specific functionality, while frameworks enable building complete applications
- **Code Reuse**: Frameworks enable reuse of code libraries for added features
- **Structure**: Frameworks provide well-defined structure for writing and organizing code

## Key Takeaways

1. Python libraries are essential tools that save development time by providing pre-built functionality
2. Frameworks offer comprehensive structures for application development with built-in guidelines
3. Using frameworks provides multiple benefits including easier development, debugging, database management, and security
4. Libraries focus on specific tasks while frameworks provide complete application development environments
5. Both libraries and frameworks promote code reuse and good coding practices

# Flask Framework Summary

## What is Flask?

Flask is a micro framework that can create web applications. It is not opinionated like some other larger frameworks and does not bind the user to a specific set of tools.

### Key Information
- **Current Version**: Flask 2.2.2
- **Python Requirement**: Minimum Python version 3.7
- **Creator**: Armin Ronacher (created in 2004 as an April Fool's joke)
- **Philosophy**: Provides minimal dependencies with extensibility through community extensions

## Main Features of Flask

### 1. Development Web Server
- Runs applications in development mode
- Built-in server for testing and development

### 2. Debugger
- Interactive traceback and stack trace in the browser
- Helps debug applications effectively

### 3. Logging
- Uses standard Python logging for application logs
- Allows custom message logging about your application

### 4. Testing Support
- Provides a way to test different parts of your application
- Enables test-driven development approach
- Compatible with frameworks like PyTest and coverage

### 5. Request/Response Objects
- Developers can access request and response objects
- Pull arguments and customize responses

## Additional Features

### Static Assets Support
- Supports CSS files, JavaScript files, and images
- Provides tags to load static files in templates

### Dynamic Pages
- Uses Jinja templating framework
- Can display information that changes for each request
- Can check user authentication status

### Routing
- Supports dynamic URLs
- Extremely useful for RESTful services
- Creates routes for different HTTP methods
- Provides redirection capabilities

### Error Handling
- Global error handlers at application level
- Comprehensive error management

### Session Management
- Built-in user session management support

## Popular Community Extensions

### Database Extensions
- **Flask-SQLAlchemy**: Adds ORM support for working with database objects in Python
- **Flask-Migrate**: Adds database migrations to SQLAlchemy ORM

### Communication Extensions
- **Flask-Mail**: Provides SMTP mail server setup capability
- **Flask-CORS**: Handles Cross-Origin Resource Sharing for cross-origin JavaScript requests

### User Management Extensions
- **Flask-User**: Adds user authentication, authorization, and user management activities
- **Flask-Admin**: Easily adds admin interfaces to Flask applications

### File and Data Handling
- **Flask-Uploads**: Adds customized file uploading capabilities
- **Marshmallow**: Provides extensive object serialization and deserialization support

### Task Management
- **Celery**: Powerful task queue for simple background tasks and complex multi-storage programs and schedules

## Installation and Dependencies

### Installation
- Available on Python package manager (pip)
- Recommended to create virtual environment using `venv` or `bin venv` module
- Install with: `pip install Flask==2.2.2`

### Version Pinning
- Recommended to pin version numbers of dependencies
- Ensures reproducibility across different environments (development, staging, production)
- Prevents new issues and bugs from automatic package updates

### Built-in Dependencies

Flask comes with several built-in dependencies:

- **Werkzeug**: Implements WSGI (Web Server Gateway Interface) - the standard Python interface between applications and servers
- **Jinja**: Template language that renders pages in your application
- **MarkupSafe**: Comes with Jinja; escapes untrusted input when rendering templates to avoid injection attacks
- **ItsDangerous**: Used to assign data securely; helps determine if data has been tampered with and protects Flask session cookies
- **Click**: Framework for writing command-line applications; provides the Flask command and allows adding custom management commands

### Viewing Dependencies
Use `pip freeze` command in the virtual environment to see all built-in packages installed by default.

## Flask vs Django Comparison

| Feature | Flask | Django |
|---------|--------|--------|
| **Framework Type** | Micro framework (lightweight) | Full-stack framework |
| **Dependencies** | Minimal basic dependencies | Includes everything needed for full-stack application |
| **Flexibility** | Very flexible, plug-and-play approach | Opinionated, makes most decisions for developer |
| **Extensibility** | Developer chooses extensions for additional features | Built-in comprehensive feature set |
| **Philosophy** | Provides foundation, developer builds up | Provides complete solution, developer focuses on logic |

## Key Takeaways

1. **Flask is a micro framework** that ships with minimal dependencies
2. **Core features** include debugging servers, routing, templates, and error handling
3. **Extensibility** through community extensions is a major strength
4. **Easy installation** as a Python package with pip
5. **Flexible approach** allows developers to choose their tools and extensions
6. **Production-ready** with proper version pinning and virtual environment setup
7. **Comparison with Django** shows Flask as lightweight and flexible vs Django's full-stack approach

# Creating Your First Flask Application

## Prerequisites

Before creating your first Flask application, ensure that you have installed Flask.

## Basic Flask Application Setup

### Step 1: Create the Server File

Create a Python file that will be your server. Let's name this file `app.py`.

### Step 2: Write the Basic Code

```python
# Import the Flask class from the flask module
from flask import Flask

# Instantiate an object of the Flask class as your app
app = Flask(__name__)

# Add the first route
@app.route("/")
def hello_world():
    return "<b>My first Flask application in action!</b>"
```

### Code Explanation

1. **Import Flask**: Import the capital F Flask class from the small f Flask module
2. **Instantiate Flask**: Create an object of the Flask class as your app
3. **Constructor**: Takes a single argument of class Scaffold. The `__name__` variable is used to:
   - Find resources on the filesystem
   - Provide debugging information by extensions
4. **Route Definition**: Use the `@app.route()` decorator to define a route
5. **Return Content**: Return text or HTML from the method

## Running Your Application

### Method 1: Using Environment Variables

#### Step 1: Set Environment Variables
```bash
export FLASK_APP=app.py
export FLASK_ENV=development  # Will be deprecated in Flask 2.3
```

#### Step 2: Run the Application
```bash
flask run
```

### Method 2: Using Command Line Arguments
```bash
flask --app app.py --debug run
```

**Benefits of `--debug` flag:**
- Enables development mode
- Enables automatic restarts when source files change
- Useful for seeing changes instantaneously during development

### Default Configuration
- Flask application runs by default on **port 5000**
- Access your application at: `http://localhost:5000`

## Testing Your Application

### Browser Testing
Navigate to `http://localhost:5000` to see your message.

### Developer Tools Analysis
When checking with browser developer tools, you should see:
- **Requested URL**: `http://localhost:5000`
- **Request Method**: HTTP GET
- **Response Status**: 200 (successful response)
- **Content Type**: `text/html`
- **Server**: Werkzeug running with Python version

## Returning JSON from Flask

### Method 1: Return Serializable Objects

```python
@app.route("/")
def hello_world():
    return {"message": "Hello, World!", "status": "success"}
```

**Testing with curl:**
```bash
curl http://localhost:5000
```

**Response:**
- Status: 200 OK
- Content Type: `application/json`
- Body: JSON format

### Method 2: Using jsonify() Method

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify(message="Hello, World!", status="success")
```

**Key Points:**
- Import `jsonify` from Flask
- Pass key-value pairs to `jsonify`
- Returns appropriate JSON response
- Same result as Method 1

## Flask Configuration Options

### Core Configuration Variables

| Variable | Description |
|----------|-------------|
| `ENV` | Indicates environment (production or development) |
| `DEBUG` | Enables debug mode |
| `TESTING` | Enables testing mode |
| `SECRET_KEY` | Used to sign the session cookie |
| `SESSION_COOKIE_NAME` | Name of the session cookie |
| `SERVER_NAME` | Binds the host and port |
| `JSONIFY` | Defaults to 'application/json' |

### Configuration Methods

#### 1. Using Config Object
```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your-secret-key'
```

#### 2. Loading from Environment Variables
```python
app.config.from_envvar('FLASK_SETTINGS')
```

#### 3. Loading from JSON File
```python
app.config.from_file('config.json', load=json.load)
```

## Application Directory Structure

As your app grows, create a proper directory structure instead of using a single Python file.

### Recommended Structure

```
my_flask_app/
├── app/                    # Main source code module directory
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── config/                 # Configuration files
│   ├── config.py
│   └── config.json
├── static/                 # Static assets
│   ├── css/
│   ├── js/
│   └── images/
├── templates/              # Dynamic content templates
│   ├── base.html
│   └── index.html
├── tests/                  # Test files
│   ├── test_app.py
│   └── test_routes.py
├── venv/                   # Virtual environment
├── app.py                  # Main application file
└── requirements.txt        # Dependencies
```

### Directory Purpose

- **app/**: Store main source code in its module directory
- **config/**: Store all configurations in separate files
- **static/**: Store static assets (images, JavaScript, CSS files)
- **templates/**: Store dynamic content templates
- **tests/**: Place all test files
- **venv/**: Virtual environment for proper dependency management

## Key Takeaways

1. **Server Creation**: Create a server by instantiating the Flask class
2. **URL Handlers**: Use the `@app.route()` decorator to create URL handlers
3. **Response Types**: Return string messages or use `jsonify()` method for JSON objects
4. **Configuration**: Set application configuration from:
   - Environment variables
   - Python files
   - `app.config` object directly
5. **Project Structure**: Use proper directory structure for larger applications
6. **Development Tools**: Use `--debug` flag for development convenience
7. **Testing**: Test applications using browsers, curl, or other HTTP clients

# 📘 Flask Request and Response Objects

### 🚏 Defining Routes and Methods
- Use `@app.route('/path')` to define routes (defaults to **GET**).
- Use the `methods` parameter to allow other HTTP methods.

```python
@app.route("/health", methods=["GET", "POST"])
```

* Example:

  * GET request → returns status OK, method GET
  * POST request → returns status OK, method POST

---

### 📨 The Flask Request Object

Each HTTP request in Flask includes a `request` object from `flask.Request`.

#### 🔍 Request Attributes

* `request.host`: server address (host\:port)
* `request.headers`: all headers
* `request.url`: full request URL
* `request.access_route`: list of forwarded IPs
* `request.full_path`: full path with query string
* `request.is_secure`: `True` if HTTPS/WSS
* `request.is_json`: `True` if body contains JSON
* `request.cookies`: dict of cookies

#### 📦 Header Attributes

* `request.cache_control`: caching details
* `request.accept`: acceptable content types
* `request.accept_encoding`: encoding types
* `request.user_agent`: client info (app/OS/version)
* `request.accept_language`: language/locale
* `request.host`: requested host and port

---

### 🧪 Inspecting Request Data

| Property             | Description                           |
| -------------------- | ------------------------------------- |
| `request.get_data()` | Raw POST data (bytes)                 |
| `request.get_json()` | Parsed JSON data                      |
| `request.args`       | Query parameters (ImmutableMultiDict) |
| `request.form`       | Form data (ImmutableMultiDict)        |
| `request.files`      | Uploaded files                        |
| `request.values`     | Combines `args` and `form`            |

#### Example: Extracting Query Parameters

```python
from flask import Flask, request

@app.route("/course")
def get_course():
    course = request.args["course"]         # KeyError if missing
    rating = request.args.get("rating")     # Returns None if missing
```

---

### 📤 The Flask Response Object

Returned by Flask view functions to send data back to clients.

#### 🔧 Common Response Attributes

* `status_code`: success/failure code (e.g., 200, 404)
* `headers`: extra response metadata
* `content_type`: type of content (e.g., `text/html`)
* `content_length`: size of response body
* `content_encoding`: how content is encoded
* `mimetype`: media type (e.g., `application/json`)
* `expires`: expiration datetime

#### 🛠️ Response Methods

| Method            | Description                        |
| ----------------- | ---------------------------------- |
| `make_response()` | Create a custom response           |
| `jsonify()`       | Return JSON data as a response     |
| `redirect()`      | Return 302 redirect to another URL |
| `abort()`         | Return an error response           |
| `set_cookie()`    | Set a cookie on client             |
| `delete_cookie()` | Delete a client-side cookie        |

---

### ✅ Summary

* Flask provides a `request` object for each client call with access to data, headers, and more.
* Flask automatically builds a `response` object, or you can customize it.
* Use attributes and helper methods to manage request and response behaviors efficiently.

## 🌐 Calling External APIs and Using Dynamic Routes in Flask

### 📥 Using `requests` to Call an External API

#### 🔧 Setup
1. Import `Flask`, `request`, and `requests`.
2. Install the `requests` library if not already done.

#### 📌 Example: Call OpenLibrary API

```python
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/author")
def get_author_books():
    res = requests.get("https://openlibrary.org/search.json?author=Michael+Crichton")
    if res.status_code == 200:
        return res.json()
    elif res.status_code == 404:
        return {"message": "Something went wrong"}, 404
    else:
        return {"message": "Server error"}, 500
```

* ✅ **200** → Return response JSON.
* ❌ **404** → Return message: “Something went wrong”.
* ❗️ Any other → Return status `500`: “Server error”.

---

### 🔁 Dynamic Routing in Flask

#### 📚 Example: Book Lookup by ISBN

```python
@app.route("/book/<isbn>")
def get_book_by_isbn(isbn):
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return {"message": "Book not found"}, res.status_code
```

* `/<isbn>` makes ISBN dynamic.
* Passes it to the function and uses it in the API call.

---

### 🔎 Parameter Types in Flask Routes

| Type   | Description                         |
| ------ | ----------------------------------- |
| string | (default) accepts any text          |
| int    | accepts only integers               |
| float  | accepts floating point numbers      |
| path   | like string but accepts slashes `/` |
| uuid   | accepts UUIDs (GUIDs)               |

#### 🛫 Example: Airport Terminals

```python
@app.route("/airport/<string:code>")
def get_airport_info(code):
    return {"airport": code.upper()}
```

#### 🔗 Example: UUID

```python
from uuid import UUID

@app.route("/network/<uuid:net_id>")
def get_network_info(net_id: UUID):
    # logic to verify net_id
    if is_valid_network(net_id):
        return {"message": "Network found"}
    else:
        return {"error": "Network not found"}, 404
```

---

### ✅ Summary

* Use the `requests` library to call external APIs in Flask.
* Return or process API responses based on their status codes.
* Use **dynamic routing** in Flask to build flexible RESTful APIs.
* Flask supports **parameter types** (string, int, float, path, uuid) for route validation.

## 🚨 Flask Error Handling

### 🎯 Learning Objectives
- Describe different HTTP status codes used by APIs.
- Explain how error handling works in Flask.
- Show how to return appropriate errors from API endpoints.

---

### 📊 HTTP Status Code Categories

| Range     | Meaning                      |
|-----------|------------------------------|
| 100–199   | Informational                |
| 200–299   | Success                      |
| 300–399   | Redirection                  |
| 400–499   | Client errors (request issue)|
| 500–599   | Server errors (server issue) |

---

### ✅ Common HTTP Status Codes in Flask

| Code | Description                                      |
|------|--------------------------------------------------|
| 200  | OK – Successful request (default in Flask)       |
| 201  | Created – Resource successfully created           |
| 202  | Accepted – Request accepted for processing        |
| 204  | No Content – Success but no content returned      |
| 400  | Bad Request – Invalid or missing request details  |
| 401  | Unauthorized – Missing/invalid credentials        |
| 403  | Forbidden – Access denied                         |
| 404  | Not Found – Resource not found                    |
| 405  | Method Not Allowed – Operation not supported      |
| 422  | Unprocessable Entity – Missing query param, etc.  |
| 500  | Internal Server Error – Something broke on server |

---

### 🔁 Returning Custom Status Codes

#### Flask Default Behavior
- Returning from a route returns status **200** automatically.
- `jsonify(...)` also returns **200** by default.

#### Override with Tuple

```python
@app.route("/")
def home():
    return "<h1>My First App</h1>", 200
```

#### Use `make_response`

```python
from flask import make_response

@app.route("/")
def custom_response():
    res = make_response("<h1>My First App</h1>")
    res.status_code = 200
    return res
```

---

### 🔍 Example: Error Handling in Route

```python
@app.route("/search")
def search_response():
    query = request.args.get("q")
    if not query:
        return {"message": "Input parameter missing"}, 422

    result = fetch_from_database(query)
    if result:
        return result
    else:
        return {"message": "Resource not found"}, 404
```

* **No query param** → 422
* **Valid resource** → 200
* **Missing resource** → 404

---

### 🧱 Flask Application-Level Error Handlers

```python
@app.errorhandler(404)
def not_found(e):
    return {"message": "API not found"}, 404

@app.errorhandler(500)
def server_error(e):
    return {"message": "Something went wrong on the server"}, 500
```

---

### ✅ Summary

* HTTP responses include status codes to indicate success or error.
* Flask returns **200 OK** by default unless you specify otherwise.
* You can return custom codes with a tuple or `make_response`.
* Flask supports **global error handlers** using `@app.errorhandler(...)`.