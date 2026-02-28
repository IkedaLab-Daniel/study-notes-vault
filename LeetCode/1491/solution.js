/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
    const highest = Math.max(...salary);
    const lowest = Math.min(...salary);

    const total = salary.reduce((a, c) => a + c, 0);
    const reduced = total - highest - lowest;

    const average = reduced / (salary.length - 2);

    return average;
};

console.log(average([1000,2000,3000]))