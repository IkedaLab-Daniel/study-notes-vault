console.log('\n\n\n')
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

const logMiddleware = store => next => action => {
    console.log('old state', store.getState(), action);
    next(action);
    console.log('new state', store.getState(), action);
}

const store = createStore(reducer, applyMiddleware(logMiddleware));

store.dispatch({ type: "dev.iceice" });