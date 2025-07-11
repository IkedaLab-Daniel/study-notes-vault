// > constants
export const INCREMENT = 'INCREMENT';
export const DECREMENT = 'DECREMENT';
export const SET = 'SET'

// > actions
export const increment = () => ({ type: INCREMENT });
export const decrement = () => ({ type: DECREMENT });
export const set = (value) => ({ type: SET, payload: value });