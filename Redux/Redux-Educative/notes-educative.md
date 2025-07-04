# Ultimate Guide to Redux - Educative

## Introduction to Redux
### What is Flux?
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