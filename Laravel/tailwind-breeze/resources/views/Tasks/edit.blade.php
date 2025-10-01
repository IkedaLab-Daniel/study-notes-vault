@extends('layouts.app')

@section('content')
<div class="max-w-2xl mx-auto p-8 bg-gray-800 min-h-[100vh]">
    <div class="bg-slate-600 text-white rounded-lg shadow-lg p-6">
        <h1 class="text-3xl font-bold mb-6 text-gray-100">Create New Task</h1>
        
        <form action="{{ route('tasks.update', $task) }}" method="POST" class="space-y-6">
            @csrf
            @method('PUT')
            <!-- Title Field -->
            <div>
                <label for="title" class="block text-sm font-medium text-gray-200 mb-2">
                    Task Title
                </label>
                <input 
                    type="text" 
                    id="title" 
                    name="title" 
                    class="w-full px-4 py-2 bg-gray-700 border border-gray-500 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-white placeholder-gray-400"
                    placeholder="Enter task title"
                    value="{{ $task->title }}"
                    required
                >
            </div>

            <!-- Description Field -->
            <div>
                <label for="description" class="block text-sm font-medium text-gray-200 mb-2">
                    Description
                </label>
                <textarea 
                    id="description" 
                    name="description" 
                    rows="4"
                    class="w-full px-4 py-2 bg-gray-700 border border-gray-500 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-white placeholder-gray-400"
                    placeholder="Enter task description"
                    required
                >{{ $task->description }}</textarea>
            </div>

            <!-- Buttons -->
            <div class="flex justify-between items-center pt-4">
                <a 
                    href="{{ route('tasks.index') }}" 
                    class="px-6 py-2 bg-gray-500 text-white rounded-lg hover:bg-gray-600 hover:scale-105 transition-all duration-200"
                >
                    Cancel
                </a>
                <button 
                    type="submit" 
                    class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 hover:scale-105 transition-all duration-200"
                >
                    Update task
            </div>
        </form>
    </div>
</div>
@endsection