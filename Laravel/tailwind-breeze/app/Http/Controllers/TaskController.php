<?php

namespace App\Http\Controllers;

use App\Models\Task;
use Illuminate\Http\Request;

class TaskController extends Controller
{
    public function index(Request $request)
    {
        $tasks = $request->user()->tasks()->latest()->get();
        return view('tasks.index', compact('tasks'));
    }

    public function create()
    {
        return view('tasks.create'); // ! TBI
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'title' => 'required|max:255',
            'description' => 'nullable',
        ]);

        // > use the relationship to create the tasl
        $request->user()->tasks()->create($validated);

        return redirect()->route('tasks.index')->with('success', 'Created successfully');
    }

    public function edit(Task $task, Request $request)
    {
        if ($task->user_id !== $request->user()->id){
            abort(403);
        }

        return view('tasks.edit', compact('task'));
    }

    public function update(Request $request, Task $task)
    {   
        if ($task->user_id !== $request->user()->id){
            abort(403);
        }

        $request->validate([
            'title' => 'required|max:255',
            'description'=>'nullable'
        ]);

        $task->update($request->only('title', 'description', 'completed'));

        return redirect()->route('tasks.index')->with('success', 'Task has been updated successfully!'); // ? success message is stored in session
    }

    public function destroy(Task $task, Request $request)
    {
        if ($task->user_id !== $request->user()->id){
            abort(403);
        }

        $task->delete();
        return redirect()->route('tasks.index')->with('success', 'Task deleted successfully');
    }

    public function publicDashboard()
    {
        $tasks = Task::with('user')->latest()->get();
        return view('tasks.dashboard', compact('tasks'));
    }
}
