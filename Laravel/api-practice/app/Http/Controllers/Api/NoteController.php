<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Note;
use Illuminate\Http\Request;

use function PHPUnit\Framework\returnSelf;

class NoteController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        // > See all notes
        $notes = Note::all();
        return response()->json($notes);
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        // > create new note
        $validated = $request->validate([
            'title' => 'required',
            'message' => 'required'
        ]);

        $note = Note::create($validated);

        return response()->json($note);

    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        $note = Note::findOrFail($id);

        return response()->json($note);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        // > update a note
        $note = Note::findOrFail($id);

        $note->update($request->all());

        return response()->json($note);
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
