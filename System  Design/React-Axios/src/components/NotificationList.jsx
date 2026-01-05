/**
 * NotificationList Component
 * Displays global notifications from AppContext
 * Demonstrates cross-component communication via Context
 */

import { useAppContext } from '../context/AppContext';
import './NotificationList.css';

const NotificationList = () => {
  const { notifications, removeNotification } = useAppContext();

  if (!notifications.length) return null;

  return (
    <div className="notification-container">
      {notifications.map((notification) => (
        <div 
          key={notification.id} 
          className={`notification notification-${notification.type}`}
        >
          <span className="notification-message">{notification.message}</span>
          <button 
            className="notification-close"
            onClick={() => removeNotification(notification.id)}
          >
            ✕
          </button>
        </div>
      ))}
    </div>
  );
};

export default NotificationList;
