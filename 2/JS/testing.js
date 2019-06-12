function arraysEqual(a, b) {
    if (a === b) return true;
    if (a == null || b == null) return false;
    if (a.length != b.length) return false;

    for (var i = 0; i < a.length; ++i) {
      if (a[i] !== b[i]) return false;
    }
    return true;
  };


QUnit.test("fibonacci up to ten", function (assert) {
    assert.ok(arraysEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8]), "Passed!");
});


QUnit.test("fibonacci up to 8", function (assert) {
    assert.ok(arraysEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8]), "Passed!");
});


QUnit.test("fibonacci up to 7", function (assert) {
    assert.ok(arraysEqual(fibonacci(7), [0, 1, 1, 2, 3, 5]), "Passed!");
});

QUnit.test("fibonacci up to 0", function (assert) {
    assert.ok(arraysEqual(fibonacci(0), [0]), "Passed!");
});

QUnit.test("sum even fibonacci up to 0", function (assert) {
    assert.ok(arraysEqual(sum_even_fibonacci(0), 0), "Passed!");
});


QUnit.test("sum even fibonacci up to 10", function (assert) {
    assert.ok(arraysEqual(sum_even_fibonacci(10), 10), "Passed!");
});

QUnit.test("sum even fibonacci up to 20", function (assert) {
    assert.ok(arraysEqual(sum_even_fibonacci(20), 10), "Passed!");
});
