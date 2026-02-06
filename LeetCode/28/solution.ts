function strStr(haystack: string, needle: string): number {
    const needle_start: string = needle[0];

    for (let i = 0; i < haystack.length; i++) {
        if (needle_start === haystack[i]) {
            if (needle === haystack.slice(i, (i + needle.length))) {
                return i;
            }
        }
    };

    return -1;
};

const ICE = strStr("sadbutsad", "sad");
console.log(ICE)