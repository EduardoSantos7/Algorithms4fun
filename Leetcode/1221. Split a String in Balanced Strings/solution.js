/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    let count = 0;
    let res = 0;

    for (let i = 0; i < s.length; i++) {
        count += s[i] == "R" ? 1 : -1;
        if (count == 0) {
            res++;
        }
    }

    return res;
};