# Ultimate Guide to Redux - Educative

# 1 - Introduction to Redux
## 1.1. - What is Flux?
Redux is an excellent Flux implementation. In less than half a year, the library became the go-to framework for React developers.

The official definition of Redux is “a predictable state container for JavaScript applications”. This means that all of your application states will be stored in one place so that you may query the state at any given point in time.

### Flux
Flux is a generic architecture or pattern rather than a specific implementation. Flux was touted as redefining the previous ideas of MVC (Model–View–Controller) and MVVM (Model–View–ViewModel) patterns and two-way data binding introduced by other frameworks by suggesting a new flow of events on the front end, called the unidirectional data flow.

**Undirectional Flow**
Action -> Dispatch -> Store -> Controller View -> Component View -> (back to Action)

In Flux, events are managed one at a time in a circular flow with several actors: dispatcher, stores, and actions.

- An action is a structure that describes any change in the system: mouse clicks, timeout events, etc.
- Actions are sent to a dispatcher. A dispatcher is a single point in the system where anyone can submit an action for handling.
- Stores hold parts of the application state for maintenance and react to commands from the dispatcher.

UI --[Action]--> Dispatch --[Action]--> Stores --[Change Notification]--> (back to UI)

Here is the simplest Flux flow:
1. Stores subscribe to a subset of actions.
2. An action is sent to the dispatcher.
3. The dispatcher notifies subscribed stores of the action.
4. Stores update their state based on the action.
5. The view updates according to the new state in the stores.
6. The next action can then be processed.

This flow ensures that it’s easy to reason about how actions flow in the system, what will cause the state to change, and how it will change.

### Flux as a library
Facebook’s developers did not initially open-source their implementation of Flux but instead released only parts of it, like the dispatcher. The JavaScript community immediately began to utilize the concept of the Flux Flow. This caused many different open-source implementations to be built and released in quick succession.

Some of the new Flux libraries followed the basic Flux pattern very closely, while others differed significantly from the original patterns.

## 1.2 - Redux and Flux
While Redux derives from Flux concepts, there are a few distinctions between the two architectures.

In contrast to Flux, Redux only has a single store that holds no logic by itself. The store dispatches and handles Actions directly, eliminating the need for a standalone dispatcher. In turn, the store passes the actions to state-changing functions called reducers.

### Application data
While many other frameworks divide the data between different services and areas, in Redux, we keep all our data in a central repository accessible by all parts of the UI.

### Changing the data
Since all of our data is sitting in a single JavaScript object, there has to be a way to modify it in a clear and consistent fashion. But allowing various places in our code to access and modify our central repository directly will make it very hard to track changes and update the UI correctly.

In Redux, sending an action initiates all changes to the store. This action is a plain JavaScript object containing all the information describing the required change. The action is dispatched to our store, which calculates the new state according to the action.

Since the store is a generic implementation, in Redux, we use reducers to calculate what our current state will look like when an action is applied.

### Updating the UI
Each UI framework using Redux (React, Angular, etc.) is responsible for subscribing to the store to listen to its “store updated” events and updating the UI accordingly.

The core concept of Redux is that our UI always reflects the state of the application in the store. Sending an action will cause our store to use our reducers to calculate a new state and notify the UI layer to update the UI accordingly.

### Advanced flows
Other parts of Redux make the application easier to build and manage, like the middleware. Every action gets passed through a pipeline of middleware. Unlike reducers, middleware can modify, stop, or add more actions.

Examples might include logging middleware, an authorization middleware that checks if the user has the necessary permissions to run the action.

## 1.3 - Redux Terminology

### Actions and action creators
The only way for an application to change its state is by processing actions.

