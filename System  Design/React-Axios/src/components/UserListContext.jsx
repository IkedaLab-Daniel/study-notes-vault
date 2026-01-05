/**
 * UserListContext Component
 * Uses Context API for global state management
 * Compare with UserList.jsx which uses local hooks
 */

import { useUserContext } from '../context/UserContext';
import { useAppContext } from '../context/AppContext';
import './UserList.css';

const UserListContext = () => {
  const { users, loading, error, fetchUsers, selectUser } = useUserContext();
  const { addNotification } = useAppContext();

  const handleRefresh = async () => {
    try {
      await fetchUsers();
      addNotification('Users refreshed successfully!', 'success');
    } catch (err) {
      addNotification('Failed to refresh users', 'error');
    }
  };

  const handleSelectUser = (user) => {
    selectUser(user);
    addNotification(`Selected user: ${user.name}`, 'info');
  };

  if (loading) {
    return (
      <div className="user-list-container">
        <div className="loading">
          <div className="spinner"></div>
          <p>Loading users from Context...</p>
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
          <button onClick={handleRefresh} className="retry-button">
            Retry
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="user-list-container">
      <div className="header">
        <div>
          <h2>Users - Context API ({users?.length || 0})</h2>
          <p style={{ fontSize: '12px', color: '#666', margin: '5px 0 0 0' }}>
            Using global state via useUserContext()
          </p>
        </div>
        <button onClick={handleRefresh} className="refresh-button">
          🔄 Refresh
        </button>
      </div>

      <div className="user-grid">
        {users?.map((user) => (
          <div 
            key={user.id} 
            className="user-card"
            onClick={() => handleSelectUser(user)}
            style={{ cursor: 'pointer' }}
          >
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
