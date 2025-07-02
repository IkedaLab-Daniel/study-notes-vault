console.log('\n\n\n')
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