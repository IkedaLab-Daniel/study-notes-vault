<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CheatsheetController extends Controller
{
    public function index()
    {
        $commandSections = [
            'Project Setup' => [
                'icon' => '📦',
                'commands' => [
                    ['command' => 'laravel new project-name', 'description' => 'Create a new Laravel project (requires Laravel installer)'],
                    ['command' => 'composer create-project laravel/laravel project-name', 'description' => 'Create Laravel project via Composer'],
                    ['command' => 'php artisan serve', 'description' => 'Start local development server'],
                    ['command' => 'php artisan --version', 'description' => 'Check Laravel version'],
                    ['command' => 'php artisan list', 'description' => 'Show all Artisan commands'],
                    ['command' => 'php artisan help command', 'description' => 'Show help for a command'],
                ]
            ],
            'Database & Migrations' => [
                'icon' => '🗄️',
                'commands' => [
                    ['command' => 'php artisan migrate', 'description' => 'Run all pending migrations'],
                    ['command' => 'php artisan migrate:rollback', 'description' => 'Rollback last batch of migrations'],
                    ['command' => 'php artisan migrate:reset', 'description' => 'Rollback all migrations'],
                    ['command' => 'php artisan migrate:refresh', 'description' => 'Reset & re-run all migrations'],
                    ['command' => 'php artisan migrate:fresh', 'description' => 'Drop all tables & run migrations from scratch'],
                    ['command' => 'php artisan make:migration create_table_name_table', 'description' => 'Create a new migration file'],
                    ['command' => 'php artisan db:seed', 'description' => 'Seed the database'],
                    ['command' => 'php artisan migrate --seed', 'description' => 'Migrate & seed database'],
                    ['command' => 'php artisan make:seeder SeederName', 'description' => 'Create a new seeder file'],
                    ['command' => 'php artisan db:wipe', 'description' => 'Delete all tables, views, and types'],
                ]
            ],
            'Models, Controllers & Resources' => [
                'icon' => '🧩',
                'commands' => [
                    ['command' => 'php artisan make:model ModelName', 'description' => 'Create a new model'],
                    ['command' => 'php artisan make:model ModelName -m', 'description' => 'Create a model with migration'],
                    ['command' => 'php artisan make:model ModelName -mc', 'description' => 'Model + Controller'],
                    ['command' => 'php artisan make:model ModelName -mfsc', 'description' => 'Model + Factory + Seeder + Controller'],
                    ['command' => 'php artisan make:controller ControllerName', 'description' => 'Create controller'],
                    ['command' => 'php artisan make:controller ControllerName --resource', 'description' => 'Create resource controller'],
                    ['command' => 'php artisan make:resource ResourceName', 'description' => 'Create API resource'],
                    ['command' => 'php artisan make:factory FactoryName', 'description' => 'Create a model factory'],
                ]
            ],
            'Routes & Caching' => [
                'icon' => '🔧',
                'commands' => [
                    ['command' => 'php artisan route:list', 'description' => 'List all routes'],
                    ['command' => 'php artisan route:cache', 'description' => 'Cache routes for performance'],
                    ['command' => 'php artisan route:clear', 'description' => 'Clear cached routes'],
                    ['command' => 'php artisan config:cache', 'description' => 'Cache config files'],
                    ['command' => 'php artisan config:clear', 'description' => 'Clear config cache'],
                    ['command' => 'php artisan cache:clear', 'description' => 'Clear application cache'],
                    ['command' => 'php artisan view:clear', 'description' => 'Clear compiled Blade templates'],
                ]
            ],
            'Views & Frontend' => [
                'icon' => '🎨',
                'commands' => [
                    ['command' => 'php artisan make:view viewname', 'description' => 'Create new Blade view (Laravel 11+)'],
                    ['command' => 'npm install', 'description' => 'Install frontend dependencies'],
                    ['command' => 'npm run dev', 'description' => 'Build assets for development'],
                    ['command' => 'npm run build', 'description' => 'Build assets for production'],
                ]
            ],
            'Testing' => [
                'icon' => '🧪',
                'commands' => [
                    ['command' => 'php artisan make:test TestName', 'description' => 'Create a test file'],
                    ['command' => 'php artisan test', 'description' => 'Run tests'],
                ]
            ],
            'Queue & Jobs' => [
                'icon' => '⚙️',
                'commands' => [
                    ['command' => 'php artisan queue:work', 'description' => 'Start processing jobs'],
                    ['command' => 'php artisan queue:listen', 'description' => 'Listen for new jobs'],
                    ['command' => 'php artisan make:job JobName', 'description' => 'Create a new job'],
                ]
            ],
            'Authentication & Users' => [
                'icon' => '👤',
                'commands' => [
                    ['command' => 'php artisan make:auth', 'description' => 'Create auth scaffolding (Laravel UI package)'],
                    ['command' => 'php artisan make:request RequestName', 'description' => 'Create form request validation class'],
                ]
            ],
            'Deployment Helpers' => [
                'icon' => '🚀',
                'commands' => [
                    ['command' => 'php artisan optimize', 'description' => 'Cache config, routes, and views'],
                    ['command' => 'php artisan optimize:clear', 'description' => 'Clear all caches'],
                    ['command' => 'composer dump-autoload', 'description' => 'Regenerate Composer autoload files'],
                ]
            ]
        ];

        return view('cheatsheet.index', ['commandSections' => $commandSections]);
    }
}
