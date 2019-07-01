var primes_factors = find_biggest_factor(1, 30);
var prod_primes = 1;

for (key in primes_factors) {
    prod_primes = prod_primes * Math.pow(key, primes_factors[key]);
}

console.log(prod_primes);




// console.log(getSmallestNumberDividable(21));