/**
 * CreateUserForm Component
 * Demonstrates POST request with optimistic UI updates
 * Shows form state management and mutation handling
 */

import { useState } from 'react';
import { useUserMutations } from '../hooks/useUsers';
import './CreateUserForm.css';

const CreateUserForm = ({ onUserCreated }) => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
  });
  
  const [showSuccess, setShowSuccess] = useState(false);
  const { createUser, loading, error } = useUserMutations();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const newUser = await createUser(formData);
      console.log('User created:', newUser);
      
      // Show success message
      setShowSuccess(true);
      setTimeout(() => setShowSuccess(false), 3000);
      
      // Reset form
      setFormData({ name: '', email: '', phone: '' });
      
      // Callback to parent
      if (onUserCreated) {
        onUserCreated(newUser);
      }
    } catch (err) {
      console.error('Failed to create user:', err);
    }
  };

  return (
    <div className="create-user-form">
      <h3>Create New User</h3>
      
      {showSuccess && (
        <div className="success-message">
          ✅ User created successfully!
        </div>
      )}

      {error && (
        <div className="error-message">
          ❌ {error}
        </div>
      )}

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name *</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
            disabled={loading}
            placeholder="Enter name"
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
            disabled={loading}
            placeholder="Enter email"
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
            disabled={loading}
            placeholder="Enter phone number"
          />
        </div>

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
