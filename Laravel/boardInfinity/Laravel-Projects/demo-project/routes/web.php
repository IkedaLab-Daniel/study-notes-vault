<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

// ? MY VERY FIRST LARAVEL OUTPUT
Route::get('/myfirstoutput', function (){
    return 'Doomshop, mothafucka';
});

Route::get('/user', function (){
    return view('user');
});