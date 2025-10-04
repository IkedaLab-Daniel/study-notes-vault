<x-app-layout>
    <div class="max-w-[1200px] mx-auto p-4 lg:p-0">
        @if (session('success'))
            <div class="mt-4 font-bold text-green-100 bg-green-700 px-4 py-3 rounded-sm flex items-center gap-2">
                <svg class="w-[20px]" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M8.5 12.5L10.5 14.5L15.5 9.5" stroke="#d5f8e1" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M7 3.33782C8.47087 2.48697 10.1786 2 12 2C17.5228 2 22 6.47715 22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 10.1786 2.48697 8.47087 3.33782 7" stroke="#d5f8e1" stroke-width="1.5" stroke-linecap="round"></path> </g></svg>
                <p>{{ session('success') }}</p>
            </div>
        @endif
        <h1 class="text-gray-100 text-4xl my-4 font-semibold">My Note:</h1>
        <div class="grid md:grid-cols-4 md:gap-4 gap-1">
            @foreach($notes as $note)
                <div class="mt-4 text-gray-100 bg-gray-700 p-4 rounded-md hover:scale-105 transition-all duration-500">
                    <p class="text-center font-bold text-2xl">"{{ $note->title }}"</p>
                    <div class="border-t border-gray-400 my-3"></div>
                    <p>{{ $note->message }}</p>
                    <div class="border-t border-gray-400 my-3"></div>
                    <p class="text-right text-sm italic">{{ $note->created_at->format('F j, Y') }}</p>
                    <div class="mt-2 flex gap-2 text-center">
                        <a href="" class="w-[50%] bg-red-700 py-1 rounded">
                            Delete
                        </a>
                         <a href="{{ route('notes.edit', $note )}}" class="w-[50%] bg-blue-700 py-1 rounded">
                            Edit
                        </a>
                    </div>
                </div>
            @endforeach
        </div>
        
        <a href="{{ route('notes.create') }}">
            <button class="text-gray-50 text-xl bg-blue-700 px-4 py-2 rounded-md fixed bottom-[50px] hover:scale-105 transition-all duration-500 right-[50px] shadow-md md:left-[10vw] md:right-auto">
                + Add new note
            </button>
        </a>

    </div>
</x-app-layout>