<x-app-layout>
    <div class="max-w-[1200px] mx-auto p-4 lg:p-0">
        <h1 class="text-gray-100 text-4xl my-4 font-semibold">My Note:</h1>
        <div class="grid md:grid-cols-4 md:gap-4 gap-1">
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
        
        <button class="text-gray-50 text-xl bg-blue-700 px-4 py-2 rounded-md fixed bottom-[50px] hover:scale-105 transition-all duration-500 right-[50px] shadow-md md:left-[10vw] md:right-auto">
            + Add new note
        </button>

    </div>
</x-app-layout>