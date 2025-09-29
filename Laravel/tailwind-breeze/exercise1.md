## 🚀 Exercise Problem: "Mini Task Manager"

**Goal:** Build a small Task Manager app where users can sign up, log in, and manage their tasks.

---

### Requirements

#### 1. Authentication (Laravel Breeze)

* Use **Laravel Breeze** for login, registration, and authentication.
* A logged-in user can only see their own tasks.
* Guests can only see the login/register page.

#### 2. Database

* Create a `tasks` table with:

  * `id`
  * `user_id` (foreign key → users table)
  * `title` (string, required)
  * `description` (text, optional)
  * `status` (enum: "pending", "in-progress", "completed")
  * `created_at`, `updated_at`

#### 3. Features

* **Task CRUD**:

  * Create a task with a title & description.
  * Edit a task.
  * Delete a task.
  * Mark a task as "in-progress" or "completed".
* **User-specific data**:

  * Each user only sees their own tasks.
* **Validation**:

  * `title` is required.
  * `description` max length 500.

#### 4. UI (Tailwind)

* Dashboard page with:

  * A **form** to add a new task.
  * A **table** or **cards** to list tasks.
  * Tailwind classes for styling (rounded corners, hover effects, responsive).
* Show task **status** with colored badges:

  * pending → gray
  * in-progress → yellow
  * completed → green
* Add a button group (Edit | Delete | Update Status).

#### 5. Bonus Challenge

* Add a **search bar** (filter tasks by title).
* Add a **status filter dropdown** (pending/in-progress/completed).
* Use Tailwind components (like modals or alerts) for a better UI.

---

### What You’ll Practice

* Laravel fundamentals: routes, controllers, models, migrations.
* Breeze authentication system.
* Relationships (`User hasMany Tasks`).
* Blade templating + Tailwind UI.
* Validation and middleware protection.