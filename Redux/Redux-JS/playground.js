console.log('\n\n\n')
import {
  createStore,
  compose,
  applyMiddleware,
  bindActionCreators
} from 'redux';

const initialState  = { value: 0 };

const incrementAction = { type: 'INCREMENT', payload: 5 };

const reducer = (state, action) => {
  if (action.type === 'INCREMENT'){
    return { state: state.value + 1 }
  }

  return state;
}

const store = createStore(reducer);

console.log(store)