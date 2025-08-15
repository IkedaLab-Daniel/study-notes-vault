import { Inertia } from '@inertiajs/inertia';
import React from 'react';

const theme = {
  bg: '#f8fafc',
  card: '#fff',
  border: '#e2e8f0',
  accent: '#6366f1',
  accentHover: '#4338ca',
  text: '#1e293b',
  muted: '#64748b',
};

export default function Index({ posts }: { posts: any[] }) {
  return (
    <div style={{ background: theme.bg, minHeight: '100vh', padding: '2rem 0' }}>
      <div style={{ maxWidth: 600, margin: '2rem auto', padding: 24, background: theme.card, border: `1px solid ${theme.border}`, borderRadius: 12, boxShadow: '0 2px 8px #e2e8f0' }}>
        <h1 style={{ textAlign: 'center', color: theme.accent, fontWeight: 700, fontSize: '2em', marginBottom: 24 }}>📚 All Blog Posts</h1>
        <div style={{ textAlign: 'center', marginBottom: 24 }}>
          <a href="/posts/create" style={{ background: theme.accent, color: 'white', padding: '10px 20px', borderRadius: 6, textDecoration: 'none', fontWeight: 600, boxShadow: '0 1px 4px #e2e8f0' }}>+ Create New Post</a>
        </div>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {posts.length === 0 && <li style={{ color: theme.muted }}>No posts yet.</li>}
          {posts.map(post => (
            <li key={post.id} style={{ marginBottom: 16, padding: 16, background: theme.bg, border: `1px solid ${theme.border}`, borderRadius: 8, boxShadow: '0 1px 4px #e2e8f0' }}>
              <a href={`/posts/${post.id}`} style={{ fontSize: '1.1em', color: theme.accent, textDecoration: 'underline', fontWeight: 600 }}>{post.title}</a>
              <div style={{ fontSize: '0.95em', color: theme.muted, marginTop: 4 }}>Author ID: {post.author_id}</div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
