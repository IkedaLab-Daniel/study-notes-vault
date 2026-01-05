/**
 * usePosts Hook
 * Specialized hook for post-related operations
 */

import { useState, useCallback } from 'react';
import { postService } from '../services/postService';
import { useFetch } from './useFetch';

export const usePosts = (params = {}) => {
  // Fetch all posts with optional parameters
  const { data: posts, loading, error, refetch } = useFetch(
    () => postService.getAllPosts(params),
    [JSON.stringify(params)], // Dependency on params
    true
  );

  return {
    posts,
    loading,
    error,
    refetch,
  };
};

export const usePost = (postId) => {
  // Fetch single post by ID
  const { data: post, loading, error, refetch } = useFetch(
    () => postService.getPostById(postId),
    [postId],
    !!postId // Only fetch if postId exists
  );

  return {
    post,
    loading,
    error,
    refetch,
  };
};

export const usePostComments = (postId) => {
  // Fetch comments for a specific post
  const { data: comments, loading, error, refetch } = useFetch(
    () => postService.getPostComments(postId),
    [postId],
    !!postId
  );

  return {
    comments,
    loading,
    error,
    refetch,
  };
};

export const usePostMutations = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const createPost = useCallback(async (postData) => {
    try {
      setLoading(true);
      setError(null);
      const result = await postService.createPost(postData);
      return result;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const updatePost = useCallback(async (id, postData) => {
    try {
      setLoading(true);
      setError(null);
      const result = await postService.updatePost(id, postData);
      return result;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const deletePost = useCallback(async (id) => {
    try {
      setLoading(true);
      setError(null);
      const result = await postService.deletePost(id);
      return result;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  return {
    createPost,
    updatePost,
    deletePost,
    loading,
    error,
  };
};
