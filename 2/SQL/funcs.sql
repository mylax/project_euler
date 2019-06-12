CREATE OR REPLACE FUNCTION fibonacci (n INTEGER)
    RETURNS int[]
    AS $$
DECLARE
    result int[];
    i integer := 0;
    j integer := 1;
BEGIN
    WHILE i <= $1 LOOP
        SELECT
            array_append(result, i) INTO result;
        SELECT
            i + j,
            j INTO j,
            i;
    END LOOP;
    RETURN result;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION fibonacci_sum_even (n int)
    RETURNS int
    AS $$
DECLARE
    result int;
BEGIN
    SELECT
        sum(x)
    FROM (
        SELECT
            x
        FROM
            unnest(fibonacci (n)) AS x
        WHERE
            x % 2 = 0) AS i INTO result;
    RETURN result;
END;
$$
LANGUAGE plpgsql;
