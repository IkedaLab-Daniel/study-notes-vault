
# Installation Guide: Laravel + Breeze + Tailwind CSS

## 1. Prerequisites
Make sure you have these installed:
- **PHP 8.1 or higher** → check with: `php -v`
- **Composer** → check with: `composer -V`
- **Node.js + npm** → check with: `node -v` and `npm -v`
- **Database** (MySQL, MariaDB, PostgreSQL, SQLite)

---

## 2. Create a New Laravel Project
```bash
composer create-project laravel/laravel myapp
cd myapp
```

---

## 3. Configure Environment

```bash
cp .env.example .env   # (Windows: copy .env.example .env)
php artisan key:generate
```

Edit `.env` and configure your database:

```env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=myapp_db
DB_USERNAME=root
DB_PASSWORD=
```

---

## 4. Run Initial Migration

```bash
php artisan migrate
```

---

## 5. Install Breeze (Auth Scaffolding with Tailwind)

```bash
composer require laravel/breeze --dev
php artisan breeze:install blade
```

---

## 6. Install Node Packages & Build

```bash
npm install
npm run dev
```

---

## 7. Migrate Auth Tables

```bash
php artisan migrate
```

---

## 8. Serve the Application

```bash
php artisan serve
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 9. Optional Production Build

```bash
npm run build
php artisan config:cache
```

---

## 10. Create a Route for Testing Tailwind

**File:** `routes/web.php`

```php
Route::get('/tailwind-demo', function () {
    return view('tailwind-demo');
});
```

---

## 11. Create a Blade View with Tailwind Components

**File:** `resources/views/tailwind-demo.blade.php`

```blade
@extends('layouts.app')

@section('content')
<div class="max-w-4xl mx-auto p-8">
    <h1 class="text-3xl font-bold text-center mb-6 text-indigo-600">
        ■ Tailwind CSS Demo Page
    </h1>

    <!-- Example Card -->
    <div class="bg-white shadow-lg rounded-2xl p-6 mb-6">
        <h2 class="text-xl font-semibold mb-2">Card Component</h2>
        <p class="text-gray-600">
            This is a simple Tailwind CSS card with padding, rounded corners, and a shadow.
        </p>
    </div>

    <!-- Example Button -->
    <div class="mb-6">
        <button class="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg shadow">
            Tailwind Button
        </button>
    </div>

    <!-- Example Alert -->
    <div class="p-4 mb-6 text-sm text-green-800 rounded-lg bg-green-100 border border-green-300" role="alert">
        ■ This is a success alert — styled with Tailwind!
    </div>

    <!-- Example Table -->
    <div class="overflow-x-auto shadow-md rounded-lg">
        <table class="min-w-full border border-gray-200">
            <thead class="bg-gray-100">
                <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Email</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Role</th>
                </tr>
            </thead>
            <tbody>
                <tr class="bg-white border-b">
                    <td class="px-6 py-4">John Doe</td>
                    <td class="px-6 py-4">john@example.com</td>
                    <td class="px-6 py-4">Admin</td>
                </tr>
                <tr class="bg-gray-50 border-b">
                    <td class="px-6 py-4">Jane Smith</td>
                    <td class="px-6 py-4">jane@example.com</td>
                    <td class="px-6 py-4">User</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
@endsection
```

---

## 12. Visit the Demo Page

```bash
php artisan serve
npm run dev
```

Open [http://127.0.0.1:8000/tailwind-demo](http://127.0.0.1:8000/tailwind-demo)