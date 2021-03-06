/* Create a TABLE with all primes up to limit n */
/* Fill a table with all uneven numbers and two up to limit n */
CREATE OR REPLACE FUNCTION fill_primes_table (n int)
    RETURNS void
    AS $$
BEGIN
    INSERT INTO primes
    SELECT
        generate_series AS prime
    FROM (
        SELECT
            generate_series(2, n)) i
WHERE
    generate_series % 2 != 0
    OR generate_series = 2;
END;
$$
LANGUAGE plpgsql;

/* Remove all numbers in table that are multiples of numbers that came before
in the same table */
CREATE OR REPLACE FUNCTION clean_primes_table ()
    RETURNS void
    AS $$
DECLARE
    counter_prime int := 2;
    n int;
BEGIN
    SELECT
        prime + 1
    FROM
        primes
    ORDER BY
        prime DESC
    LIMIT 1 INTO n;
    WHILE counter_prime <= CEILING(sqrt(n))
    LOOP
        DELETE FROM primes
        WHERE prime % counter_prime = 0
            AND prime >= counter_prime * counter_prime;
        SELECT
            prime
        FROM
            primes
        WHERE
            prime > counter_prime
        LIMIT 1 INTO counter_prime;
    END LOOP;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION find_factors (n bigint)
    RETURNS bigint
    AS $$
DECLARE
    counter_prime int := 2;
    biggest_factor int;
BEGIN
    WHILE counter_prime <= CEILING(sqrt(n))
    LOOP
        IF n % counter_prime = 0 THEN
        SELECT counter_prime INTO biggest_factor;
        END IF;
        SELECT
            prime
        FROM
            primes
        WHERE
            prime > counter_prime
        ORDER BY
            prime ASC
        LIMIT 1 INTO counter_prime;
    END LOOP;
    IF biggest_factor IS NULL THEN RETURN n; END IF;
    RETURN biggest_factor;
END;
$$
LANGUAGE plpgsql;
