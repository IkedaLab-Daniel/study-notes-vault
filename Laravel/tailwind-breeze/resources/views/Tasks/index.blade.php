@extends('layouts.app')

@section('content')
<div class="max-w-6xl mx-auto p-8 bg-gray-800 min-h-[100vh] relative">
    @if(session('success'))
        <!-- Success message -->
        <div class="bg-green-600 py-2 px-5 rounded-md inline"> 
            <svg class="w-5 h-5 text-green-50 inline mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
            </svg>
            <p class="text-green-50 inline">{{session('success')}}</p>
        </div>
    @endif
    
    <h1 class="mt-4 text-3xl font-bold mb-6 text-gray-100">Tasks List</h1>
    <a href="{{ route('tasks.create') }}" class="w-full ">
        <p class="mb-4 bg-blue-600 text-center text-white py-2 px-4 rounded md:w-auto md:absolute md:right-7 md:top-7 hover:scale-105 transition-all duration-200 fixed bottom-0 w-[85%] shadow-2xl md:bottom-auto">
            Add new task
        </p>
    </a>
    @if(count($tasks) == 0)
        <div class="flex justify-center items-center h-[300px] flex-col gap-1">
            <svg class="w-20 h-20 text-gray-200" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
            </svg>
            <p class="text-gray-200 text-3xl">No task yet</p>
        </div>
    @endif
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        @foreach($tasks as $task)
            <div class="bg-slate-600 text-white rounded-lg p-6 shadow-lg">
                <h3 class="text-xl font-semibold mb-2">{{ $task->title }}</h3>
                <p class="text-gray-200 mb-3">{{ $task->description }}</p>
                <p class="text-sm">
                    <span class="font-medium">Status:</span>
                    @if($task->completed == true)
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
                    <a href="{{ route('tasks.edit', $task) }}" class="w-[50%]">
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