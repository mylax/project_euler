DROP TABLE primes;

CREATE TABLE primes (
    prime int
);

SELECT
    * FROM fill_primes_table (100000);

SELECT
    clean_primes_table ();

SELECT * FROM find_factors(600851475143);
