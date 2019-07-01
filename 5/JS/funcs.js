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


function table(arr) {
    var a = [], b = [], prev;

    arr.sort();
    for ( var i = 0; i < arr.length; i++ ) {
        if ( arr[i] !== prev ) {
            a.push(arr[i]);
            b.push(1);
        } else {
            b[b.length-1]++;
        }
        prev = arr[i];
    }

    return [a, b];
}


/* For each number in from, to find the prime factors and return an array that
finds the maximum number of prime factors
*/
function find_biggest_factor(from, to) {
    var all_factors = {};
    var primes = find_primes(to);
    for(let i = from; i <= to; i++){
        var factors = [];
        var filler = i;
        for(let k = 0; primes[k] <= filler; k++) {
            while(filler % primes[k] === 0 && i >= primes[k]) {
                factors.push(primes[k]);
                filler = filler / primes[k];
            }
        }
        listed_prime_factors = table(factors);
        for (g in listed_prime_factors[0]) {
            prime = listed_prime_factors[0][g];
            prime_count = listed_prime_factors[1][g];
            if (all_factors[prime] === undefined || all_factors[prime] < prime_count ) {
                all_factors[prime] = prime_count;
            }
        }
    }
    return all_factors;
}


/*2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?*/

function getSmallestNumberDividable(upperEnd) {
    var res = 1;
    while (true) {
      var checkDi = true;
      for (var i = 1; i <= upperEnd; i++) {
        if (res % i !== 0) {
          checkDi = false;
          break;
        }
      }
      if (!!checkDi) return res;
      res++;
    }
  }