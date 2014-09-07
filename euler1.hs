euler1 = sumMultiplesOf 3 999 + sumMultiplesOf 5 999 - sumMultiplesOf 15 999

sumMultiplesOf n limit = n * (limit `div` n) * ((limit `div` n) + 1) `div` 2
