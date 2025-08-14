## **📦 Project Setup**

| Command                                                | Description                                               |
| ------------------------------------------------------ | --------------------------------------------------------- |
| `laravel new project-name`                             | Create a new Laravel project (requires Laravel installer) |
| `composer create-project laravel/laravel project-name` | Create Laravel project via Composer                       |
| `php artisan serve`                                    | Start local development server                            |
| `php artisan --version`                                | Check Laravel version                                     |
| `php artisan list`                                     | Show all Artisan commands                                 |
| `php artisan help command`                             | Show help for a command                                   |

---

## **🗄️ Database & Migrations**

| Command                                              | Description                                   |
| ---------------------------------------------------- | --------------------------------------------- |
| `php artisan migrate`                                | Run all pending migrations                    |
| `php artisan migrate:rollback`                       | Rollback last batch of migrations             |
| `php artisan migrate:reset`                          | Rollback all migrations                       |
| `php artisan migrate:refresh`                        | Reset & re-run all migrations                 |
| `php artisan migrate:fresh`                          | Drop all tables & run migrations from scratch |
| `php artisan make:migration create_table_name_table` | Create a new migration file                   |
| `php artisan db:seed`                                | Seed the database                             |
| `php artisan migrate --seed`                         | Migrate & seed database                       |
| `php artisan make:seeder SeederName`                 | Create a new seeder file                      |
| `php artisan db:wipe`                                | Delete all tables, views, and types           |

---

## **🧩 Models, Controllers, & Resources**

| Command                                                 | Description                           |
| ------------------------------------------------------- | ------------------------------------- |
| `php artisan make:model ModelName`                      | Create a new model                    |
| `php artisan make:model ModelName -m`                   | Create a model with migration         |
| `php artisan make:model ModelName -mc`                  | Model + Controller                    |
| `php artisan make:model ModelName -mfsc`                | Model + Factory + Seeder + Controller |
| `php artisan make:controller ControllerName`            | Create controller                     |
| `php artisan make:controller ControllerName --resource` | Create resource controller            |
| `php artisan make:resource ResourceName`                | Create API resource                   |
| `php artisan make:factory FactoryName`                  | Create a model factory                |

---

## **🔧 Routes & Caching**

| Command                    | Description                    |
| -------------------------- | ------------------------------ |
| `php artisan route:list`   | List all routes                |
| `php artisan route:cache`  | Cache routes for performance   |
| `php artisan route:clear`  | Clear cached routes            |
| `php artisan config:cache` | Cache config files             |
| `php artisan config:clear` | Clear config cache             |
| `php artisan cache:clear`  | Clear application cache        |
| `php artisan view:clear`   | Clear compiled Blade templates |

---

## **🎨 Views & Frontend**

| Command                          | Description                                                      |
| -------------------------------- | ---------------------------------------------------------------- |
| `php artisan make:view viewname` | (If using Laravel 11+ built-in make\:view) Create new Blade view |
| `npm install`                    | Install frontend dependencies                                    |
| `npm run dev`                    | Build assets for development                                     |
| `npm run build`                  | Build assets for production                                      |

---

## **🧪 Testing**

| Command                          | Description        |
| -------------------------------- | ------------------ |
| `php artisan make:test TestName` | Create a test file |
| `php artisan test`               | Run tests          |

---

## **⚙️ Queue & Jobs**

| Command                        | Description           |
| ------------------------------ | --------------------- |
| `php artisan queue:work`       | Start processing jobs |
| `php artisan queue:listen`     | Listen for new jobs   |
| `php artisan make:job JobName` | Create a new job      |

---

## **👤 Authentication & Users**

| Command                                | Description                                      |
| -------------------------------------- | ------------------------------------------------ |
| `php artisan make:auth`                | (For Laravel UI package) Create auth scaffolding |
| `php artisan make:request RequestName` | Create form request validation class             |

---

## **🚀 Deployment Helpers**

| Command                      | Description                        |
| ---------------------------- | ---------------------------------- |
| `php artisan optimize`       | Cache config, routes, and views    |
| `php artisan optimize:clear` | Clear all caches                   |
| `composer dump-autoload`     | Regenerate Composer autoload files |