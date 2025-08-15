<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use Inertia\Inertia;

class PostController extends Controller
{
    // List all posts
    public function index()
    {
        $posts = \App\Models\Post::latest()->get();
        return Inertia::render('posts/Index', [
            'posts' => $posts
        ]);
    }

    // Show single post
    public function show($id)
    {
        $post = \App\Models\Post::findOrFail($id);
        return Inertia::render('posts/Show', [
            'post' => $post
        ]);
    }

    // Show create form
    public function create()
    {
    return Inertia::render('posts/Create');
    }

    // Store new post
    public function store(Request $request)
    {
        $data = $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'required|string',
        ]);
        $data['author_id'] = auth()->id() ?? 1; // fallback for demo
        $post = \App\Models\Post::create($data);
        return redirect()->route('posts.show', $post->id);
    }

    // Show edit form
    public function edit($id)
    {
        $post = \App\Models\Post::findOrFail($id);
        return Inertia::render('posts/Edit', [
            'post' => $post
        ]);
    }

    // Update post
    public function update(Request $request, $id)
    {
        $post = \App\Models\Post::findOrFail($id);
        $data = $request->validate([
            'title' => 'required|string|max:255',
            'content' => 'required|string',
        ]);
        $post->update($data);
        return redirect()->route('posts.show', $post->id);
    }

    // Delete post
    public function destroy($id)
    {
        $post = \App\Models\Post::findOrFail($id);
        $post->delete();
        return redirect()->route('posts.index');
    }
}
