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
