CREATE TABLE crossproducts (
    n1 int,
    n2 int,
    prod bigint
);
INSERT INTO crossproducts
SELECT n1, n2 , prod FROM (
SELECT
    n1,
    n2,
    n1 * n2 AS prod
FROM (
    SELECT * FROM generate_series(1, 999) AS n1 CROSS JOIN
        generate_series(1, 999) AS n2

) i ) k
WHERE prod = reverse(prod);

SELECT n1, n2, prod FROM crossproducts WHERE prod = (SELECT MAX(prod) FROM crossproducts);