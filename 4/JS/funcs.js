function reverse(n) {
    var reversed = "";
    for (i in String(n)) {
        reversed = String(n)[i].concat(reversed);
    }
    return Number(reversed);
};

function palindromic(n1, n2) {
    var prod;
    var result = 0;
    var biggest_n1;
    var biggest_n2;

    for (let i = 0; i < n1; i++) {
        for (let j = 0; j < n2; j++) {
            prod = i * j;
            if(prod > result && reverse(prod) === prod) {
                result = prod;
                biggest_n1 = i;
                biggest_n2 = j;
            }

        }
    }
    return {"prod": result, "n1":biggest_n1, "n2":biggest_n2}
}
