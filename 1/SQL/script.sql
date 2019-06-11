CREATE OR REPLACE FUNCTION test3 (k int[], n int)
  RETURNS bigint
  AS $$
  SELECT
    SUM(a)
  FROM ( SELECT DISTINCT
      generate_series(unnest(k), n - 1, unnest(k)) as a) as s;
$$
LANGUAGE SQL;

SELECT
  test3 (ARRAY[5, 3],
    1000);
