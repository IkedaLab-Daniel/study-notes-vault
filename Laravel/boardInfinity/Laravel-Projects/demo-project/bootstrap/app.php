<?php

use Illuminate\Foundation\Application;
use Illuminate\Foundation\Configuration\Exceptions;
use Illuminate\Foundation\Configuration\Middleware;

return Application::configure(basePath: dirname(__DIR__))
    ->withRouting(
        web: __DIR__.'/../routes/web.php',
        api: __DIR__.'/../routes/api.php',
        commands: __DIR__.'/../routes/console.php',
        health: '/up',
    )
    ->withMiddleware(function (Middleware $middleware): void {
        // Register custom middleware
        $middleware->alias([
            'check.headers' => \App\Http\Middleware\CheckHeaders::class,
        ]);
        
        // Or add it to global middleware stack (applies to all routes)
        // $middleware->append(\App\Http\Middleware\CheckHeaders::class);
        
        // Or add it to web middleware group
        // $middleware->web(append: [
        //     \App\Http\Middleware\CheckHeaders::class,
        // ]);
    })
    ->withExceptions(function (Exceptions $exceptions): void {
        //
    })->create();
