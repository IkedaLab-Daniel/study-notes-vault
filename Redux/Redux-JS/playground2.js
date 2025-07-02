console.log('\n\n\n')
import {
  createStore,
  compose,
  applyMiddleware,
  bindActionCreators,
  combineReducers
} from 'redux';

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