/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const len_s = s.length;
    const len_t = t.length;

    if (len_s != len_t) {
        return false;
    }

    let sorted_s = s.split("").sort().join("");
    let sorted_t = t.split("").sort().join("");

    for (let i = 0; i < len_s; i++) {
        if (sorted_s[i] != sorted_t[i]) {
            return false;
        }
    }

    return true;
};

console.log(isAnagram("anagram", "nagaram"))