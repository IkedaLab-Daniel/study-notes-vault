<x-app-layout>
    <body class="bg-gray-700 ">
        @if (count($notes) == 0)
            <h1 class="text-gray-100 text-5xl">No notes yet</h1>
        @else
            <h1>{{ notes }}</h1>
        @endif
        <h1>{{ $user_name }}</h1>
    </body>
</x-app-layout>