const funcs = require('./funcs.js');

var sum = funcs.find_multiples([3, 5], 1000).reduce((partial_sum, a) => partial_sum + a, 0); 
console.log(sum);