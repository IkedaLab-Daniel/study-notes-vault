/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function(timeSeries, duration) {
    let poison_duration = 0

    if (timeSeries.length == 1) {
        return duration
    }

    for (let i = 1; i <= timeSeries.length - 1; i++) {
        let between = timeSeries[i] - timeSeries[i - 1]
        
        if (between >= duration) {
            poison_duration += duration
        } else {
            poison_duration += between
        }
    }

    poison_duration += duration

    return poison_duration
};

console.log(findPoisonedDuration([1,4], 2))