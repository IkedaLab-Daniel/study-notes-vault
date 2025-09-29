<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Index for task</h1>
    <div>
        <h2>Tasks:</h2>
         @foreach($tasks as $task)
            <div class="bg-slate-600 w-[300px] h-[300px]">
                <p>Title: {{ $task->title }}</p>
                <p>Description: {{ $task->description }}</p>
                <p>Due Date: {{ $task->due }}</p>
                <p>Status: {{ $task->status }}</p>
            </div>
        
        @endforeach
    </div>
   
</body>
</html>