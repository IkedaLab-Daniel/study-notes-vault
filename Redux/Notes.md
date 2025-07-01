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

