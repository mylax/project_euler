CREATE TABLE primes (
    prime int
);

SELECT
    * FROM fill_primes_table (100);

SELECT
    clean_primes_table ();

SELECT find_factors(100) = 5;
SELECT find_factors(7) = 7;
SELECT find_factors(12) = 3;