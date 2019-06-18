function arraysEqual(a, b) {
    if (a === b) return true;
    if (a == null || b == null) return false;
    if (a.length != b.length) return false;

    for (var i = 0; i < a.length; ++i) {
      if (a[i] !== b[i]) return false;
    }
    return true;
  };


QUnit.test("primes up to ten", function (assert) {
    assert.ok(arraysEqual(find_primes(10), [2, 3, 5, 7]), "Passed!");
});


QUnit.test("primes up to 7", function (assert) {
    assert.ok(arraysEqual(find_primes(7), [2, 3, 5, 7]), "Passed!");
});


QUnit.test("primes up to 1", function (assert) {
    assert.ok(arraysEqual(find_primes(1), []), "Passed!");
});

QUnit.test("primes up to 20", function (assert) {
    assert.ok(arraysEqual(find_primes(20), [2, 3, 5, 7, 11, 13, 17, 19]), "Passed!");
});





QUnit.test("biggest prime factor of 10", function (assert) {
    assert.ok(arraysEqual(find_biggest_factor(10), 5), "Passed!");
});


QUnit.test("biggest prime factor of 100", function (assert) {
    assert.ok(arraysEqual(find_biggest_factor(100), 5), "Passed!");
});



QUnit.test("biggest prime factor of 7", function (assert) {
    assert.ok(arraysEqual(find_biggest_factor(7), 7), "Passed!");
});
