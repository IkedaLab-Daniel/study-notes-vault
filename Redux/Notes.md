# Redux Fundamentals (feat. React)

## 1 - Introduction
- Flux architecture
- Redux:
    - Handle States globally
    - A library
    - Can be use on frontend frameworks like React and Angular

## 2 - Redux API's & Compose
- Compose
    - Redux function to put many function into one singe function
```js
const makeLouder = string => string.toUpperCase();
const repeatThreeTimes = string => string.repeat(3);
const embolden = string => string.bold();

const makeLouderRepeatThreeTimesAndEmbolden = compose(embolden, repeatThreeTimes, makeLouder)
```

## 3 - Redux Stores and Reducers
createStore() expect the reducer
- reducer - 2 things come in, one thing comes out
- React -> (state of the world, something happen) -> [reducer: New state of the world] -> React
- replaceReducer:
    - all it does is that function you passed in,replace reducer takes one argument, which is a new reducer and it swaps it out.
    - for code splitting
- getState:
    - get a state :O
    - to determine what should be pass on components
- action:
    - main requirement is a "type"

## 4 - Redux Stores & Dispatch
- Why shout the type values
```js
    { type: 'INCREMENT' }
```
   - because these types are CONSTANTS
   - seperate to other variables
   - to create a constant in the beginning and use that. So mispell show reference error
   - other convention:
```js
    { type: 'counter/increment' }
```

## 5 - Action Creators
- Action Creator
```js
const increment = (amount) => ({ type: "INCREMENT", payload: amount})
```
- simple but powerful
- if you decided to change a feature, refactoring will be easier

## 6 - Setting initialState
- getState()
    - return the current state
- initialValue()
    - must be pass on reducer (recommended) or the store
```js
const initialState  = { value: 0 };
const reducer = (state = initialState, action) => { ...
```

## 7 - Some Rules for Reducers
*disover at your own peril*
- No mutating objects. If you touch it, you replace it.
- You have to return something and ideally, it should be the unchanged state if there is nothing you need to do it.
- It's just a JavaScript function

**Prefer Flat Objects**
```js
const angryBlogPost = {
    title: 'A letter to the editor',
    content: 'I am very salty about',
    author: {
        firstName: 'Steve',
        lastName: 'Kinney',
        location: {
            city: 'Denver',
        }
    }
}
```
Sample reducer action
```js
if (action.type === 'CITY_CHANGE'){
    return{
        ...state,
        author: {
            ...state.author,
            location: {
                city: action.payload,
            }
        }
    }
}
```
- Does it make sense to have multile stores?
    - No, it's an anti-pattern
    - Usually only one provider
    - Generally speaking, you'll have one store and one giant set of data

## 8 - Subscribe & Binding Action Creators
- subscribe
    - Like an event listener in DOM
    - *I care about changes on this state. Here's the function to will give u to go ahead*

Sample subscriber function to be called:
```js
const subscriber = () => console.log('SUBSCRIBER', store.getState());
```

Sample implementation
```js
store.subscribe(subscriber); // ? subscribe the subscriber-function
store.dispatch(increment()); // ? using the function (recommended)
store.dispatch( { type: INCREMENT }); // ? explicit, not recommended for future refactoring
store.dispatch(add(100));
```

Sample output:
```bash
SUBSCRIBER { value: 1 }
SUBSCRIBER { value: 2 }
SUBSCRIBER { value: 102 }
```

- bindActionCreators
    - functions that create actions
    - function bound to the dispatch that we can call
```js
const actions = bindActionCreators({ increment, add, }, store.dispatch)

console.log(actions)

actions.add(1000);
actions.increment();

console.log(store.getState)
```
 - Where *increment, add* are defined functiuons
 - *store.dispatch* is where it will bin
 
 ## 9 - Combine Reducers
 - combineReducers()
 - When project gets bigger
 - Split stuffs into 2 or more reducers

Standard:
```js
const addTask = (title) => ({ type: ADD_TASK, payload: title});
const addUser = (name) => ({ type: ADD_USER, payload: name});

const reducer = (state = initialState, action) => {
    if (action.type === ADD_USER){
        return {
            ...state,
            users: [...state.users, action.payload]
        };
    }

    if (action.type === ADD_TASK){
        return{
            ...state,
            tasks: [...state.tasks, action.payload]
        };
    }
};
```

Refactored:
```js
const addTask = (title) => ({ type: ADD_TASK, payload: title});
const addUser = (name) => ({ type: ADD_USER, payload: name});

const userReducer = (users = initialState.users, action) => {
    if (action.type === ADD_USER){
        return [...users, action.payload]
    }

    return users;
};

const taskReducer = (tasks = initialState.tasks, action) => {
    if (action.type === ADD_TASK){
        return [...tasks, action.payload]
    }

    return tasks
}

const reducer = combineReducers({ users: userReducer, tasks: taskReducer })
const store = createStore(reducer);
```

