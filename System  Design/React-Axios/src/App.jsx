/**
 * Main App Component
 * Demonstrates React + Axios integration with proper state management
 * Features: Local hooks AND Context API patterns
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
                Built with React 19 + Axios + Context API | Data from{' '}
                <a href="https://jsonplaceholder.typicode.com" target="_blank" rel="noopener noreferrer">
                  JSONPlaceholder
                </a>
              </p>
            </footer>
          </div>
        </PostProvider>
      </UserProvider>
    </AppProvider>
  );
}

export default App;
