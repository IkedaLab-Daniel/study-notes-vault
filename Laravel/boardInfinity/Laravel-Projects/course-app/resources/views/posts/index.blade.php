<h1>All Blog Posts</h1>
<a href="{{ route('posts.create') }}">Create New Post</a>
<ul>
@foreach($posts as $post)
    <li>
        <a href="{{ route('posts.show', $post->id) }}">{{ $post->title }}</a>
    </li>
@endforeach
</ul>