- every action flows through every single reducer

## 10 - Enhancers
- createStrore() enchancer
- create a copy of the store, do anything what we need to it
```js
/**
 * Creates a Redux store that holds the state tree.
 *
 * @param {Function} reducer - A function that returns the next state tree, given the current state and an action to handle.
 * @param {any} [preloadedState={}] - The initial state. You may optionally specify it to hydrate the state from the server in universal apps, or to restore a previously serialized user session.
 * @param {Function} [enhancer] - The store enhancer. You may optionally specify it to enhance the store with third-party capabilities such as middleware, time travel, persistence, etc.
 * @returns {Store} A Redux store that lets you read the state, dispatch actions, and subscribe to changes.
 */
```

Most basic enchancer that does nothing:
```js
const monitorEnhancer = (createStore) => (reducer, initialState, enhancer) => {
    return createStore(reducer, initialState, enhancer);
}
```

- it's kinda middleware
- applyMiddleware on the other hand takes in multiple middleware and compose it

Sample:
```js
const reducer = state => state

const monitorEnhancer = (createStore) => (reducer, initialState, enhancer) => {
    const monitorReducer = (state, action) => {
        const start = performance.now();
        const newState = reducer(state, action)
        const end = performance.now();
        const diff = end - start
        console.log(diff)

        return newState
    }

    return createStore(monitorReducer, initialState, enhancer)
}

/**
 * Creates a Redux store that holds the state tree.
 *
 * @param {Function} reducer - A function that returns the next state tree, given the current state and an action to handle.
 * @param {any} [preloadedState={}] - The initial state. You may optionally specify it to hydrate the state from the server in universal apps, or to restore a previously serialized user session.
 * @param {Function} [enhancer] - The store enhancer. You may optionally specify it to enhance the store with third-party capabilities such as middleware, time travel, persistence, etc.
 * @returns {Store} A Redux store that lets you read the state, dispatch actions, and subscribe to changes.
 */
const store = createStore(reducer, {}, monitorEnhancer)

store.dispatch({ type: "dev.iceice" })
```

## 11 - Enhancers Exercise
- Make: console log the state before we call the reducer and console log it again afterwards
- So no need to have console.log() on all the reducers - Make one enchancer to do that

This is the sht i made:
```js
import {
  createStore,
  compose,
  applyMiddleware,
  bindActionCreators,
  combineReducers
} from 'redux';

const reducer = state => state

const logEnhancer = (createStore) => (reducer, initialState, enhancer) => {
    const logState = (state, action) => {
        // ? console log initial state
        console.log("\nBefore:", state)
        state += 1
        const newState = state;
        console.log("After:", newState)
        
        return newState;
    }

    return createStore(logState, initialState, enhancer)
}

const store = createStore(reducer, 1, logEnhancer)

store.dispatch({ type: "dev.iceice" })
```

Output:
```bash
Before: 1
After: 2

Before: 2
After: 3
```

## 12 - Enhancer Solution
_LOL! The solution actually used "logEnhancer" as name for the enchancer like my solution HAHA_
Solution:
```js
import {
  createStore,
  compose,
  applyMiddleware,
  bindActionCreators,
  combineReducers
} from 'redux';

const reducer = (state = { count: 1}) => state

const logEnhancer = (createStore) => (reducer, initialState, enhancer) => {
    const logReducer = (state, action) => {
        console.log('old state', state, action);
        const newState = reducer(state, action);
        console.log('new state', newState, action)

        return newState
    }

    return createStore(logReducer, initialState, enhancer)
}

const store = createStore(reducer, logEnhancer);

// ? if you have two or more enchancers
// const store = createStore(reducer, compose(logEnhancer, anotherEnchanger, moreEnhancer));

store.dispatch({ type: "dev.iceice" });
```

## 13 - Middleware
- applyMiddleware()
    - middlewares are much more common
    - gives you opportunity to do a bunch of things before you hit the reducer
    - syntax is little bit cleaner

```js
const reducer = (state = { count: 1}) => state

const logEnhancer = (createStore) => (reducer, initialState, enhancer) => {
    const logReducer = (state, action) => {
        console.log('old state', state, action);
        const newState = reducer(state, action);
        console.log('new state', newState, action)

        return newState
    }

    return createStore(logReducer, initialState, enhancer)
}

const logMiddleware = store => next => action => {
    console.log('old state', store.getState(), action);
    next(action);
    console.log('new state', store.getState(), action);
}

const store = createStore(reducer, applyMiddleware(logMiddleware));

store.dispatch({ type: "dev.iceice" });
```

