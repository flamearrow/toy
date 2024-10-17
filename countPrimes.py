# count number of primes from 1 to n using Sieve of Eratosthenes Algorithm
# idea: create a map of [n], mark everything as prime frist
# then starting from 3, if i is prime, all multiples of i are NOT prime
#  when counting mutiples, dont' need i, 2i, 3i..., only need to count from i*i, i*i+i, i*i+2i
#  because 2/3 are alreayd visited
def countPrimes(n: int) -> int:
    if n < 2:
        return 0
    pMap = [1] * n
    pMap[0] = 0
    pMap[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if pMap[i] == 1:  # if this is a prime, all its duplicates are not primes
            # starting from i*i but not i*1/i*2/i*3 because 1/2/3 are already visited
            for j in range(i * i, n, i):
                pMap[j] = 0
    return sum(pMap)