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

const  monitorMiddleware= store => next => action => {
    const start = performance.now();
    console.log('start:', start)
    next(action);
    const end = performance.now();
    console.log('end:', end)
    const diff = end - start
    console.log('diff:', diff)
}

const store = createStore(reducer, applyMiddleware(logMiddleware, monitorMiddleware));

store.dispatch({ type: "dev.iceice" });