/**
 * PostListContext Component
 * Uses Context API with computed filtered data
 * Demonstrates state synchronization across components
 */

import { useEffect } from 'react';
import { usePostContext } from '../context/PostContext';
import { useUserContext } from '../context/UserContext';
import { useAppContext } from '../context/AppContext';
import './PostList.css';

const PostListContext = () => {
  const { 
    filteredPosts, 
    filters,
    loading, 
    error, 
    fetchPosts,
    setUserFilter,
    setSearchFilter 
  } = usePostContext();
  
  const { users } = useUserContext();
  const { addNotification } = useAppContext();

  // Fetch posts on mount
  useEffect(() => {
    if (!filteredPosts.length) {
      fetchPosts();
    }
  }, []);

  const handleRefresh = async () => {
    try {
      await fetchPosts();
      addNotification('Posts refreshed!', 'success');
    } catch (err) {
      addNotification('Failed to refresh posts', 'error');
    }
  };

  if (loading) {
    return (
      <div className="post-list-container">
        <div className="loading">
          <div className="spinner"></div>
          <p>Loading posts from Context...</p>
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
          <button onClick={handleRefresh} className="retry-button">
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="post-list-container">
      <div className="header">
        <div>
          <h2>Posts - Context API ({filteredPosts?.length || 0})</h2>
          <p style={{ fontSize: '12px', color: '#666', margin: '5px 0 0 0' }}>
            Using global state with computed filters
          </p>
        </div>
        <div className="controls">
          <select
            value={filters.userId || ''}
            onChange={(e) => setUserFilter(e.target.value)}
            className="user-filter"
          >
            <option value="">All Users</option>
            {users?.map((user) => (
              <option key={user.id} value={user.id}>
                {user.name}
              </option>
            ))}
          </select>
          
          <input
            type="text"
            placeholder="Search posts..."
            value={filters.search}
            onChange={(e) => setSearchFilter(e.target.value)}
            className="user-filter"
            style={{ minWidth: '200px' }}
          />
          
          <button onClick={handleRefresh} className="refresh-button">
            🔄 Refresh
          </button>
        </div>
      </div>

      <div className="posts-grid">
        {filteredPosts?.map((post) => (
          <div key={post.id} className="post-card">
            <div className="post-header">
              <span className="post-id">#{post.id}</span>
              <span className="user-badge">User {post.userId}</span>
            </div>
            <h3 className="post-title">{post.title}</h3>
            <p className="post-body">{post.body}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PostListContext;
