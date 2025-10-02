<x-app-layout>
    <body>
        <div class="p-6">
            @if (count($notes) == 0)
                <div>
                    <!-- SVG DITO MAMAYA -->
                    <h2>No notes Yet</h2>
                </div>
            @else
                <div class="flex justify-between items-center">
                    <span class="text-slate-200 text-4xl font-bold">My notes:</span>
                    <div>
                        <a href="" class="text-slate-50 bg-blue-700 py-2 px-4 rounded">
                            Add Note
                        </a>
                    </div>
                </div>
                <div class="mt-4 md:p-4 grid grid-cols-1 md:grid-cols-4 gap-4">
                    @foreach($notes as $note)
                        <div class="p-4 text-slate-200 bg-slate-700 rounded-md">
                            <p class="text-center text-xl font-semibold">"{{$note->title}}"</p>
                            <div class="mt-2 border-t border-slate-400"></div>
                            <p class="mt-3 text-sm text-slate-400">Message:</p>
                            <p>{{$note->message}}</p>
                        </div>        
                    @endforeach
                </div>
                
            @endif
        
        </div>        
    </body>
</x-app-layout>