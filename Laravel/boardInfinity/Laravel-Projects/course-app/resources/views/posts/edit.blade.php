<h1>Edit Post</h1>
<form method="POST" action="{{ route('posts.update', $post->id) }}">
    @csrf
    @method('PUT')
    <label>Title:</label>
    <input type="text" name="title" value="{{ $post->title }}" required>
    <br>
    <label>Content:</label>
    <textarea name="content" required>{{ $post->content }}</textarea>
    <br>
    <button type="submit">Update</button>
</form>
<a href="{{ route('posts.show', $post->id) }}">Back to Post</a>
