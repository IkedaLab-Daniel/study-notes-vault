<x-app-layout>
    <div class="p-3 md:p-0">
        <div class="h-full text-gray-50 bg-gray-700 md:w-[800px] md:p-4 p-2 mx-auto mt-[50px] rounded-xl shadow-lg">
            <h1 class="text-3xl font-semibold text-center my-4">Create a new note</h1>
            <form 
                action="{{ route('notes.store') }}"
                method="POST" 
                class= "bg-gray-700 flex flex-col gap-2 px-4"
            >
                @csrf
                <label class="text-xl" for="title">Title:</label>
                <input placeholder="Title" class="bg-gray-600 w-[100%] rounded-md" type="text" name="title">
                <label class="text-xl" for="message">Message:</label>
                <textarea placeholder="Message" class="bg-gray-600 w-[100%] rounded-md" rows="6" name="message" id="message"></textarea>
                <div class="mt-4 flex gap-4 ">
                    <a href="{{ route('notes.index') }}" class="bg-gray-800 py-2 text-xl text-center w-[50%] hover:scale-105 transition-all duration-500 shadow-lg">
                        Back
                    </a>
                    <button class="bg-blue-700 py-2 text-xl w-[50%] hover:scale-105 transition-all duration-500 shadow-lg">Submit</button>
                </div>
            </form>
        </div>
    </div>
</x-app-layout>