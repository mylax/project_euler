CREATE TABLE primes (
    prime int
);

CREATE TABLE factors_multiple_numbers (
    prime bigint,
    count bigint
);

CREATE TABLE factors (
    prime bigint
);

CREATE AGGREGATE mul (
    bigint) (
    SFUNC = int8mul,
    STYPE = bigint
);

SELECT
    *
FROM
    fill_primes_table (100000);

SELECT
    clean_primes_table ();

SELECT
    create_all_factors ();

SELECT
    mul (POWER(prime, amount)::bigint) AS powers
FROM (
    SELECT
        prime,
        MAX("count") AS amount
    FROM
        factors_multiple_numbers
    GROUP BY
        prime) g;

