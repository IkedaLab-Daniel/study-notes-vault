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
      setError(err.message);
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
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const deleteUser = useCallback(async (id) => {
    try {
      setLoading(true);
      setError(null);
      const result = await userService.deleteUser(id);
      return result;
    } catch (err) {
      setError(err.message);
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
