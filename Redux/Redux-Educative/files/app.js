// Our mutation (reducer) function creates
// a _new_ state based on the action passed
function reducer(state, action) {
  switch (action.type) {
    case 'INC':
      return Object.assign({}, state, { counter: state.counter + 1 });
    case 'DEC':
      return Object.assign({}, state, { counter: state.counter - 1 });
    default:
      return state;
  }
}

function test(){
    store.dispatch({ type: 'INC' });
}

const initialState = {
  counter: 3
};

const store = Redux.createStore(reducer, initialState);

// Function to update view (this might be React or Angular in a real app)
function updateView() {
  document.querySelector('#counter').innerText = store.getState().counter;
}

store.subscribe(updateView);

// Update view for the first time
updateView();

// Listen to click events
document.getElementById('inc').onclick = () => store.dispatch({ type: 'INC' });
document.getElementById('dec').onclick = () => store.dispatch({ type: 'DEC' });