/**
 * PostList Component
 * Displays posts with filtering by user
 * Demonstrates parameterized API calls and state management
 */

import { useState } from 'react';
import { usePosts } from '../hooks/usePosts';
import { useUsers } from '../hooks/useUsers';
import PostDetail from './PostDetail';
import './PostList.css';

const PostList = () => {
  const [selectedUserId, setSelectedUserId] = useState('');
  const [selectedPostId, setSelectedPostId] = useState(null);
  
  const { users } = useUsers();
  const { posts, loading, error, refetch } = usePosts(
    selectedUserId ? { userId: selectedUserId } : {}
  );

  if (loading) {
    return (
      <div className="post-list-container">
        <div className="loading">
          <div className="spinner"></div>
          <p>Loading posts...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="post-list-container">
        <div className="error">
          <h3>❌ Error</h3>
          <p>{error}</p>
          <button onClick={refetch} className="retry-button">
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="post-list-container">
      <div className="header">
        <h2>Posts ({posts?.length || 0})</h2>
        <div className="controls">
          <select
            value={selectedUserId}
            onChange={(e) => setSelectedUserId(e.target.value)}
            className="user-filter"
          >
            <option value="">All Users</option>
            {users?.map((user) => (
              <option key={user.id} value={user.id}>
                {user.name}
              </option>
            ))}
          </select>
          <button onClick={refetch} className="refresh-button">
            🔄 Refresh
          </button>
        </div>
      </div>

      <div className="posts-grid">
        {posts?.map((post) => (
          <div 
            key={post.id} 
            className="post-card"
            onClick={() => setSelectedPostId(post.id)}
          >
            <div className="post-header">
              <span className="post-id">#{post.id}</span>
              <span className="user-badge">User {post.userId}</span>
            </div>
            <h3 className="post-title">{post.title}</h3>
            <p className="post-body">{post.body}</p>
            <button className="view-details-btn">
              View Details →
            </button>
          </div>
        ))}
      </div>

      {selectedPostId && (
        <PostDetail 
          postId={selectedPostId} 
          onClose={() => setSelectedPostId(null)} 
        />
      )}
    </div>
  );
};

export default PostList;
