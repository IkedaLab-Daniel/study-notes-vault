<?php

namespace App\Http\Controllers;

use App\Models\Task;
use Illuminate\Http\Request;
use Illuminate\View\View;

class TaskController extends Controller
{
    public function show(): View
    {
        return view('task.index', [
            'title' => Task::all()
        ]);
    }
}
