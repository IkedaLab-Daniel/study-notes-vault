@extends('layouts.app')

@section('content')
<div class="max-w-6xl mx-auto p-8 bg-gray-800 min-h-[100vh] relative">
    <h1 class="text-3xl font-bold mb-6 text-gray-100">Tasks List</h1>
    <a href="" class="w-full ">
        <p class="mb-4 bg-blue-600 text-center text-white py-2 px-4 rounded w-auto absolute right-7 top-7 hover:scale-105 transition-all duration-200">
            Add new task
        </p>
    </a>
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
                <div class="mt-2 w-full flex justify-center gap-3">
                    <form action="{{ route('tasks.destroy', $task) }}" method="POST" class="w-[50%]">
                        @csrf @method('DELETE')
                        <button class="p-1 w-full bg-red-600 rounded hover:scale-105 transition-transform duration-500" type="submit">
                            Delete
                        </button>
                    </form>
                    <a href="" class="w-[50%]">
                        <button class="p-1 w-full bg-blue-500 rounded hover:scale-105 transition-transform duration-500">
                            Edit
                        </button>
                    </a>
                </div>
            </div>
        @endforeach
    </div>
</div>
@endsection