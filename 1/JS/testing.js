QUnit.test("multiples three up to ten", function (assert) {
    assert.ok(arraysEqual(find_multiples([3], 10), [3, 6, 9]), "Passed!");
});


QUnit.test("multiples null up to ten", function (assert) {
    assert.ok(arraysEqual(find_multiples([], 10), []), "Passed!");
});


QUnit.test("multiples 11 up to ten", function (assert) {
    assert.ok(arraysEqual(find_multiples([11], 10), []), "Passed!");
});

QUnit.test("multiples of 3 and 5 of ten", function (assert) {
    assert.ok(arraysEqual(find_multiples([3, 5], 10), [3, 5, 6, 9]), "Passed!");
});
