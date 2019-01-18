/** 
Given a 32 - bit signed integer, reverse digits of an integer.
*/

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
    var MAX_INT = 2 ** 31 - 1; // Max input size is a 32 bit integer
    var MIN_INT = -MAX_INT;
    if (x < 0) {
        rev = Number(String(x * -1).split('').reverse().join('')) * -1;
    } else {
        rev = Number(String(x).split('').reverse().join(''));
    }
    if (rev > MAX_INT || rev < MIN_INT) {
        return 0;
    } else {
        return rev;
    }
};