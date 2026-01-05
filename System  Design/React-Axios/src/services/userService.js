/**
 * User Service
 * All user-related API calls
 */

import axiosInstance from '../api/axiosInstance';
import { API_CONFIG } from '../config/api.config';

export const userService = {
  /**
   * Get all users
   * @returns {Promise} Array of users
   */
  getAllUsers: async () => {
    const response = await axiosInstance.get(API_CONFIG.ENDPOINTS.USERS);
    return response.data;
  },

  /**
   * Get user by ID
   * @param {number} id - User ID
   * @returns {Promise} User object
   */
  getUserById: async (id) => {
    const response = await axiosInstance.get(`${API_CONFIG.ENDPOINTS.USERS}/${id}`);
    return response.data;
  },

  /**
   * Create new user
   * @param {Object} userData - User data
   * @returns {Promise} Created user object
   */
  createUser: async (userData) => {
    const response = await axiosInstance.post(API_CONFIG.ENDPOINTS.USERS, userData);
    return response.data;
  },

  /**
   * Update user
   * @param {number} id - User ID
   * @param {Object} userData - Updated user data
   * @returns {Promise} Updated user object
   */
  updateUser: async (id, userData) => {
    const response = await axiosInstance.put(`${API_CONFIG.ENDPOINTS.USERS}/${id}`, userData);
    return response.data;
  },

  /**
   * Delete user
   * @param {number} id - User ID
   * @returns {Promise} Response
   */
  deleteUser: async (id) => {
    const response = await axiosInstance.delete(`${API_CONFIG.ENDPOINTS.USERS}/${id}`);
    return response.data;
  },
};
