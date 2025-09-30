@extends('layouts.app')

@section('content')
<div class="max-w-6xl mx-auto p-8 bg-gray-800 min-h-[100vh]">
    <h1 class="text-3xl font-bold mb-6 text-gray-800">Tasks List</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        @foreach($tasks as $task)
            <div class="bg-slate-600 text-white rounded-lg p-6 shadow-lg">
                <h3 class="text-xl font-semibold mb-2">{{ $task->title }}</h3>
                <p class="text-gray-200 mb-3">{{ $task->description }}</p>
                <p class="text-sm">
                    <span class="font-medium">Status:</span>
                    @if($task->status)
                        <span class="bg-green-500 px-2 py-1 rounded text-xs">Completed</span>
                    @else
                        <span class="bg-red-500 px-2 py-1 rounded text-xs">Pending</span>
                    @endif
                </p>
                <form action="{{ route('tasks.destroy', $task) }}" method="POST">
                    @csrf @method('DELETE')
                    <button
                        class="mt-4 p-1 w-[100%] bg-red-600 rounded hover:scale-105 transition-transform duration-500"

                        type="submit"
                    >Delete</button>
                </form>
            </div>
        @endforeach
    </div>
</div>
@endsection