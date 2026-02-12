/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    const new_arr = s.split(" ")

    for (let i = new_arr.length ; i >= 0; i--) {
        if (new_arr[i] == '') {
            continue
        }
        
        last_item = new_arr[i].split(" ")
        return last_item.length
    }
};

console.log(lengthOfLastWord("Hello World"))