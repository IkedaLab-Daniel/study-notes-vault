<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use Symfony\Component\HttpFoundation\Response;

class CheckHeaders
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        // These will show in artisan serve terminal:
        
        // 1. Log::info() - Shows in terminal
        Log::info("🔥 Custom Middleware was called - INFO level");
        
        // 2. Log::warning() - Shows in terminal
        Log::warning("⚠️  Custom Middleware - WARNING level");
        
        // 3. Log::error() - Shows in terminal
        Log::error("❌ Custom Middleware - ERROR level");
        
        // 4. Direct output methods (for development only):
        echo "📍 Middleware executed - using echo\n";
        
        // 5. Using error_log() - appears in terminal
        error_log("🐛 Middleware called - using error_log");
        
        // Headers info (using info level so it shows)
        Log::info("📋 Request Headers: " . json_encode($request->header()));

        $ua = $request->header('user-agent');
        if (str_contains($ua, 'Hacker Browser')){
            return redirect('unauth');
        };
        
        return $next($request);
    }
}
