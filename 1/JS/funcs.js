function find_multiples(k, n) {
  multiples = [];
  for (let divisor of k) {
    for (let i = divisor; i < n; i += divisor) {
      multiples.push(i);
    }
  }
  return [...new Set(multiples)].sort();
};


function arraysEqual(a, b) {
  if (a === b) return true;
  if (a == null || b == null) return false;
  if (a.length != b.length) return false;

  for (var i = 0; i < a.length; ++i) {
    if (a[i] !== b[i]) return false;
  }
  return true;
};