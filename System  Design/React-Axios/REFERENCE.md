# React + Axios + State Management Reference

A comprehensive reference implementation showcasing **industry-standard patterns** for integrating React with Axios, featuring proper state management, error handling, and clean architecture.

## 🎯 Features

- ✅ **Centralized Axios Configuration** with interceptors
- ✅ **Service Layer Pattern** for API abstraction
- ✅ **Custom Hooks** for local state management
- ✅ **Context API** for global state management
- ✅ **Proper State Management** (loading, error, data states)
- ✅ **Error Handling** with global interceptors
- ✅ **Optimistic UI Updates**
- ✅ **Request/Response Logging** (dev mode)
- ✅ **Authentication Token Handling**
- ✅ **Global Notifications System**
- ✅ **Clean Component Architecture**

## 📁 Project Structure

```
src/
├── api/
│   └── axiosInstance.js          # Configured Axios instance with interceptors
├── config/
│   └── api.config.js              # API configuration and endpoints
├── services/
│   ├── userService.js             # User-related API calls
│   └── postService.js             # Post-related API calls
├── context/                       # Global state management (Context API)
│   ├── AppContext.jsx             # App-wide state (auth, theme, notifications)
│   ├── UserContext.jsx            # Global user state
│   └── PostContext.jsx            # Global post state with filtering
├── hooks/                         # Local state management
│   ├── useFetch.js                # Generic data fetching hook
│   ├── useApi.js                  # Advanced API hook with optimistic updates
│   ├── useUsers.js                # User-specific hooks
│   └── usePosts.js                # Post-specific hooks
├── components/
│   ├── UserList.jsx               # User list (local hooks pattern)
│   ├── UserListContext.jsx        # User list (Context API pattern)
│   ├── PostList.jsx               # Posts (local hooks pattern)
│   ├── PostListContext.jsx        # Posts (Context API pattern)
│   ├── PostDetail.jsx             # Post details modal with nested data
│   ├── CreateUserForm.jsx         # Form with mutation handling
│   └── NotificationList.jsx       # Global notification display
└── App.jsx                        # Main application with Providers
```

## 🚀 Quick Start

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

### Build

```bash
npm run build
```

## 🏗️ Architecture Patterns

### 1. **Context API for Global State**

The project demonstrates **BOTH** state management patterns:

#### **Local State (Hooks)** - For component-specific data
```javascript
// In component
const { users, loading, error } = useUsers();
```
✅ Use when: Data is used in one component/tree  
✅ Benefits: Simple, no provider needed, isolated state

#### **Global State (Context)** - For app-wide shared data
```javascript
// Wrap app with providers
<UserProvider>
  <C3mponent />
</UserProvider>

// In any nested component
const { users, loading, createUser } = useUserContext();
```
✅ Use when: Data shared across multiple components  
✅ Benefits: No prop drilling, synchronized state, global actions

### Example Contexts:

**AppContext** - App-wide settings
```javascript
const { theme, isAuthenticated, addNotification } = useAppContext();
```

**UserContext** - Global user management
```javascript
const { users, selectedUser, createUser, deleteUser } = useUserContext();
```

**PostContext** - Posts with computed filters
```javascript
const { filteredPosts, setUserFilter, setSearchFilter } = usePostContext();
```

### 2. **Axios Instance Configuration**

Located in [`src/api/axiosInstance.js`](src/api/axiosInstance.js)

- Single axios instance for the entire app
- Request interceptors for auth tokens
- Response interceptors for global error handling
- Environment-aware logging

```javascript
import axiosInstance from './api/axiosInstance';

// Use in services
const response = await axiosInstance.get('/users');
```

### 2. **Service Layer Pattern**

Services abstract API calls from components:

```javascript
// services/userService.js
export const userService = {
  getAllUsers: async () => {...},
  getUserById: async (id) => {...},
  createUser: async (userData) => {...},
  updateUser: async (id, userData) => {...},
  deleteUser: async (id) => {...},
};
```

**Benefits:**
- Centralized API logic
- Easy to test and mock
- Reusable across components
- Type-safe contracts

### 4. **Custom Hooks for Data Fetching**

#### `useFetch` - Generic fetching hook

```javascript
const { data, loading, error, refetch } = useFetch(
  () => userService.getAllUsers(),
  [], // dependencies
  true // immediate fetch
);
```

#### `useApi` - Advanced mutations hook

```javascript
const { execute, loading, error, data } = useApi();

await execute(
  () => userService.createUser(userData),
  {
    onSuccess: (result) => console.log('Success!', result),
    onError: (err) => console.error('Failed', err),
    optimisticData: tempData // Optimistic update
  }
);
```

#### Domain-specific hooks

```javascript
// useUsers.js
const { users, loading, error, refetch } = useUsers();
const { createUser, updateUser, deleteUser } = useUserMutations();

// usePosts.js
const { posts, loading, error } = usePosts({ userId: 1 });
const { post } = usePost(postId);
const { comments } = usePostComments(postId);
```

### 5. **State Management Pattern**

Every data-fetching component follows the same pattern:

```javascript
const Component = () => {
  const { data, loading, error, refetch } = useCustomHook();

  if (loading) return <LoadingState />;
  if (error) return <ErrorState error={error} onRetry={refetch} />;
  return <SuccessState data={data} />;
};
```

**States handled:**
- `loading` - Initial and refetch loading
- `error` - Error messages with retry capability
- `data` - Successfully fetched data
- `refetch` - Manual data refresh

