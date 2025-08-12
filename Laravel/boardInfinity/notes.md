## **What is Laravel?**

* **Open-source PHP framework** created by **Taylor Otwell**.
* Uses **MVC (Model–View–Controller)** architecture to separate:

  * **Model** → Data
  * **View** → User interface
  * **Controller** → Business logic
* Based on **Symfony** components.
* Designed for **developer friendliness** with strong documentation.

---

## **Why is Laravel Popular?**

* **Modular packaging system** for better code organization.
* **Built-in utilities** for deployment & maintenance.
* **Syntactic sugar** for cleaner, more readable code.

---

## **Key Features**

1. **MVC Architecture** – Organized, reusable code for large projects.
2. **Eloquent ORM** – Simplifies database connectivity through Object-Relational Mapping.
3. **Blade Templating Engine** – Easy, expressive template syntax for dynamic pages.
4. **Authentication & Authorization** – Built-in, secure access control.
5. **Security** – Password hashing, XSS prevention, SQL injection protection.
6. **Artisan CLI** – Command-line tool to generate code, run tasks, and manage apps.

---

## **Advantages**

* **Easy to Learn** – Beginner-friendly design.
* **Large Community** – Active support, tutorials, and resources.
* **Wide Range of Packages** – Speeds up development.
* **Scalable** – Handles high traffic efficiently.
* **Secure by Default** – Strong out-of-the-box security features.

---

## **Setting Up Laravel Development Environment**

### **Prerequisites**

* **PHP**
* **Composer**
* **Web server** (Apache recommended)
* **Database** (MySQL for this exercise)
* Add dependencies to **environment variables** for easy terminal access.

---

### **Setup Steps**

1. **Create a directory** for Laravel projects.
2. **Install Laravel installer globally**:

   ```bash
   composer global require laravel/installer
   ```
3. **Create a new project**:

   ```bash
   laravel new demo_project
   ```
4. **Choose options**:

   * Starter kits (optional) – authentication system or none.
   * Testing framework – PHP Unit (commonly preferred).
   * Git repository – optional initialization.
5. Laravel automatically:

   * Generates a project structure with basic code architecture.
   * Runs `php artisan key:generate`.
   * Prompts for database selection (MySQL in this example).

### **Laravel Project Structure Overview**

#### **1. `app/`**

* **Heart of the application** — contains most of your custom code.
* **`Http/`**

  * **Controllers**: Handle incoming HTTP requests and return responses.
  * **Middleware**: Filter requests before they reach your application.
* **`Providers/`**: Service providers that bind classes and perform tasks during bootstrapping.
* **`Console/`**: Your custom Artisan commands.
* **`Exceptions/`**: Custom exception classes to handle and categorize errors.

---

#### **2. `bootstrap/`**

* Holds files needed to **bootstrap the Laravel application**.
* **`app.php`**: Initializes the app and loads service providers.

---

#### **3. `config/`**

* Stores all **configuration files** for Laravel components (e.g., database connections, mail settings, cache).

---

#### **4. `public/`**

* **Web-accessible directory** — the entry point of your application.
* **`index.php`**: Main entry point for all incoming requests.
* **`favicon.ico`**: The site’s favicon.

---

### **Tips from the video**

1. **Use namespaces** to organize code for easier access.
2. Stick to Laravel’s given folder structure (controllers, models, views already separated).
3. Use **descriptive file and folder names**.
4. **Document your code** so you (and others) can understand it later.

## Laravel Routing, Controllers, and Views

* **Routing** matches incoming requests to specific code in your application.
* Defined using the `Route` class methods (e.g., `Route::get()` for HTTP GET requests).
* Routes are stored in the **`routes/`** directory:

  * **`web.php`**: For web interface routes, includes session state & CSRF protection.
  * **`api.php`**: For stateless API routes with API middleware group.
* Example: `Route::get('/user', function () { return 'User loaded'; });`
* **Artisan CLI** (`php artisan serve`) runs the local development server.
* **Views** are returned using the `view()` function, stored in **`resources/views/`** as Blade templates (`.blade.php`).
* Data can be passed from routes/controllers to views for dynamic HTML output.

## Laravel Controllers and Views

* **Controllers** handle incoming HTTP requests, perform tasks (e.g., retrieving data, validating input), and return responses.
* **Views** generate HTML for the user; Blade templates enable dynamic content generation.
* Tips:

  * Use dependency injection for testable, reusable code.
  * Use view composers to pass common data to multiple views.
  * Document controllers and views for maintainability.
* Controller methods handle specific routes (e.g., GET `/user` or POST `/login`).
* Logic should be in controllers, keeping route files clean.
* Create controllers with `php artisan make:controller`.
* Map routes to controller methods using `[Controller::class, 'method']`.
* Pass data from controllers to views (e.g., fetching user data from DB).
* Use **migrations** (`php artisan migrate`) to create tables and **seeders** (`php artisan db:seed`) to populate initial data.
* Ensure proper imports for models, controllers, and routes to avoid errors.
