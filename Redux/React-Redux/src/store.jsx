import { createStore } from 'redux'
import { reducer } from './reducer'

const enhancer = window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__();


export const store = createStore(reducer, enhancer)