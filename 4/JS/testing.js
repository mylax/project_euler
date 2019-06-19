function arraysEqual(a, b) {
    if (a === b) return true;
    if (a == null || b == null) return false;
    if (a.length != b.length) return false;

    for (var i = 0; i < a.length; ++i) {
      if (a[i] !== b[i]) return false;
    }
    return true;
  };


QUnit.test("reverse ten, should be one? its a feature not a bug", function (assert) {
    assert.ok(arraysEqual(reverse(10), 1), "Passed!");
});

QUnit.test("reverse 101", function (assert) {
    assert.ok(arraysEqual(reverse(101), 101), "Passed!");
});

QUnit.test("biggest palindrom up to ten and ten is 9", function (assert) {
    assert.ok(arraysEqual(palindromic(10, 10)["prod"], 9), "Passed!");
});

QUnit.test("biggest palindrom up to 11 and ten is 99", function (assert) {
    assert.ok(arraysEqual(palindromic(11, 10)["prod"], 99), "Passed!");
});
