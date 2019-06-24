function find_primes(limit) {
    var sieve = [];
    var primes = [];

    for (let i = 0; i <= limit; i++) {
        sieve.push(true);
    }
    sieve[0] = sieve[1] = false;

    for (let [i, isprime] of sieve.entries()) {
        if(isprime) {
            primes.push(i);
            if(i <= Math.ceil(Math.sqrt(limit))) {
                for(let k = i * i; k <= limit; k += i) {
                    sieve[k] = false;
                };
            };
        }
    }
    return primes;
};


function find_biggest_factor(n) {
    var all_factors = [];
    var factors = [];
    var primes = find_primes(Math.ceil(Math.sqrt(n)));
    for(let i = 1; i <= 20; i++){
        for(k in primes) {
            while(n % primes[k] === 0) {
                factors.push(primes[k]);
                n = n / primes[k];
            }

        }
    }
    return factors;
}
