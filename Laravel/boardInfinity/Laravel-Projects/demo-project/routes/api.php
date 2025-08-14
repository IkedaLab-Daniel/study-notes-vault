<?php

use App\Http\Controllers\API\CourseAPIController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

// Example API routes - you can add your API controllers here
// Route::apiResource('courses', App\Http\Controllers\API\CourseApiController::class);
// Route::get('/courses/{id}', [App\Http\Controllers\API\CourseApiController::class, 'show']);
Route::apiResource('course', CourseAPIController::class);