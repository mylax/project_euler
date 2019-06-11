CREATE OR REPLACE FUNCTION sum_multiples (k int[], n int)
  RETURNS bigint
  AS $$
  SELECT
    SUM(a)
  FROM ( SELECT DISTINCT
      generate_series(unnest(k), n - 1, unnest(k)) as a) as s;
$$
LANGUAGE SQL;