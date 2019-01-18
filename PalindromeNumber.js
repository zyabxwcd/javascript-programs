/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    reverse = String(x).split('').reverse().join('');
    if(reverse == x) {
        return true;
    } else {
        return false;
    }
};