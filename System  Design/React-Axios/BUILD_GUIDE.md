# React + Axios System Build Guide

A comprehensive guide to building a production-ready React application with Axios, featuring dual state management patterns (Custom Hooks + Context API), proper error handling, and modular architecture.

## Table of Contents

1. [System Overview](#system-overview)
2. [Prerequisites](#prerequisites)
3. [Project Initialization](#project-initialization)
4. [Architecture Overview](#architecture-overview)
5. [Step-by-Step Build Guide](#step-by-step-build-guide)
6. [Testing & Development](#testing--development)
7. [Best Practices](#best-practices)

---

## System Overview

This system demonstrates a well-architected React application with:

- **Dual State Management**: Both local hooks and Context API patterns
- **Axios Integration**: Centralized HTTP client with interceptors
- **Modular Architecture**: Services, hooks, contexts, and components separation
- **Error Handling**: Comprehensive error states and user feedback
- **Type Safety**: JSDoc documentation for better DX
- **Modern React**: Using React 19 features

**Tech Stack:**
- React 19
- Axios 1.13+
- Vite 7
- ES6 Modules

---

## Prerequisites

Before starting, ensure you have:

```bash
# Node.js (v18 or higher recommended)
node --version  # Should be >= 18.0.0

# npm or yarn
npm --version   # Should be >= 9.0.0
```

---

## Project Initialization

### Step 1: Create Vite Project

```bash
# Create new Vite project with React template
npm create vite@latest react-axios -- --template react

# Navigate to project directory
cd react-axios

# Install dependencies
npm install

# Install Axios
npm install axios
```

### Step 2: Project Structure Setup

Create the following directory structure:

```
src/
├── api/                # Axios configuration
├── config/             # App configuration
├── context/            # React Context providers
├── hooks/              # Custom React hooks
├── services/           # API service layer
├── components/         # React components
└── assets/             # Static assets
```

```bash
# Create directories
mkdir -p src/{api,config,context,hooks,services,components,assets}
```

---

## Architecture Overview

### Layer Architecture

```
┌─────────────────────────────────────────┐
│         Components Layer                │
│  (UI, user interactions)                │
└───────────────┬─────────────────────────┘
                │
    ┌───────────┴──────────────┐
    │                          │
┌───▼─────────┐      ┌────────▼───────┐
│   Hooks     │      │   Context API  │
│  (Local)    │      │   (Global)     │
└───────┬─────┘      └────────┬───────┘
        │                     │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │   Services Layer    │
        │  (Business Logic)   │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │   Axios Instance    │
        │  (HTTP Client)      │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │      API/Backend    │
        └─────────────────────┘
```

---

## Step-by-Step Build Guide

### Phase 1: Configuration Layer

#### 1.1 API Configuration (`src/config/api.config.js`)

Create centralized configuration for all API settings:

```javascript
/**
 * API Configuration
 * Centralized configuration for API endpoints and settings
 */

export const API_CONFIG = {
  // Base URL - change based on environment
  BASE_URL: import.meta.env.VITE_API_BASE_URL || 'https://jsonplaceholder.typicode.com',
  
  // Timeout in milliseconds
  TIMEOUT: 10000,
  
  // Common headers
  HEADERS: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
  
  // API endpoints
  ENDPOINTS: {
    USERS: '/users',
    POSTS: '/posts',
    COMMENTS: '/comments',
    TODOS: '/todos',
  },
};

// Environment-specific configurations
export const ENV = {
  isDevelopment: import.meta.env.MODE === 'development',
  isProduction: import.meta.env.MODE === 'production',
};
```

**Key Concepts:**
- ✅ Single source of truth for API configuration
- ✅ Environment-based configuration using Vite's `import.meta.env`
- ✅ Easy to modify endpoints without touching code

---

### Phase 2: HTTP Client Layer

#### 2.1 Axios Instance (`src/api/axiosInstance.js`)

Create a configured Axios instance with interceptors:

```javascript
/**
 * Axios Instance Configuration
 * Centralized Axios instance with interceptors for request/response handling
 */

import axios from 'axios';
import { API_CONFIG, ENV } from '../config/api.config';

// Create axios instance with default config
const axiosInstance = axios.create({
  baseURL: API_CONFIG.BASE_URL,
  timeout: API_CONFIG.TIMEOUT,
  headers: API_CONFIG.HEADERS,
});

// Request interceptor
axiosInstance.interceptors.request.use(
  (config) => {
    // Add authentication token if available
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    
    // Log requests in development
    if (ENV.isDevelopment) {
      console.log('🚀 Request:', config.method.toUpperCase(), config.url);
    }
    
    return config;
  },
  (error) => {
    if (ENV.isDevelopment) {
      console.error('❌ Request Error:', error);
    }
    return Promise.reject(error);
  }
);

// Response interceptor
axiosInstance.interceptors.response.use(
  (response) => {
    // Log successful responses in development
    if (ENV.isDevelopment) {
      console.log('✅ Response:', response.config.url, response.status);
    }
    return response;
  },
  (error) => {
    // Handle errors globally
    if (error.response) {
      // Server responded with error status
      const { status, data } = error.response;
      
      switch (status) {
        case 401:
          // Unauthorized - clear token and redirect to login
          localStorage.removeItem('authToken');
          console.error('Unauthorized access - token may be invalid');
          break;
        case 403:
          console.error('Forbidden - insufficient permissions');
          break;
        case 404:
          console.error('Resource not found');
          break;
        case 500:
          console.error('Server error - please try again later');
          break;
        default:
          console.error(`Error ${status}:`, data?.message || 'Unknown error');
      }
    } else if (error.request) {
      // Request made but no response received
      console.error('Network error - no response from server');
    } else {
      // Error in request configuration
      console.error('Request configuration error:', error.message);
    }
    
    return Promise.reject(error);
  }
);

export default axiosInstance;
```

**Key Concepts:**
- ✅ **Request Interceptor**: Automatically adds auth tokens, logs requests
- ✅ **Response Interceptor**: Global error handling, logging
- ✅ **Centralized Configuration**: One place to modify all requests
- ✅ **Error Handling**: Consistent error handling across the app

---

### Phase 3: Service Layer

#### 3.1 User Service (`src/services/userService.js`)

Create service layer that abstracts API calls:

```javascript
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
```

#### 3.2 Post Service (`src/services/postService.js`)

```javascript
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
```

**Key Concepts:**
- ✅ **Separation of Concerns**: Business logic separated from components
- ✅ **Reusability**: Services can be used in hooks OR contexts
- ✅ **Documentation**: JSDoc for better IDE support
- ✅ **Consistency**: All API calls follow the same pattern

---

### Phase 4: Custom Hooks (Local State Pattern)

#### 4.1 Generic useFetch Hook (`src/hooks/useFetch.js`)

Create a reusable hook for data fetching:

```javascript
/**
 * useFetch Hook
 * Generic hook for data fetching with proper state management
 * Handles loading, error, and data states
 */

import { useState, useEffect, useCallback } from 'react';

/**
 * @param {Function} fetchFunction - Async function to fetch data
 * @param {Array} dependencies - Dependencies to trigger refetch
 * @param {boolean} immediate - Whether to fetch immediately on mount
 * @returns {Object} { data, loading, error, refetch }
 */
export const useFetch = (fetchFunction, dependencies = [], immediate = true) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(immediate);
  const [error, setError] = useState(null);

  const executeFetch = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const result = await fetchFunction();
      setData(result);
      return result;
    } catch (err) {
      setError(err.message || 'An error occurred');
      console.error('Fetch error:', err);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [fetchFunction]);

  useEffect(() => {
    if (immediate) {
      executeFetch();
    }
  }, [...dependencies, immediate]);

  // Refetch function for manual refetching
  const refetch = useCallback(() => {
    return executeFetch();
  }, [executeFetch]);

  return { data, loading, error, refetch };
};
```

#### 4.2 Generic useApi Hook (`src/hooks/useApi.js`)

Create a hook for API mutations with advanced features:

```javascript
/**
 * useApi Hook
 * Advanced hook for API calls with loading, error handling, and optimistic updates
 */

import { useState, useCallback } from 'react';

/**
 * @returns {Object} { execute, loading, error, data, reset }
 */
export const useApi = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  /**
   * Execute API call
   * @param {Function} apiFunction - Async API function
   * @param {Object} options - Options (onSuccess, onError, optimisticData)
   */
  const execute = useCallback(async (apiFunction, options = {}) => {
    const { onSuccess, onError, optimisticData } = options;

    try {
      setLoading(true);
      setError(null);

      // Optimistic update
      if (optimisticData) {
        setData(optimisticData);
      }

      const result = await apiFunction();
      setData(result);

      // Success callback
      if (onSuccess) {
        onSuccess(result);
      }

      return result;
    } catch (err) {
      const errorMessage = err.response?.data?.message || err.message || 'An error occurred';
      setError(errorMessage);

      // Revert optimistic update on error
      if (optimisticData) {
        setData(null);
      }

      // Error callback
      if (onError) {
        onError(err);
      }

      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  // Reset state
  const reset = useCallback(() => {
    setData(null);
    setLoading(false);
    setError(null);
  }, []);

  return { execute, loading, error, data, reset };
};
```

#### 4.3 Specialized useUsers Hook (`src/hooks/useUsers.js`)

Create domain-specific hooks:

```javascript
/**
 * useUsers Hook
 * Specialized hook for user-related operations
 */

import { useState, useCallback } from 'react';
import { userService } from '../services/userService';
import { useFetch } from './useFetch';

export const useUsers = () => {
  // Fetch all users
  const { data: users, loading, error, refetch } = useFetch(
    () => userService.getAllUsers(),
    [],
    true
  );

  return {
    users,
    loading,
    error,
    refetch,
  };
};

export const useUser = (userId) => {
  // Fetch single user by ID
  const { data: user, loading, error, refetch } = useFetch(
    () => userService.getUserById(userId),
    [userId],
    !!userId // Only fetch if userId exists
  );

  return {
    user,
    loading,
    error,
    refetch,
  };
};

export const useUserMutations = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const createUser = useCallback(async (userData) => {
    try {
      setLoading(true);
      setError(null);
      const result = await userService.createUser(userData);
      return result;
    } catch (err) {
      setError(err.message || 'Failed to create user');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const updateUser = useCallback(async (id, userData) => {
    try {
      setLoading(true);
      setError(null);
      const result = await userService.updateUser(id, userData);
      return result;
    } catch (err) {
      setError(err.message || 'Failed to update user');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const deleteUser = useCallback(async (id) => {
    try {
      setLoading(true);
      setError(null);
      await userService.deleteUser(id);
    } catch (err) {
      setError(err.message || 'Failed to delete user');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  return {
    createUser,
    updateUser,
    deleteUser,
    loading,
    error,
  };
};
```

#### 4.4 Specialized usePosts Hook (`src/hooks/usePosts.js`)

```javascript
/**
 * usePosts Hook
 * Specialized hook for post-related operations
 */

import { postService } from '../services/postService';
import { useFetch } from './useFetch';

export const usePosts = (params = {}) => {
  const { data: posts, loading, error, refetch } = useFetch(
    () => postService.getAllPosts(params),
    [JSON.stringify(params)],
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
  const { data: post, loading, error, refetch } = useFetch(
    () => postService.getPostById(postId),
    [postId],
    !!postId
  );

  return {
    post,
    loading,
    error,
    refetch,
  };
};
```

**Key Concepts:**
- ✅ **Composition**: Generic hooks composed into specialized ones
- ✅ **Separation of Queries and Mutations**: Different hooks for read/write
- ✅ **Local State**: Each component gets its own state
- ✅ **Flexibility**: Easy to customize per component

---

### Phase 5: Context API (Global State Pattern)

#### 5.1 App Context (`src/context/AppContext.jsx`)

Global app-wide state management:

```javascript
/**
 * App Context
 * Global application state management
 * Manages app-wide settings, theme, notifications, etc.
 */

import { createContext, useContext, useState, useCallback, useEffect } from 'react';

const AppContext = createContext(undefined);

export const AppProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');
  const [notifications, setNotifications] = useState([]);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [authToken, setAuthToken] = useState(null);

  // Load auth state from localStorage on mount
  useEffect(() => {
    const token = localStorage.getItem('authToken');
    if (token) {
      setAuthToken(token);
      setIsAuthenticated(true);
    }
  }, []);

  // Toggle theme
  const toggleTheme = useCallback(() => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  }, []);

  // Login
  const login = useCallback((token) => {
    localStorage.setItem('authToken', token);
    setAuthToken(token);
    setIsAuthenticated(true);
  }, []);

  // Logout
  const logout = useCallback(() => {
    localStorage.removeItem('authToken');
    setAuthToken(null);
    setIsAuthenticated(false);
  }, []);

  // Add notification
  const addNotification = useCallback((message, type = 'info') => {
    const id = Date.now();
    const notification = { id, message, type };
    
    setNotifications(prev => [...prev, notification]);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
      removeNotification(id);
    }, 5000);
    
    return id;
  }, []);

  // Remove notification
  const removeNotification = useCallback((id) => {
    setNotifications(prev => prev.filter(n => n.id !== id));
  }, []);

  const value = {
    // State
    theme,
    notifications,
    isAuthenticated,
    authToken,
    
    // Actions
    toggleTheme,
    login,
    logout,
    addNotification,
    removeNotification,
  };

  return (
    <AppContext.Provider value={value}>
      {children}
    </AppContext.Provider>
  );
};

// Custom hook to use the context
export const useAppContext = () => {
  const context = useContext(AppContext);
  
  if (context === undefined) {
    throw new Error('useAppContext must be used within an AppProvider');
  }
  
  return context;
};
```

#### 5.2 User Context (`src/context/UserContext.jsx`)

Domain-specific global state:

```javascript
/**
 * User Context
 * Global state management for user-related data
 */

import { createContext, useContext, useState, useCallback, useEffect } from 'react';
import { userService } from '../services/userService';

const UserContext = createContext(undefined);

export const UserProvider = ({ children }) => {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch all users
  const fetchUsers = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await userService.getAllUsers();
      setUsers(data);
      return data;
    } catch (err) {
      setError(err.message || 'Failed to fetch users');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  // Fetch single user
  const fetchUserById = useCallback(async (id) => {
    try {
      setLoading(true);
      setError(null);
      const data = await userService.getUserById(id);
      setSelectedUser(data);
      return data;
    } catch (err) {
      setError(err.message || 'Failed to fetch user');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  // Create user
  const createUser = useCallback(async (userData) => {
    try {
      setLoading(true);
      setError(null);
      const newUser = await userService.createUser(userData);
      
      // Optimistically update local state
      setUsers(prev => [...prev, newUser]);
      return newUser;
    } catch (err) {
      setError(err.message || 'Failed to create user');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  // Update user
  const updateUser = useCallback(async (id, userData) => {
    try {
      setLoading(true);
      setError(null);
      const updatedUser = await userService.updateUser(id, userData);
      
      // Update in local state
      setUsers(prev => 
        prev.map(user => user.id === id ? updatedUser : user)
      );
      
      if (selectedUser?.id === id) {
        setSelectedUser(updatedUser);
      }
      
      return updatedUser;
    } catch (err) {
      setError(err.message || 'Failed to update user');
      throw err;
    } finally {
      setLoading(false);
    }
  }, [selectedUser]);

  // Delete user
  const deleteUser = useCallback(async (id) => {
    try {
      setLoading(true);
      setError(null);
      await userService.deleteUser(id);
      
      // Remove from local state
      setUsers(prev => prev.filter(user => user.id !== id));
      
      if (selectedUser?.id === id) {
        setSelectedUser(null);
      }
    } catch (err) {
      setError(err.message || 'Failed to delete user');
      throw err;
    } finally {
      setLoading(false);
    }
  }, [selectedUser]);

  // Auto-fetch users on mount
  useEffect(() => {
    fetchUsers();
  }, [fetchUsers]);

  const value = {
    // State
    users,
    selectedUser,
    loading,
    error,
    
    // Actions
    fetchUsers,
    fetchUserById,
    createUser,
    updateUser,
    deleteUser,
    setSelectedUser,
  };

  return (
    <UserContext.Provider value={value}>
      {children}
    </UserContext.Provider>
  );
};

// Custom hook to use the context
export const useUserContext = () => {
  const context = useContext(UserContext);
  
  if (context === undefined) {
    throw new Error('useUserContext must be used within a UserProvider');
  }
  
  return context;
};
```

#### 5.3 Post Context (`src/context/PostContext.jsx`)

```javascript
/**
 * Post Context
 * Global state management for post-related data
 */

import { createContext, useContext, useState, useCallback } from 'react';
import { postService } from '../services/postService';

const PostContext = createContext(undefined);

export const PostProvider = ({ children }) => {
  const [posts, setPosts] = useState([]);
  const [selectedPost, setSelectedPost] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

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

  const createPost = useCallback(async (postData) => {
    try {
      setLoading(true);
      setError(null);
      const newPost = await postService.createPost(postData);
      setPosts(prev => [newPost, ...prev]);
      return newPost;
    } catch (err) {
      setError(err.message || 'Failed to create post');
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const deletePost = useCallback(async (id) => {
    try {
      setLoading(true);
      setError(null);
      await postService.deletePost(id);
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

  const value = {
    posts,
    selectedPost,
    loading,
    error,
    fetchPosts,
    fetchPostById,
    createPost,
    deletePost,
    setSelectedPost,
  };

  return (
    <PostContext.Provider value={value}>
      {children}
    </PostContext.Provider>
  );
};

export const usePostContext = () => {
  const context = useContext(PostContext);
  
  if (context === undefined) {
    throw new Error('usePostContext must be used within a PostProvider');
  }
  
  return context;
};
```

**Key Concepts:**
- ✅ **Global State**: State shared across multiple components
- ✅ **Provider Pattern**: Wrap app with providers
- ✅ **Custom Hooks**: Easy consumption with `useContext` wrapper
- ✅ **Optimistic Updates**: Update local state immediately

---

### Phase 6: Component Layer

#### 6.1 UserList Component (Hooks Pattern) (`src/components/UserList.jsx`)

Component using local hooks:

```javascript
/**
 * UserList Component
 * Displays users using local hooks pattern
 */

import { useUsers } from '../hooks/useUsers';
import './UserList.css';

const UserList = () => {
  const { users, loading, error, refetch } = useUsers();

  if (loading) {
    return (
      <div className="user-list-container">
        <div className="loading">
          <div className="spinner"></div>
          <p>Loading users...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="user-list-container">
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
    <div className="user-list-container">
      <div className="header">
        <h2>Users ({users?.length || 0})</h2>
        <button onClick={refetch} className="refresh-button">
          🔄 Refresh
        </button>
      </div>

      <div className="user-grid">
        {users?.map((user) => (
          <div key={user.id} className="user-card">
            <div className="user-avatar">
              {user.name.charAt(0).toUpperCase()}
            </div>
            <div className="user-info">
              <h3>{user.name}</h3>
              <p className="user-email">{user.email}</p>
              <p className="user-company">{user.company?.name}</p>
              <p className="user-phone">📞 {user.phone}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default UserList;
```

#### 6.2 UserListContext Component (Context Pattern) (`src/components/UserListContext.jsx`)

Component using Context API:

```javascript
/**
 * UserListContext Component
 * Displays users using Context API pattern
 */

import { useUserContext } from '../context/UserContext';
import './UserList.css';

const UserListContext = () => {
  const { users, loading, error, fetchUsers } = useUserContext();

  if (loading) {
    return (
      <div className="user-list-container">
        <div className="loading">
          <div className="spinner"></div>
          <p>Loading users...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="user-list-container">
        <div className="error">
          <h3>❌ Error</h3>
          <p>{error}</p>
          <button onClick={fetchUsers} className="retry-button">
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="user-list-container">
      <div className="header">
        <h2>Users - Context ({users?.length || 0})</h2>
        <button onClick={fetchUsers} className="refresh-button">
          🔄 Refresh
        </button>
      </div>

      <div className="user-grid">
        {users?.map((user) => (
          <div key={user.id} className="user-card">
            <div className="user-avatar">
              {user.name.charAt(0).toUpperCase()}
            </div>
            <div className="user-info">
              <h3>{user.name}</h3>
              <p className="user-email">{user.email}</p>
              <p className="user-company">{user.company?.name}</p>
              <p className="user-phone">📞 {user.phone}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default UserListContext;
```

#### 6.3 CreateUserForm Component (`src/components/CreateUserForm.jsx`)

Form with API integration:

```javascript
/**
 * CreateUserForm Component
 * Form for creating new users with validation
 */

import { useState } from 'react';
import { useApi } from '../hooks/useApi';
import { useAppContext } from '../context/AppContext';
import { userService } from '../services/userService';
import './CreateUserForm.css';

const CreateUserForm = () => {
  const { execute, loading, error } = useApi();
  const { addNotification } = useAppContext();
  
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    company: {
      name: '',
    },
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    
    if (name === 'companyName') {
      setFormData(prev => ({
        ...prev,
        company: { name: value },
      }));
    } else {
      setFormData(prev => ({
        ...prev,
        [name]: value,
      }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      await execute(
        () => userService.createUser(formData),
        {
          onSuccess: (user) => {
            addNotification(`User ${user.name} created successfully!`, 'success');
            // Reset form
            setFormData({
              name: '',
              email: '',
              phone: '',
              company: { name: '' },
            });
          },
          onError: () => {
            addNotification('Failed to create user', 'error');
          },
        }
      );
    } catch (err) {
      // Error handled by useApi
    }
  };

  return (
    <div className="create-user-container">
      <h2>Create New User</h2>
      
      <form onSubmit={handleSubmit} className="user-form">
        <div className="form-group">
          <label htmlFor="name">Name *</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
            placeholder="John Doe"
          />
        </div>

        <div className="form-group">
          <label htmlFor="email">Email *</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            placeholder="john@example.com"
          />
        </div>

        <div className="form-group">
          <label htmlFor="phone">Phone</label>
          <input
            type="tel"
            id="phone"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
            placeholder="+1-234-567-8900"
          />
        </div>

        <div className="form-group">
          <label htmlFor="companyName">Company</label>
          <input
            type="text"
            id="companyName"
            name="companyName"
            value={formData.company.name}
            onChange={handleChange}
            placeholder="Acme Inc."
          />
        </div>

        {error && (
          <div className="form-error">
            ❌ {error}
          </div>
        )}

        <button 
          type="submit" 
          className="submit-button"
          disabled={loading}
        >
          {loading ? 'Creating...' : 'Create User'}
        </button>
      </form>
    </div>
  );
};

export default CreateUserForm;
```

#### 6.4 NotificationList Component (`src/components/NotificationList.jsx`)

Global notification system:

```javascript
/**
 * NotificationList Component
 * Displays global notifications from AppContext
 */

import { useAppContext } from '../context/AppContext';
import './NotificationList.css';

const NotificationList = () => {
  const { notifications, removeNotification } = useAppContext();

  if (notifications.length === 0) {
    return null;
  }

  return (
    <div className="notification-list">
      {notifications.map((notification) => (
        <div
          key={notification.id}
          className={`notification notification-${notification.type}`}
        >
          <span className="notification-message">{notification.message}</span>
          <button
            onClick={() => removeNotification(notification.id)}
            className="notification-close"
          >
            ✕
          </button>
        </div>
      ))}
    </div>
  );
};

export default NotificationList;
```

**Key Concepts:**
- ✅ **Loading States**: Proper loading indicators
- ✅ **Error Handling**: User-friendly error messages
- ✅ **Form Management**: Controlled inputs with validation
- ✅ **Notifications**: Global feedback system

---

### Phase 7: Main App Setup

#### 7.1 App Component (`src/App.jsx`)

```javascript
/**
 * Main App Component
 * Demonstrates React + Axios integration with dual state management
 */

import { useState } from 'react';
import { UserProvider } from './context/UserContext';
import { PostProvider } from './context/PostContext';
import { AppProvider } from './context/AppContext';
import UserList from './components/UserList';
import UserListContext from './components/UserListContext';
import PostList from './components/PostList';
import PostListContext from './components/PostListContext';
import CreateUserForm from './components/CreateUserForm';
import NotificationList from './components/NotificationList';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('users-hooks');

  return (
    <AppProvider>
      <UserProvider>
        <PostProvider>
          <div className="app">
            <NotificationList />
            
            <header className="app-header">
              <h1>React + Axios State Management</h1>
              <p className="subtitle">Local Hooks + Context API patterns</p>
            </header>

            <nav className="tab-navigation">
              <button
                className={`tab-button ${activeTab === 'users-hooks' ? 'active' : ''}`}
                onClick={() => setActiveTab('users-hooks')}
              >
                👥 Users (Hooks)
              </button>
              <button
                className={`tab-button ${activeTab === 'users-context' ? 'active' : ''}`}
                onClick={() => setActiveTab('users-context')}
              >
                👥 Users (Context)
              </button>
              <button
                className={`tab-button ${activeTab === 'posts-hooks' ? 'active' : ''}`}
                onClick={() => setActiveTab('posts-hooks')}
              >
                📝 Posts (Hooks)
              </button>
              <button
                className={`tab-button ${activeTab === 'posts-context' ? 'active' : ''}`}
                onClick={() => setActiveTab('posts-context')}
              >
                📝 Posts (Context)
              </button>
              <button
                className={`tab-button ${activeTab === 'create' ? 'active' : ''}`}
                onClick={() => setActiveTab('create')}
              >
                ➕ Create User
              </button>
            </nav>

            <main className="app-content">
              {activeTab === 'users-hooks' && <UserList />}
              {activeTab === 'users-context' && <UserListContext />}
              {activeTab === 'posts-hooks' && <PostList />}
              {activeTab === 'posts-context' && <PostListContext />}
              {activeTab === 'create' && <CreateUserForm />}
            </main>

            <footer className="app-footer">
              <p>
                Built with React 19 + Axios + Context API
              </p>
            </footer>
          </div>
        </PostProvider>
      </UserProvider>
    </AppProvider>
  );
}

export default App;
```

#### 7.2 Main Entry (`src/main.jsx`)

```javascript
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

---

## Testing & Development

### Run Development Server

```bash
npm run dev
```

Navigate to `http://localhost:5173`

### Build for Production

```bash
npm run build
```

### Preview Production Build

```bash
npm run preview
```

---

## Best Practices

### 1. **When to Use Hooks vs Context**

**Use Local Hooks When:**
- Component-specific state
- Simple data fetching
- No state sharing needed
- Better performance (no provider overhead)

**Use Context When:**
- Global state needed across many components
- Shared actions (create, update, delete)
- Authentication state
- Theme/settings
- Notifications

### 2. **Error Handling Strategy**

```javascript
// Service Layer: Let errors bubble up
export const userService = {
  getAllUsers: async () => {
    const response = await axiosInstance.get('/users');
    return response.data; // Don't catch here
  },
};

// Hook/Context Layer: Catch and set error state
const fetchUsers = async () => {
  try {
    const data = await userService.getAllUsers();
    setUsers(data);
  } catch (err) {
    setError(err.message); // Handle here
  }
};

// Component Layer: Display error to user
if (error) {
  return <div className="error">{error}</div>;
}
```

### 3. **Separation of Concerns**

```
Components     → UI only, no business logic
Hooks/Context  → State management, orchestration
Services       → API calls, pure functions
Axios Instance → HTTP config, interceptors
Config         → Constants, endpoints
```

### 4. **Performance Optimization**

```javascript
// ✅ Memoize callbacks
const fetchUsers = useCallback(async () => {
  // ...
}, []);

// ✅ Proper dependencies
useEffect(() => {
  fetchUsers();
}, [fetchUsers]);

// ✅ Prevent unnecessary rerenders
const value = useMemo(() => ({
  users,
  loading,
  fetchUsers,
}), [users, loading, fetchUsers]);
```

### 5. **Loading States**

Always handle three states:
- **Loading**: Show spinner
- **Error**: Show error message with retry
- **Success**: Show data

### 6. **Optimistic Updates**

```javascript
// Update UI immediately
setUsers(prev => [...prev, newUser]);

// Then make API call
try {
  await userService.createUser(newUser);
} catch (err) {
  // Revert on error
  setUsers(prev => prev.filter(u => u.id !== newUser.id));
}
```

---

## Common Patterns

### Pattern 1: Fetch on Mount

```javascript
useEffect(() => {
  fetchData();
}, []);
```

### Pattern 2: Refetch with Dependencies

```javascript
useEffect(() => {
  fetchPosts(userId);
}, [userId]);
```

### Pattern 3: Manual Trigger

```javascript
const handleRefresh = () => {
  refetch();
};
```

### Pattern 4: Form Submission

```javascript
const handleSubmit = async (e) => {
  e.preventDefault();
  await execute(() => service.create(data), {
    onSuccess: () => addNotification('Success!'),
    onError: () => addNotification('Error!'),
  });
};
```

---

## Troubleshooting

### Issue: "Context is undefined"

**Solution:** Ensure component is wrapped with Provider

```javascript
// ❌ Wrong
<UserList /> // Not wrapped

// ✅ Correct
<UserProvider>
  <UserList />
</UserProvider>
```

### Issue: Infinite Loop

**Solution:** Check useEffect dependencies

```javascript
// ❌ Wrong
useEffect(() => {
  setData([...data, item]); // data changes → reruns
}, [data]);

// ✅ Correct
useEffect(() => {
  setData(prev => [...prev, item]);
}, []); // Run once
```

### Issue: Stale Closures

**Solution:** Use useCallback with proper dependencies

```javascript
// ❌ Wrong
const handleClick = () => {
  console.log(users); // Stale
};

// ✅ Correct
const handleClick = useCallback(() => {
  console.log(users);
}, [users]);
```

---

## Next Steps

1. **Add TypeScript** for type safety
2. **Add React Query** for advanced data fetching
3. **Add Testing** with Vitest and React Testing Library
4. **Add Routing** with React Router
5. **Add State Management** with Redux/Zustand (if needed)
6. **Add Error Boundaries** for better error handling
7. **Add Authentication Flow** with JWT
8. **Add Caching Strategy** with service workers
9. **Add CI/CD Pipeline** for automated deployments

---

## Summary

This system demonstrates:

✅ **Modular Architecture**: Clear separation of concerns  
✅ **Dual Patterns**: Both local hooks and global context  
✅ **Error Handling**: Comprehensive error states  
✅ **Scalability**: Easy to add new features  
✅ **Maintainability**: Well-organized code structure  
✅ **Performance**: Optimized with React best practices  
✅ **Documentation**: JSDoc and comments throughout  

**Key Takeaway**: The service layer makes it easy to use the same API calls in both hooks and contexts, giving you flexibility in choosing the right state management approach for each use case.
