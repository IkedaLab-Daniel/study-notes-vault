/**
 * User Context
 * Global state management for user-related data
 * Demonstrates Context API pattern for shared state across components
 */

import { createContext, useContext, useState, useCallback, useEffect } from 'react';
import { userService } from '../services/userService';

// Create Context
const UserContext = createContext(undefined);

// Provider Component
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

  // Clear error
  const clearError = useCallback(() => {
    setError(null);
  }, []);

  // Select user
  const selectUser = useCallback((user) => {
    setSelectedUser(user);
  }, []);

  // Load users on mount
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
    selectUser,
    clearError,
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
