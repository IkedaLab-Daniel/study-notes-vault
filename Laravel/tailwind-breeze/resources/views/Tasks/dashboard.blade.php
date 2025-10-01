@extends('layouts.app')

@section('content')
    <div>
        @foreach ($tasks as $task)
            <p class="text-white">{{ $task }}</p>
        @endforeach
    </div>
@endsection