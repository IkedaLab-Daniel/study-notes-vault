<x-app-layout>
    <div class="max-w-[1200px] mx-auto">
        <h1 class="text-gray-100 text-4xl my-4 font-semibold">My Note:</h1>
        <div class="grid md:grid-cols-4 gap-4">
            @foreach($notes as $note)
                <div class="mt-4 text-gray-100 bg-gray-700 p-4 rounded-md hover:scale-105 transition-all duration-500">
                    <p class="text-center font-bold text-2xl">"{{ $note->title }}"</p>
                    <div class="border-t border-gray-400 my-3"></div>
                    <p>{{ $note->message }}</p>
                    <div class="border-t border-gray-400 my-3"></div>
                    <p class="text-right text-sm italic">{{ $note->created_at->format('F j, Y') }}</p>
                </div>
            @endforeach
        </div>
    </div>
</x-app-layout>