In most cases, actions in Redux are nothing more than plain JavaScript objects passed to the store that holds all the information needed for the store to be able to modify the state:
```js
{
  type: 'INCREMENT',
  payload: {
    counterId: 'main',
    amount: -10
  }
}
```
These objects are commonly wrapped in a function that can generate the objects based on a parameter because they often contain logic that can be used in multiple places in an application:
```js
function incrementAction(counterId, amount) {
  return {
    type: 'INCREMENT',
    payload: {
      counterId,
      amount
    }
  };
};
```
### Reducer
When a store receives an action, the store must figure out how to change the state accordingly. To do so, it calls a function, passing it the current state and the received action:
```js
function calculateNextState(currentState, action) {
  ...
  return nextState;
}
```
This function is called a reducer. In real Redux applications, there will be one root reducer function that will call additional reducer functions to calculate the nested state:
```js
function rootReducer(state, action) {
  switch (action.type) {

    case 'INCREMENT':
      return Object.assign({}, state, {
        counter: state.counter + action.payload.amount
      });

    default:
      return state;
  }
}
```
This sample reducer copies the original state into a new JavaScript object and overwrites the counter key with an updated value. The reducer does not change the original state parameter passed to it, keeping it immutable.

Note: Reducers never modify the original state; they always create a new copy with the needed modifications.

### Middleware
Middleware are the most powerful and versatile entities in Redux because they have has access to the actions, the dispatch() function, and the store. Middleware acts like interceptors for actions. Before reaching the store, middleware can modify, create, and suppress actions.

### Store
Unlike many other Flux implementations, Redux has a single store that holds the application information but no user logic. The role of the store is to receive actions, pass them through all the registered middleware, and then use reducers to calculate a new state and save it.

When a shift in the state is made, the store will receive an action and in turn notify all registered listeners of the change. This allows various parts of the system, like the UI, to update themselves according to the new state.

## 1.4 - General Concepts
Redux is all about functional programming and pure functions. Understanding these concepts is crucial to understanding the underlying principles of Redux.

Functional programming centers around avoiding changing state and mutable data—in other words, making your code predictable and free of side effects.

JavaScript allows you to write code in a functional style, as it treats functions as first-class objects. However, JavaScript was not designed to be a functional programming language, so there are some caveats that you will need to keep in mind.

### Pure and impure functions#
A pure function returns values by using only its arguments: it uses no additional data, changes no data structures, touches no storage, and emits no external events (like network calls). This means that you can be completely sure that you will always get the same result every time you call the function with the same arguments. Here is an example of pure functions:
```js
function square(x) {
  return x * x;
}
y = square(4)
console.log("The square of 4 is", y)
```
If a function uses any variables not passed in as arguments or creates side effects, the function is impure. When a function depends on variables or functions outside of its lexical scope, you can never be sure that the function will behave the same every time it’s called. For example, the following is an impure function:
```js
function rand() {
  return Math.random();
}
y = rand()
console.log("Random number is", y)
```
### Mutating Objects
Another important concept that often causes headaches for developers starting to work with Redux is immutability. JavaScript has limited tooling for managing immutable objects, and we are often required to use external libraries.

Immutability means that something can’t be changed, guaranteeing developers that it will have the same properties and values forever if you create an object. For example, let’s declare a simple object as a constant:
```js
const colors = {
  red: '#FF0000',
  green: '#00FF00',
  blue: '#0000FF'
};

console.log("Previous Value ", colors);

colors.red = '#FFFFFF';
console.log("New Value ", colors);
```
Even though the colors object is a constant, we can still change its content, as const will only check if the reference to the object has changed. To make the colors object appear immutable, we can use the Object.freeze() method:

The value of the red property will now be '#FFFFFF' since we have already updated the value.
```js
const colors = {
  red: '#FF0000',
  green: '#00FF00',
  blue: '#0000FF'
};

console.log("Previous Value ", colors);

colors.red = '#FFFFFF';
console.log("New Value ", colors);

Object.freeze(colors);

colors.red = '#000000';

console.log("Value after freezing ", colors);
```
Here, once we used Object.freeze(), the colors object became immutable. In practice, things are often more complicated, though. JavaScript does not provide good native ways to make data structures fully immutable. For example, Object.freeze() won’t freeze nested objects:
```js
const orders = {
  bread: {
    price: 10
  },
  milk: {
    price: 20
  }
};

Object.freeze(orders);

orders.milk.price -= 15;

console.log("Price of Milk", orders.milk.price);
```
To work around the nature of our beloved language, we have to use third-party libraries like deep-freeze, seamless-immutable, or Immutable.js.