## 📚 Key Concepts

### Request Interceptors

Add headers, auth tokens, logging:

```javascript
axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  }
);
```

### Response Interceptors

Handle errors globally:

```javascript
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized
      localStorage.removeItem('authToken');
    }
    return Promise.reject(error);
  }
);
```

### Error Handling

Multiple layers:

1. **Global** - Interceptors
2. **Service** - Service layer try/catch
3. **Component** - Hook error states
4. **UI** - Error boundaries (optional)

### Environment Configuration

Use `.env` files:

```env
VITE_API_BASE_URL=https://api.example.com
```

Access in code:

```javascript
const baseURL = import.meta.env.VITE_API_BASE_URL;
```

## 🎨 Components Overview

### UserList (Local Hooks)
- Uses `useUsers()` hook for local state
- Independent state per instance
- Loading and error states
- Manual refresh capability

### UserListContext (Global Context)
- Uses `useUserContext()` for shared state
- State synchronized across all instances
- Notifications on actions
- User selection propagates globally

### PostList (Local Hooks)
- Uses `usePosts()` hook
- Parameterized API calls
- Local filtering logic

### PostListContext (Global Context)
- Uses `usePostContext()`
- Computed filtered posts with `useMemo`
- Search and user filters
- State shared across app

### NotificationList
- Global notification system
- Consumes `useAppContext()`
- Auto-dismiss after 5 seconds
- Success/error/info types

### PostDetail (Modal)
- Shows post with comments
- Nested data fetching
- Modal backdrop click handling
- Separate loading states

### CreateUserForm
- POST request example
- Form state management
- Success/error feedback
- Optimistic UI updates

## 🔥 Best Practices Implemented

### ✅ Separation of Concerns
- API logic in services
- State logic in hooks
- Presentation in components

### ✅ DRY (Don't Repeat Yourself)
- Reusable hooks
- Generic `useFetch` pattern
- Centralized config

### ✅ Error Handling
- Try/catch in services
- Error states in hooks
- User-friendly error messages
- Retry mechanisms

### ✅ Loading States
- PrWhen to Use Local Hooks vs Context

#### ✅ Use Local Hooks When:
- Data is component-specific
- No need to share across components
- Performance is critical (avoid re-renders)
- Simple CRUD operations

#### ✅ Use Context When:
- Data shared across multiple components
- Need to avoid prop drilling
- App-wide settings (theme, auth, notifications)
- Synchronized state across views

### oper loading indicators
- Disabled states during mutations
- Skeleton screens (optional)

### ✅ Performance
- `useCallback` for stable references
- Conditional fetching
- Debouncing (where needed)
- Memoization with `useMemo`

### ✅ Type Safety
- JSDoc comments
- Prop validation (can add PropTypes)
- Clear function signatures

## 🔄 Common Patterns

### Fetching on Mount

```javascript
const { data } = useFetch(fetchFunction, [], true);
```

### Conditional Fetching

```javascript
const { data } = useFetch(
  () => getUser(userId),
  [userId],
  !!userId // Only fetch if userId exists
);
```

### Manual Fetching

```javascript
const { data, refetch } = useFetch(fetchFunction, [], false);

// Later...
const handleClick = () => refetch();
```

### Parameterized Fetching

```javascript
const { posts } = usePosts({ userId: selectedUserId });
// Refetches when selectedUserId changes
```

### Optimistic Updates

```javascript
const { execute } = useApi();

await execute(
  () => createPost(newPost),
  {
    optimisticData: { id: 'temp', ...newPost },
    onSuccess: () => refetch(),
  }
);
```

## 🛠️ Extending the Example

### Add New Service

1. Create service file in `services/`
2. Define API methods
3. Export service object

```javascript
// services/commentService.js
export const commentService = {
  getAll: async () => {...},
  getById: async (id) => {...},
};
```
Context API for global state
- ✅ Choosing between local hooks vs Context
- ✅ Implementing service layer pattern
- ✅ Managing loading/error states
- ✅ Handling API authentication
- ✅ Building notification systems
1. Create hook file in `hooks/`
2. Use `useFetch` or `useApi`
3. Export hook

```javascript
// hooks/useComments.js
export const useComments = () => {
  return useFetch(() => commentService.getAll());
};
```

### Add New Component

1. Create component in `components/`
2. Import custom hook
3. Handle states (loading/error/success)

## 📖 Learning Resources

- [Axios Documentation](https://axios-http.com/docs/intro)
- [React Hooks](https://react.dev/reference/react)
- [Custom Hooks Guide](https://react.dev/learn/reusing-logic-with-custom-hooks)
- [API Service Pattern](https://kentcdodds.com/blog/eliminate-an-entire-category-of-bugs-with-a-few-simple-tools)

## 🎯 Use This As Reference For

- ✅ Setting up Axios in React
- ✅ Creating reusable data-fetching hooks
- ✅ Implementing service layer pattern
- ✅ Managing loading/error states
- ✅ Handling API authentication
- ✅ Organizing React project structure
- ✅ Implementing CRUD operations
- ✅ Building scalable React apps

## 📝 Notes

- Uses [JSONPlaceholder](https://jsonplaceholder.typicode.com) as mock API
- For production, replace with your actual API endpoint in `.env`
- Add authentication logic as needed
- Consider adding React Query/SWR for advanced caching

## 🤝 Contributing

This is a reference implementation. Feel free to adapt patterns to your needs.

---

**Built with ❤️ using React 19 + Axios + Vite**
