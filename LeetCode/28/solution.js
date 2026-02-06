/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    const needle_start = needle[0];

    for (let i = 0; i < haystack.length; i++) {
        if (needle_start == haystack[i]) {
            let haystack_slice = (haystack.slice(i, (i + haystack.length)))
            if (needle == haystack.slice(i, (i + haystack.length))) {
                return i;
            }
        }
    }

    return -1;
};

const ICE = strStr("sadbutsad", "sad");
console.log(ICE)