exports.find_multiples =  function find_multiples(k, n) {
  multiples = [];
  for (let divisor of k) {
    for (let i = divisor; i < n; i += divisor) {
      multiples.push(i);
    }
  }
  return [...new Set(multiples)].sort();
};