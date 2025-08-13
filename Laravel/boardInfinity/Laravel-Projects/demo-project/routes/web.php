<?php

use App\Http\Controllers\UserController;
use App\Http\Controllers\CourseController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/user/{id}', [UserController::class, 'getUser']);
Route::get('/course', [CourseController::class, 'index']);
Route::get('/course/{id}', [CourseController::class, 'findCourse']);