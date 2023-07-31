/**
 * Given an integer x, return true if x is a palindrome, and false otherwise.
 */

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let value = x.toString();

    for (let i = 0; i < value.length / 2; i++) {
        if (value[i] !== value[value.length - i - 1]) {
            return false;
        }
    }
    
    return true;
};