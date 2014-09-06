-- If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
-- The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

problem1 = sumMultiplesOf 3 999 + sumMultiplesOf 5 999 - sumMultiplesOf 15 999

sumMultiplesOf n limit = n * (limit `div` n) * ((limit `div` n) + 1) `div` 2
