<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>User Profile</title>
    @vite(['resources/css/app.css', 'resources/js/app.js'])
</head>
<body class="bg-gray-50 dark:bg-gray-900 min-h-screen py-8">
    <div class="max-w-4xl mx-auto px-4">
        <div class="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
            @if($user)
                <div class="flex items-center space-x-4">
                    <div class="w-16 h-16 bg-blue-500 rounded-full flex items-center justify-center text-white text-xl font-bold">
                        {{ strtoupper(substr($user->name, 0, 1)) }}
                    </div>
                    <div>
                        <h1 class="text-2xl font-bold text-gray-900 dark:text-white">{{ $user->name }}</h1>
                        <p class="text-gray-600 dark:text-gray-300">{{ $user->email }}</p>
                        <p class="text-sm text-gray-500 dark:text-gray-400">
                            Joined: {{ $user->created_at->format('M d, Y') }}
                        </p>
                    </div>
                </div>
                
                <div class="mt-8">
                    <h2 class="text-lg font-semibold text-gray-900 dark:text-white mb-4">User Information</h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded">
                            <label class="text-sm font-medium text-gray-700 dark:text-gray-300">User ID</label>
                            <p class="text-gray-900 dark:text-white">{{ $user->id }}</p>
                        </div>
                        <div class="bg-gray-50 dark:bg-gray-700 p-4 rounded">
                            <label class="text-sm font-medium text-gray-700 dark:text-gray-300">Email Verified</label>
                            <p class="text-gray-900 dark:text-white">
                                {{ $user->email_verified_at ? 'Yes' : 'No' }}
                            </p>
                        </div>
                    </div>
                </div>
            @else
                <div class="text-center py-12">
                    <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center text-red-500 text-2xl mx-auto mb-4">
                        !
                    </div>
                    <h1 class="text-2xl font-bold text-gray-900 dark:text-white mb-2">User Not Found</h1>
                    <p class="text-gray-600 dark:text-gray-300">The requested user could not be found in the database.</p>
                </div>
            @endif
            
            <div class="mt-8 pt-6 border-t border-gray-200 dark:border-gray-600">
                <a href="{{ url('/') }}" class="inline-flex items-center px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-md transition-colors">
                    ← Back to Home
                </a>
            </div>
        </div>
    </div>
</body>
</html>
