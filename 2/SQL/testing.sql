SELECT fibonacci (10) = ARRAY[0, 1, 1, 2, 3, 5, 8];
SELECT fibonacci (0) = ARRAY[0];
SELECT fibonacci (8) = ARRAY[0, 1, 1, 2, 3, 5, 8];
SELECT fibonacci (7) = ARRAY[0, 1, 1, 2, 3, 5];


SELECT fibonacci_sum_even (10) = 10;
SELECT fibonacci_sum_even (20) = 10;
SELECT fibonacci_sum_even (0) = 0;