## 1.5 - Redux and React/Angular
Redux began as a companion to React, but it has started to gather a major following with other frameworks, like Angular. Redux is fully framework-agnostic at its base, and it can easily be used with any JavaScript framework to handle state and changes.

Note: Redux—or its concepts—is also used on the server-side, with implementations in Java, Python, and more. There are even implementations for other platforms, such as ReSwift for iOS.

Third-party libraries provide a set of convenience functions for each framework to connect Redux seamlessly with different frameworks.

# 2 - Basic Redux Implementation
## 2.1 - Basic Structure
People love Redux because of its simplicity. Thus, unlike other frameworks, where the only way to learn is to study the API, we can start by implementing Redux ourselves.

The basic premise behind Redux is the idea that the store saves all the application states in one place. To use this idea in applications, we will need to find a way to:
1. Modify the state as a result of events (user-generated or from the server).
2. Monitor state changes so we can update the UI.

The first part can be split into two blocks of functionality:
- Notify the store that an action has happened.
- Help the store figure out how to modify the state according to our application’s logic.

Using this structure, let’s build a simple application that will implement a counter. Our application will use pure JavaScript and HTML and require no additional libraries in any modern browser.

We will have two buttons that will allow us to increment and decrement a simple counter and a place where we can see the current counter value.

## 2.2 - Creating Functions
To make our demo functional, let’s create a click handler for each button that will use the dispatch() function to notify our store that an action needs to be performed:

We will come back to its implementation later. Also, let’s define a function that will update the counter's value in the HTML based on the application state received as an argument:

Since we want our view to represent the current application state, we need consistent and reliable updates every time the state (and the counter) changes.

We will use the subscribe() function, which we will also implement a bit later. The role of the function will be to call our callback every time anything in the state changes:

## 2.3 - Implementing Reducer
We have now:

- created a basic application structure with a simple state
- implemented a function that will be responsible for updating the HTML based on the state
- defined two functions—dispatch() and subscribe().

But there is still one thing missing. How will our mini-Redux know how to handle the events and change the application state?

For this, we define an additional function. Redux will call our function on each action dispatched, passing it the current state and the action.

To be compliant with Redux’s terminology, we will call the function a reducer. The reducer’s job will be to understand the action and, based on it, create a new state.

An important thing to remember is that reducers must always return a new, modified copy of the state. They shouldn’t mutate the existing state, like in this example:
```js
// This is wrong!
state.counter = state.counter + 1;
```

## 2.4 - Implementing Dispatch
Now it’s time to implement the actual change of the state. Since we are building a generic framework, we will not include the code to increment/decrement the counter but rather will call a function that we expect the user to supply, a function called reducer().

The dispatch() function calls the reducer() implemented by the application creator, passing it both the current state and the action that it received.

We then check if the new state differs from the old one, and if it does, we replace the old state and notify all the listeners of the change:
```js
// dispatch() implementation
let state = null;

function dispatch(action) {
  const newState = reducer(state, action);

  if (newState !== state) {
    state = newState;

    listeners.forEach(listener => listener());
  }
}
```
One remaining task is to notify our view of the state change. We only have a single listener in our example, but we already can implement full listener support by allowing multiple callbacks to register for the state change event. We will implement this by keeping a list of all the registered callbacks:
```js
//subscribe() implementation 

const listeners = [];

function subscribe(callback) {
  listeners.push(callback);
}
```
This might surprise you, but we have just implemented a major part of the Redux framework. The real code isn’t much longer.

