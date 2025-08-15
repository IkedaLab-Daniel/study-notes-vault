import React from 'react';

const theme = {
  bg: '#f8fafc',
  card: '#fff',
  border: '#e2e8f0',
  accent: '#6366f1',
  accentHover: '#4338ca',
  text: '#1e293b',
  muted: '#64748b',
  danger: '#ef4444',
  success: '#059669',
};

export default function Show({ post }: { post: any }) {
  return (
    <div style={{ background: theme.bg, minHeight: '100vh', padding: '2rem 0' }}>
      <div style={{ maxWidth: 600, margin: '2rem auto', padding: 24, background: theme.card, border: `1px solid ${theme.border}`, borderRadius: 12, boxShadow: '0 2px 8px #e2e8f0' }}>
        <h1 style={{ textAlign: 'center', color: theme.accent, fontWeight: 700, fontSize: '2em', marginBottom: 24 }}>{post.title}</h1>
        <p style={{ margin: '1em 0', fontSize: '1.1em', color: theme.text }}>{post.content}</p>
        <div style={{ color: theme.muted, marginBottom: 16 }}>Author ID: {post.author_id}</div>
        <div style={{ textAlign: 'center', marginBottom: 16 }}>
          <a href={`/posts/${post.id}/edit`} style={{ background: theme.success, color: 'white', padding: '10px 20px', borderRadius: 6, textDecoration: 'none', fontWeight: 600, marginRight: 8 }}>Edit</a>
          <form method="POST" action={`/posts/${post.id}`} style={{ display: 'inline' }}>
            <input type="hidden" name="_method" value="DELETE" />
            <button type="submit" style={{ background: theme.danger, color: 'white', padding: '10px 20px', borderRadius: 6, border: 'none', fontWeight: 600, cursor: 'pointer' }}>Delete</button>
          </form>
        </div>
        <div style={{ textAlign: 'center' }}>
          <a href="/posts" style={{ color: theme.accent, textDecoration: 'underline', fontWeight: 600 }}>← Back to Posts</a>
        </div>
      </div>
    </div>
  );
}
