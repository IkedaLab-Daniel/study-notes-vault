import React, { useState } from 'react';
import { Inertia } from '@inertiajs/inertia';
import { usePage } from '@inertiajs/react';

const theme = {
  bg: '#f8fafc',
  card: '#fff',
  border: '#e2e8f0',
  accent: '#6366f1',
  accentHover: '#4338ca',
  text: '#1e293b',
  muted: '#64748b',
  success: '#059669',
};

export default function Edit({ post }: { post: any }) {
  const [title, setTitle] = useState(post.title);
  const [content, setContent] = useState(post.content);
  const { errors } = usePage().props as { errors?: Record<string, string> };

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    Inertia.put(`/posts/${post.id}`, { title, content });
  }

  return (
    <div style={{ background: theme.bg, minHeight: '100vh', padding: '2rem 0' }}>
      <div style={{ maxWidth: 500, margin: '2rem auto', padding: 24, background: theme.card, border: `1px solid ${theme.border}`, borderRadius: 12, boxShadow: '0 2px 8px #e2e8f0' }}>
        <h1 style={{ textAlign: 'center', color: theme.success, fontWeight: 700, fontSize: '2em', marginBottom: 24 }}>✏️ Edit Post</h1>
        <form onSubmit={handleSubmit}>
          <div style={{ marginBottom: 16 }}>
            <label style={{ fontWeight: 'bold', color: theme.text }}>Title:</label><br />
            <input
              value={title}
              onChange={e => setTitle(e.target.value)}
              required
              style={{ width: '100%', padding: 10, borderRadius: 6, border: `1px solid ${theme.border}`, fontSize: '1em' }}
            />
            {errors?.title && <div style={{ color: '#ef4444', marginTop: 4 }}>{errors.title}</div>}
          </div>
          <div style={{ marginBottom: 16 }}>
            <label style={{ fontWeight: 'bold', color: theme.text }}>Content:</label><br />
            <textarea
              value={content}
              onChange={e => setContent(e.target.value)}
              required
              style={{ width: '100%', minHeight: 120, padding: 10, borderRadius: 6, border: `1px solid ${theme.border}`, fontSize: '1em' }}
            />
            {errors?.content && <div style={{ color: '#ef4444', marginTop: 4 }}>{errors.content}</div>}
          </div>
          <button type="submit" style={{ background: theme.success, color: 'white', padding: '10px 20px', border: 'none', borderRadius: 6, cursor: 'pointer', fontWeight: 600 }}>Update</button>
        </form>
        <div style={{ marginTop: 24, textAlign: 'center' }}>
          <a href={`/posts/${post.id}`} style={{ color: theme.accent, textDecoration: 'underline', fontWeight: 600 }}>← Back to Post</a>
        </div>
      </div>
    </div>
  );
}
