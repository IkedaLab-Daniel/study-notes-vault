/**
 * Post Service
 * All post-related API calls
 */

import axiosInstance from '../api/axiosInstance';
import { API_CONFIG } from '../config/api.config';

export const postService = {
  /**
   * Get all posts
   * @param {Object} params - Query parameters (e.g., { userId: 1 })
   * @returns {Promise} Array of posts
   */
  getAllPosts: async (params = {}) => {
    const response = await axiosInstance.get(API_CONFIG.ENDPOINTS.POSTS, { params });
    return response.data;
  },

  /**
   * Get post by ID
   * @param {number} id - Post ID
   * @returns {Promise} Post object
   */
  getPostById: async (id) => {
    const response = await axiosInstance.get(`${API_CONFIG.ENDPOINTS.POSTS}/${id}`);
    return response.data;
  },

  /**
   * Get comments for a post
   * @param {number} postId - Post ID
   * @returns {Promise} Array of comments
   */
  getPostComments: async (postId) => {
    const response = await axiosInstance.get(`${API_CONFIG.ENDPOINTS.POSTS}/${postId}/comments`);
    return response.data;
  },

  /**
   * Create new post
   * @param {Object} postData - Post data
   * @returns {Promise} Created post object
   */
  createPost: async (postData) => {
    const response = await axiosInstance.post(API_CONFIG.ENDPOINTS.POSTS, postData);
    return response.data;
  },

  /**
   * Update post
   * @param {number} id - Post ID
   * @param {Object} postData - Updated post data
   * @returns {Promise} Updated post object
   */
  updatePost: async (id, postData) => {
    const response = await axiosInstance.put(`${API_CONFIG.ENDPOINTS.POSTS}/${id}`, postData);
    return response.data;
  },

  /**
   * Delete post
   * @param {number} id - Post ID
   * @returns {Promise} Response
   */
  deletePost: async (id) => {
    const response = await axiosInstance.delete(`${API_CONFIG.ENDPOINTS.POSTS}/${id}`);
    return response.data;
  },
};
