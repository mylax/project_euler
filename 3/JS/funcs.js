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
    var primes = find_primes(Math.ceil(Math.sqrt(n)));
    var biggestfactor = null;
    for(let [i, prime] of primes.entries()) {
        if(n % prime === 0) {
            biggestfactor = prime;
        }
    }
    if(biggestfactor === null){
        return n;
    }
    return biggestfactor;
}
