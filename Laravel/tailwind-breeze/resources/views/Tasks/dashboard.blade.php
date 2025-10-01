@extends('layouts.app')

@section('content')
    <div>
        <h1 class="p-4 text-5xl font-bold mb-6 text-gray-100">All tasks:</h1>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-2 p-4 text-white">
            @foreach ($tasks as $task)
                <div class="bg-gray-700 p-4 rounded-md">
                    <p>Name: {{ $task->title }}</p>
                    @if($task->title)
                        <p>Description: {{ $task->title }}</p>
                    @else
                        <p>Description: No description</p>
                    @endif
                    <p>By: {{ $task->user->name }}</p>
                    <p>Created at: {{ $task->created_at->format('F j, Y') }}</p>
                </div>
            @endforeach
        </div>
    </div>
@endsection