## 2.5 - Final Implementation
To complete our example, let’s switch to the real Redux library and see how similar the solution remains.

First, add the Redux library, for now using unpkg:
```js
<script src="https://unpkg.com/redux/dist/redux.js" />
```
We then change our previous state definition to be a constant that only defines the initial value of the state:

```js
const initialState = {
  counter: 3
};
```
Now we can use it to create a Redux store:
```js
const store = Redux.createStore(reducer, initialState);
```
As you can see, we are using our reducer from before. The switch statement is the only change that needs to be made to the reducer. Instead of using just the action: switch (action), we include the mandatory type property, which indicates the type of action being performed:
```js
switch (action.type)
```
The Redux store will also give us all the features we implemented ourselves before, like subscribe() and dispatch(). Thus, we can safely delete these methods.

To subscribe to store changes, we simply call the subscribe() method of the store:
```js
store.subscribe(updateView);
```
subscribe() does not pass the state to the callback, so we need to access it via store.getState():
```js
//Updating view by reading the state from the store

// Function to update view (this might be React or Angular in a real app)
function updateView() {
  document.querySelector('#counter').innerText = store.getState().counter;
}

store.subscribe(updateView);
```
The last change is in the dispatch() method. As mentioned previously, our actions now need to have the type property. Thus, instead of sending the string 'INC' as the action, we now need to send { type: 'INC' }.

Here is what the complete code will look like:

# 3 - Cloning a Redux Boilerplate
## 3.1 - Redux Boilerplate
Modern client-side applications often require the use of some boilerplate to make development easier. The boilerplate may include directory structure, code transformation tools, testing infrastructure, and production pipeline tools.

All the popular frameworks have optional command-line tools to help developers quickly bootstrap their projects with all the required settings. These include Create React App, Vue CLI, or the heavier Angular CLI that offers many more features than just project initiation. All of these settings ease the chore of setting up a new project.

### Setting up on the local environment
For our purposes, we will use a bare-bones boilerplate.

To start things off, we’ll clone the starter project, install the needed packages, and verify that our environment is ready:

Run the following commands:
```bash
git clone git@github.com:redux-book/starter.git
cd starter
npm install
npm start
```
If everything went smoothly, you should be able to access http://localhost:8080 and see a page showing A simple Redux starter and a running counter.

If you open the JavaScript console in the developer tools, you should also see Redux started in the console. The project is ready!

## 3.2 - Skeleton Overview
Let’s take a quick look at all the files included within the starter project. The main file we will be working with is app.js (index.js on our platform), but it is important to get familiar with the directory structure before working on any project. The project files are:

### package.json
While most fields in this file are irrelevant, it is important to note two sections, devDependencies and dependencies.

The devDependencies contains a list of all the tools needed to build the project. It currently includes only Webpack-related packages, which enable us to run our app.

The dependencies section lists all the packages we will bundle with our application. It includes only the redux library itself and jquery to make the DOM manipulation code look nicer.

### webpack.config.js
This is the main Webpack configuration file. This settings file instructs Webpack how to chain transpilation tools and how to build packages and usually holds most of the configuration of the project’s tooling.

In our simple project, there is only one settings file. Our webpack.config.js file defines index.js as the main file, which acts as an entry point to our application and the output destination for the bundled project.

### index.html, index.js
Single-page applications, unlike their server-rendered cousins, have a single entry point.

Every part and page of the application will be rendered in our project starting from index.html, and all the JavaScript-related startup code will be in index.js.

## 3.3 - Setup

# 4 - Complete Redux Project
## 4.1 - Introduction
To illustrate how to use different parts of Redux, we will be building a recipe book application.

It will add recipes and ingredients for each recipe and fetch an initial recipe list from a remote server.

The first step with any Redux-based app is to plan how data will be arranged in the store. Our recipe object will start out holding only the recipe’s name. To store the current list, we can use a regular array: