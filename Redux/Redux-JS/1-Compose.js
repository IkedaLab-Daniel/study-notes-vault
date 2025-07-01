import {
  compose,
  applyMiddleware,
  bindActionCreators
} from 'redux';

// COMPOSE
// Take a multiple function and compose a new function that takes all those function

const makeLouder = string => string.toUpperCase();
const repeatThreeTimes = string => string.repeat(3);
const embolden = string => string.bold();

// Using nested functions
// const makeLouderRepeatThreeTimesAndEmbolden = string => embolden(repeatThreeTimes((makeLouder(string))))

// Using Redux - Compose
const makeLouderRepeatThreeTimesAndEmbolden = compose(embolden, repeatThreeTimes, makeLouder)

console.log('\n\n\n\n\n\n')
console.log(makeLouderRepeatThreeTimesAndEmbolden('dev.iceice'))