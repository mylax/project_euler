function fibonacci(limit) {
    var i = 0;
    var j = 1;
    result = [];
    while (i <= limit) {
        result.push(i);
        i = j;
        j = result[result.length - 1] + j;
    }
    return result;
}

function sum_even_fibonacci(limit) {
    var fibo = fibonacci(limit);
    result = [];
    for (i=0; i <= fibo.length - 1; i++) {
        if (fibo[i] % 2 === 0) {
            result.push(fibo[i]);
        }
    }
    return result.reduce((sum, value) => sum + value)
}