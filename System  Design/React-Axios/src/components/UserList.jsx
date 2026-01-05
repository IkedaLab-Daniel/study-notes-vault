/**
 * UserList Component
 * Displays a list of users fetched from API
 * Demonstrates proper loading and error state handling
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
