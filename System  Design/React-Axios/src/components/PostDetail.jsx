/**
 * PostDetail Component (Modal)
 * Shows post details with comments
 * Demonstrates nested data fetching
 */

import { usePost, usePostComments } from '../hooks/usePosts';
import './PostDetail.css';

const PostDetail = ({ postId, onClose }) => {
  const { post, loading: postLoading } = usePost(postId);
  const { comments, loading: commentsLoading } = usePostComments(postId);

  const handleBackdropClick = (e) => {
    if (e.target.className === 'modal-backdrop') {
      onClose();
    }
  };

  return (
    <div className="modal-backdrop" onClick={handleBackdropClick}>
      <div className="modal-content">
        <div className="modal-header">
          <h2>Post Details</h2>
          <button className="close-button" onClick={onClose}>
            ✕
          </button>
        </div>

        {postLoading ? (
          <div className="loading">
            <div className="spinner"></div>
            <p>Loading post...</p>
          </div>
        ) : (
          <>
            <div className="post-detail">
              <div className="post-meta">
                <span className="post-id">#{post?.id}</span>
                <span className="user-badge">User {post?.userId}</span>
              </div>
              <h3>{post?.title}</h3>
              <p>{post?.body}</p>
            </div>

            <div className="comments-section">
              <h3>Comments ({comments?.length || 0})</h3>
              
              {commentsLoading ? (
                <div className="loading-comments">
                  <div className="spinner-small"></div>
                  <p>Loading comments...</p>
                </div>
              ) : (
                <div className="comments-list">
                  {comments?.map((comment) => (
                    <div key={comment.id} className="comment-card">
                      <div className="comment-header">
                        <strong>{comment.name}</strong>
                        <span className="comment-email">{comment.email}</span>
                      </div>
                      <p className="comment-body">{comment.body}</p>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default PostDetail;
