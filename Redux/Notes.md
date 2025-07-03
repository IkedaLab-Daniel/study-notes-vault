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

## 6 - Setting initialState
- getState()
    - return the current state
- initialValue()
    - must be pass on reducer (recommended) or the store
```js
const initialState  = { value: 0 };
const reducer = (state = initialState, action) => { ...
```

## 7 - Some Rules for Reducers
*disover at your own peril*
- No mutating objects. If you touch it, you replace it.
- You have to return something and ideally, it should be the unchanged state if there is nothing you need to do it.
- It's just a JavaScript function

**Prefer Flat Objects**
```js
const angryBlogPost = {
    title: 'A letter to the editor',
    content: 'I am very salty about',
    author: {
        firstName: 'Steve',
        lastName: 'Kinney',
        location: {
            city: 'Denver',
        }
    }
}
```
Sample reducer action
```js
if (action.type === 'CITY_CHANGE'){
    return{
        ...state,
        author: {
            ...state.author,
            location: {
                city: action.payload,
            }
        }
    }
}
```
- Does it make sense to have multile stores?
    - No, it's an anti-pattern
    - Usually only one provider
    - Generally speaking, you'll have one store and one giant set of data

## 8 - Subscribe & Binding Action Creators
- subscribe
    - Like an event listener in DOM
    - *I care about changes on this state. Here's the function to will give u to go ahead*

Sample subscriber function to be called:
```js
const subscriber = () => console.log('SUBSCRIBER', store.getState());
```

Sample implementation
```js
store.subscribe(subscriber); // ? subscribe the subscriber-function
store.dispatch(increment()); // ? using the function (recommended)
store.dispatch( { type: INCREMENT }); // ? explicit, not recommended for future refactoring
store.dispatch(add(100));
```

Sample output:
```bash
SUBSCRIBER { value: 1 }
SUBSCRIBER { value: 2 }
SUBSCRIBER { value: 102 }
```

- bindActionCreators
    - functions that create actions
    - function bound to the dispatch that we can call
```js
const actions = bindActionCreators({ increment, add, }, store.dispatch)

console.log(actions)

actions.add(1000);
actions.increment();

console.log(store.getState)
```
 - Where *increment, add* are defined functiuons
 - *store.dispatch* is where it will bin
 
 ## 9 - Combine Reducers
 - combineReducers()
 - When project gets bigger
 - Split stuffs into 2 or more reducers

Standard:
```js
const addTask = (title) => ({ type: ADD_TASK, payload: title});
const addUser = (name) => ({ type: ADD_USER, payload: name});

const reducer = (state = initialState, action) => {
    if (action.type === ADD_USER){
        return {
            ...state,
            users: [...state.users, action.payload]
        };
    }

    if (action.type === ADD_TASK){
        return{
            ...state,
            tasks: [...state.tasks, action.payload]
        };
    }
};
```

Refactored:
```js
const addTask = (title) => ({ type: ADD_TASK, payload: title});
const addUser = (name) => ({ type: ADD_USER, payload: name});

const userReducer = (users = initialState.users, action) => {
    if (action.type === ADD_USER){
        return [...users, action.payload]
    }

    return users;
};

const taskReducer = (tasks = initialState.tasks, action) => {
    if (action.type === ADD_TASK){
        return [...tasks, action.payload]
    }

    return tasks
}

const reducer = combineReducers({ users: userReducer, tasks: taskReducer })
const store = createStore(reducer);
```

- every action flows through every single reducer

## 10 - Enhancers
- createStrore() enchancer
- create a copy of the store, do anything what we need to it
```js
/**
 * Creates a Redux store that holds the state tree.
 *
 * @param {Function} reducer - A function that returns the next state tree, given the current state and an action to handle.
 * @param {any} [preloadedState={}] - The initial state. You may optionally specify it to hydrate the state from the server in universal apps, or to restore a previously serialized user session.
 * @param {Function} [enhancer] - The store enhancer. You may optionally specify it to enhance the store with third-party capabilities such as middleware, time travel, persistence, etc.
 * @returns {Store} A Redux store that lets you read the state, dispatch actions, and subscribe to changes.
 */
```

Most basic enchancer that does nothing:
```js
const monitorEnhancer = (createStore) => (reducer, initialState, enhancer) => {
    return createStore(reducer, initialState, enhancer);
}
```

- it's kinda middleware
- applyMiddleware on the other hand takes in multiple middleware and compose it

Sample:
```js
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
```

## 11 - Enhancers Exercise
- Make: console log the state before we call the reducer and console log it again afterwards
- So no need to have console.log() on all the reducers - Make one enchancer to do that

This is the sht i made:
```js
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
```

Output:
```bash
Before: 1
After: 2

Before: 2
After: 3
```

