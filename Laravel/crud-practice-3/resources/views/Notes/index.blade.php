<x-app-layout>
    <h1 class="text-gray-100 text-4xl">Sample</h1>
    @foreach($notes as $note)
        <div class="text-gray-100">
            <p>{{ $note->title }}</p>
        </div>
    @endforeach
</x-app-layout>