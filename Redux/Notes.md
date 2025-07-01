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
    