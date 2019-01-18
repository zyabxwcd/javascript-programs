/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var MAX_INT = 2**31 -1; // Max input size is a 32 bit integer
    var MIN_INT = -MAX_INT;
    if (x < 0) {
        reversed = Number(String(x*-1).split('').reverse().join(''))*-1;
    } else {
        reversed = Number(String(x).split('').reverse().join(''));
    }
    if (reversed > MAX_INT || reversed < MIN_INT) {
        return 0;
    } else {
      return reversed;  
    }
};