## 12 - Enhancer Solution
_LOL! The solution actually used "logEnhancer" as name for the enchancer like my solution HAHA_
Solution:
```js
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

const store = createStore(reducer, logEnhancer);

// ? if you have two or more enchancers
// const store = createStore(reducer, compose(logEnhancer, anotherEnchanger, moreEnhancer));

store.dispatch({ type: "dev.iceice" });
```

## 13 - Middleware
- applyMiddleware()
    - middlewares are much more common
    - gives you opportunity to do a bunch of things before you hit the reducer
    - syntax is little bit cleaner

```js
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
```

## 14 - Middleware Exercise
Basically turn the performance monitor enchanher into middleware and add it to applymiddleware
My solution:
```js
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
```

Output:
```bash
old state { count: 1 } { type: 'dev.iceice' }
start: 36.46675
end: 36.702084
diff: 0.2353340000000017
new state { count: 1 } { type: 'dev.iceice' }
```

## 15 - Middleware Solution
- to remember middleware structure = "SNAck"
> const  monitorMiddleware= **S** tore => **N** ext => **A** ction => { ...

Solution:
```js
const  monitorMiddleware= store => next => action => {
    const start = performance.now();
    next(action);
    const end = performance.now();
    const diff = end - start
    console.log(diff)
}
```

## React - Redux notes
- useSelector
    - a fancy word for a function in Redux
    - get something in the global state
    ```js
      const count = useSelector(state => state.count);
    ```
- Redux devtools extension
    - add this as an enhancer on store:
```js
window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__();
```

```js
const enhancer = window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__();
export const store = createStore(reducer, enhancer) 
```

## Lesson: Connecting Increment and Decrement
If have redux on a React project, should we never use useState()?
- No. There are other types of state, like model state, that no need to be in Redux for their state management. One good example are Forms. We usually use useState() on changed of in the fields; if we were to use redux, there a lot of dispatch just for a simple state model

## Lesson: Binding Actions
There many ways be can bind actions to useReducers in a component

1. Standard:
```jsx
...
const dispatch = useDispatch();
...
<button onClick={() => dispatch(increment())}>Increment</button>
....
```

2. Using bindActionCreators() (from 'redux' toolkit):
```js
...
const actions = bindActionCreators({ increment, decrement, set}, dispatch)
...
<button onClick={() => actions.increment()}>Increment</button>
...
```

3. custom hook (use-action):
- use-action.jsx:
```js
import { useDispatch } from "react-redux"
import { bindActionCreators} from 'redux'

export const useActions = (actions) => {
    const dispatch = useDispatch();
    return bindActionCreators(actions, dispatch)
}
```

- components:
```js
const actions = useActions({increment, decrement, set});
...
<button onClick={() => actions.increment()}>Increment</button>
```

4. *take logic and make useCounter*
- use-counter.jsx:
```js
import { useSelector } from "react-redux"
import { useActions } from "./use-actions";
import { increment, decrement, set } from "./action";

export const useCounter = () => {
    const count = useSelector(state => state.count);
    const actions = useActions({increment, decrement, set})

    return { count, ...actions}
}
```

- use-actions.jsx: just like above
- components:
```js
const { count, increment, decrement, set } = useCounter()
...
<button onClick={() => increment()}>Increment</button>
...
```

## Lesson: Connect API vs Hooks
### Hooks
- built in React Hooks
- Simple and easy
- ! - seperation of concern
- ! - difficult to unit test

### Connect API
- wraps presentational components 
- easy to unit test
- ! - wrapping

*project repo not working. Can't install dependencies due to dependency error*
https://github.com/stevekinney/tip-calculator

## Lesson: mapStateToProps & Connect API
```js
const mapDispatchToProps = {
    updateTip // action
};

export const TipSelectContainer = connect(
    mapStateTOProps,
    mapDispatchToProps
)(TipSelect);
```

## Lesson: Redux Toolkit & State Slice
Transcript:
```txt
So we've made a bunch of allusions to a tool called Redux Toolkit,which, again, sits on top of Redux.It's clearly not in every code bases predated and it all depends.If you're kind of walking along a very common path,it provides a whole bunch of useful abstractions.If you've got a very large and complicated code base, it might not be the right fit.But I think there's two things.One, I think for a lot of especially newer applications, smaller applications,it's absolutely the right fit.And two, there are ideas that you can take from Redux Toolkit andbegin to think about and apply in your code base even if Redux Toolkitis maybe not the best fit or it's just too hard to totally transition to.I think there are ideas that you can borrow and inspiration you can learn forhow you can create abstractions on top of Redux.So let's take a look.This is kinda shows you what it's trying to bring to the table,which is taking a lot of the boilerplate.I think Erick asked me at one point, does this ever become second nature?And it does, but that feeling of one of the complaints on Redux all the timeis there's a lot of boilerplate.And we were talking about this a little bit during the break, butit all kinda depends, right?If this is a small app or something very kind of that's limited in scope,I don't even know if Redux is the right choice.But if you also think that, hey, this is gonna be a very large app we're gonnamaintain over a really long period of time.Then kind of spending a little bit of time configuring andsetting up the foundation with Redux might make sense.It's always definitely like most things.It was like you should always use it all the time.It would have just been built-in, right?A lot of these become choices that we need to make, orthis is also usually in case you're moving into a code base.So what it seeks to do is kind of tie up our actions, our action creators,our reducers all into one kind of extraction called a slice.Even wires up the DevTools andMiddleware just out of the box kinda gets all of that set up for us.So what we're gonna do is we're gonna just takea tour of the Create React App template.You just see it at a high level, and then we'll actually implement it inan application as well that can now actually see all the moving pieces.So at first, what I kinda want you to do is just kind of take it all in andget the highlight.You don't have to memorize everything as we go through it.We're just trying to get a lay of the land, andthen we'll get a little bit more into it as time goes on.So if we look here, you can see that the demo app is, again, yeah,who doesn't love a good counter for demoing managing state?So you can see we can increment it and decrement it.We can change the amount as well and add the amount in,very similar to what we all built as a team.Earlier, you can add only if odd,which because I'm adding 400 will always be the same, so on and so forth.Cool, so let's actually just look at how this application islaid out to see what we can learn about Redux Toolkit.Redux Toolkit, like in the template, has this idea of a store.js,and then it's dividing stuff into folders called features.You think about before we had our items and our tip percentage before.This is all you get to choose the folder structure.If you don't like this folder structure, you don't have to use it.I think it all depends, again, for simple applications,you might just have everything in very clean place like that.But you can see that there's even the counter component with the state.In a large application, you can see how many different things might revivemultiple pieces and it gets a little bit tricky.It really depends on the nature of what you're building.But the major thing for us to look at is this counter slice.You can think about a slice as just bundling a lot of the ceremonythat we were doing around.Okay, we're gonna make the action type constants.And we are gonna go ahead and we're going to create maybe action creators.And we're gonna make the reducers.And we're going to all these different pieces.So you can see here's basically what a slice looks like.You give it a name, in this case, it's the counter, right?We might have had menu items, or counter, or whatever.The initial state, which is something we've seen before, in this case,it is value 0 and status equals idle.We'll talk a little about that in a second.And then the reducers, you can see that here we've got keys,which is increment, decrement, increment by amount,very similar to what we had before, and it's mutating the state.All right, pop quiz, sports fans, what library is usingjust willy nilly modify the state without telling us?>> Immer? >> Immer, yeah,which it's abstracting that and hiding that.So if you started with Redux Toolkit and then had to jump into a code base thatdidn't have Redux Toolkit, you might be like, yeah, I can just mutate state.I did that before, right?It's actually all of these methods are going through Immer under the hood, whichallows us to kind of mutate the state as we need to and it's handling that for us.But again, abstraction is great until you don't really know what it's doing, andthen it becomes a little bit tricky.And what's interesting, we're not doing a lot of the pieces wherewe're matching action type equals a certain constant.Because what's happening is it's making action types based on the keys inthe reducer that we can then use throughout the application.If we look at counter.js you can see that it's increment, decrement.It's actually getting all of those from the counter slice itself.So it's making the actions on our behalf.It's storing the action types.It's kinda hiding most of the inner workings away from us,which is really great because it saves us from having to do all that tedium.On the other hand, it is also hiding a lot of the inner workings away from us.So whether or not it's right for you is absolutely a trade-off.But everything is contained in these slices.It is trying to kinda wire up as much of it as possible.So we'll look at setting up a reducer, using the actions, andthis extra reducer thing, we'll also take a look at as well.And you can see this counterSlice.actions is where all the actions are stored fromas well.You can see that it's using selectors.All the concepts that we've learned so far were leading up to this moment,where we could see it all kinda tied together.
```

## Lesson: Creating a Slice of State
Normal one from redux:
```js
import { createStore } from 'redux';

export const store = createStore(
  (state = { humans: [], tasks: [] }, action) => state
);
```

Instead of using Redux directly, we'll use Redux toolkit to most of what we need
- configureStore()
    - abstraction that takes some opstions and return a fully configured store
    - automatically apply a few middlewares for us
    - 1. middleware that checks if ur mutating state
    - 2. middleware that makes sure we say that u can export an import serialized version of json
    - 3. Allow dispatch functions to make AJAX calls
    - Also wires up the redux dev tool
    - *does everything under the hood*
```js
import { configureStore } from "@reduxjs/toolkit";

export const store = configureStore({
  reducer: (state) => state
});
```

## Lesson: Async Thunks with React Toolkit
- Simple Needs -> Use Redux Thunks
- Really sophisticated things -> Redux-Saga, Redux-Observable

Thunk Middleware
- way too simple, but u get the point
```js
export const middleware = (store) => (next) => (action) => {
    if (typeof action === 'function'){
        const fn = action;
        return fn(store.dispatch);
    }

    return next(action);
}

```