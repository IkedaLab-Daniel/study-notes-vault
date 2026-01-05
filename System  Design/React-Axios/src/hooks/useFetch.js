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
