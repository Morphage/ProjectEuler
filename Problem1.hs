-- If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
-- The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

problem1 = sumMultiplesOf 3 + sumMultiplesOf 5 - sumMultiplesOf 15

sumMultiplesOf n = n * (999 `div` n) * ((999 `div` n) + 1) `div` 2