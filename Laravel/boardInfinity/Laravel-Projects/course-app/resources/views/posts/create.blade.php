<h1>Create New Post</h1>
<form method="POST" action="{{ route('posts.store') }}">
    @csrf
    <label>Title:</label>
    <input type="text" name="title" required>
    <br>
    <label>Content:</label>
    <textarea name="content" required></textarea>
    <br>
    <button type="submit">Create</button>
</form>
<a href="{{ route('posts.index') }}">Back to Posts</a>
