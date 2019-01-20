/**
 * Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
 */
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    reverse = String(x).split('').reverse().join('');
    return reverse == x;
};