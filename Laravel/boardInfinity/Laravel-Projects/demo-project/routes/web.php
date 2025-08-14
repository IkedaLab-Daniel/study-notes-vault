<?php

use App\Http\Controllers\UserController;
use App\Http\Controllers\CourseController;
use App\Http\Controllers\CheatsheetController;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Auth;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/unauth', function () {
    return response()->json([
        'status' => 'unauthorized',
        'message' => 'Access denied: Browser detected',
        'redirect_reason' => 'Mozilla user-agent found in request headers'
    ], 403);
});

Route::get('/user/{id}', [UserController::class, 'getUser']);
Route::get('/course', [CourseController::class, 'index']);
Route::get('/course/{id}', [CourseController::class, 'findCourse'])->middleware('check.headers');
Route::get('/cheatsheet', [CheatsheetController::class, 'index']);
Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');

Route::get('/profile', function(){
    return view('layouts.profile');
});