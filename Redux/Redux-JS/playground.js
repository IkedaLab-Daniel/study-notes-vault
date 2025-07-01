console.log('\n\n\n')
import {
  createStore,
  compose,
  applyMiddleware,
  bindActionCreators
} from 'redux';

const initialState  = { value: 0 };

// > actions constants
const INCREMENT = "INCREMENT";
const ADD = "ADD";

const incrementAction = { type: INCREMENT, payload: 5 };

// > action creator
const increment = () => ({ type: INCREMENT })
const add = (amount) => ({ type: ADD, payload: amount})

// > reducer
const reducer = (state = initialState, action) => {
  if (action.type === 'INCREMENT'){
    return { value: state.value + 1 }
  }

  if (action.type === ADD){
    return { value: state.value + action.payload}
  }

  return state;
}

// > subscribe
const subscriber = () => console.log('SUBSCRIBER', store.getState());

const store = createStore(reducer);

// > bindActionCreators
const actions = bindActionCreators({ increment, add, }, store.dispatch)

console.log(actions)

actions.add(1000);
actions.increment();

console.log(store.getState)
