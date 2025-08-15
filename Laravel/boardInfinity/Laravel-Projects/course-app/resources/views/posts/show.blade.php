<h1>{{ $post->title }}</h1>
<p>{{ $post->content }}</p>
<p>Author ID: {{ $post->author_id }}</p>
<a href="{{ route('posts.edit', $post->id) }}">Edit</a>
<form method="POST" action="{{ route('posts.destroy', $post->id) }}">
    @csrf
    @method('DELETE')
    <button type="submit">Delete</button>
</form>
<a href="{{ route('posts.index') }}">Back to Posts</a>
