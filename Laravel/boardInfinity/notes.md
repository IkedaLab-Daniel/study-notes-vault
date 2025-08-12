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