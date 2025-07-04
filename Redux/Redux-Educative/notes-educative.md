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
