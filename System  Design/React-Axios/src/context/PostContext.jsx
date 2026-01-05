/**
 * Post Context
 * Global state management for posts
 * Demonstrates caching and state synchronization
 */

import { createContext, useContext, useState, useCallback, useMemo } from 'react';
import { postService } from '../services/postService';

const PostContext = createContext(undefined);

export const PostProvider = ({ children }) => {
  const [posts, setPosts] = useState([]);
  const [selectedPost, setSelectedPost] = useState(null);
  const [filters, setFilters] = useState({ userId: null, search: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch all posts
  const fetchPosts = useCallback(async (params = {}) => {
    try {
      setLoading(true);
      setError(null);
      const data = await postService.getAllPosts(params);
      setPosts(data);
      return data;
    } catch (err) {
      setError(err.message || 'Failed to fetch posts');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  // Fetch single post
  const fetchPostById = useCallback(async (id) => {
    try {
      setLoading(true);
      setError(null);
      const data = await postService.getPostById(id);
      setSelectedPost(data);
      return data;
    } catch (err) {
      setError(err.message || 'Failed to fetch post');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  // Create post
  const createPost = useCallback(async (postData) => {
    try {
      setLoading(true);
      setError(null);
      const newPost = await postService.createPost(postData);
      
      // Add to local state
      setPosts(prev => [newPost, ...prev]);
      return newPost;
    } catch (err) {
      setError(err.message || 'Failed to create post');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  // Update post
  const updatePost = useCallback(async (id, postData) => {
    try {
      setLoading(true);
      setError(null);
      const updatedPost = await postService.updatePost(id, postData);
      
      // Update in local state
      setPosts(prev => 
        prev.map(post => post.id === id ? updatedPost : post)
      );
      
      if (selectedPost?.id === id) {
        setSelectedPost(updatedPost);
      }
      
      return updatedPost;
    } catch (err) {
      setError(err.message || 'Failed to update post');
      throw err;
    } finally {
      setLoading(false);
    }
  }, [selectedPost]);

  // Delete post
  const deletePost = useCallback(async (id) => {
    try {
      setLoading(true);
      setError(null);
      await postService.deletePost(id);
      
      // Remove from local state
      setPosts(prev => prev.filter(post => post.id !== id));
      
      if (selectedPost?.id === id) {
        setSelectedPost(null);
      }
    } catch (err) {
      setError(err.message || 'Failed to delete post');
      throw err;
    } finally {
      setLoading(false);
    }
  }, [selectedPost]);

  // Set filters
  const setUserFilter = useCallback((userId) => {
    setFilters(prev => ({ ...prev, userId }));
  }, []);

  const setSearchFilter = useCallback((search) => {
    setFilters(prev => ({ ...prev, search }));
  }, []);

  // Filtered posts (computed)
  const filteredPosts = useMemo(() => {
    let result = posts;
    
    if (filters.userId) {
      result = result.filter(post => post.userId === parseInt(filters.userId));
    }
    
    if (filters.search) {
      const searchLower = filters.search.toLowerCase();
      result = result.filter(post => 
        post.title.toLowerCase().includes(searchLower) ||
        post.body.toLowerCase().includes(searchLower)
      );
    }
    
    return result;
  }, [posts, filters]);

  const value = {
    // State
    posts,
    filteredPosts,
    selectedPost,
    filters,
    loading,
    error,
    
    // Actions
    fetchPosts,
    fetchPostById,
    createPost,
    updatePost,
    deletePost,
    setUserFilter,
    setSearchFilter,
    setSelectedPost,
  };

  return (
    <PostContext.Provider value={value}>
      {children}
    </PostContext.Provider>
  );
};

// Custom hook to use the context
export const usePostContext = () => {
  const context = useContext(PostContext);
  
  if (context === undefined) {
    throw new Error('usePostContext must be used within a PostProvider');
  }
  
  return context;
};
