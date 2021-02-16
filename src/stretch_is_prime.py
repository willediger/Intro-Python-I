# 3. Write a program to determine if a number, given on the command line, is prime.

#    1. How can you optimize this program?
#    2. Implement [The Sieve of
#       Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), one
#       of the oldest algorithms known (ca. 200 BC).

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,int((n+1)**0.5)+1):
        if n % i == 0:
            return False
    return True

assert is_prime(113) == True, "113 is prime"
assert is_prime(114) == False, "114 is not prime"

def return_primes(sieve_results):
    # returns list of primes from list of T/F for prime = true whose indices are offset by -2 compared to number
    # ie [True, True, False, True] should return a list of [2, 3, 5]
    return [idx+2 for (idx, val) in enumerate(sieve_results) if val]

def sieve(n):
    #list of "True" from 2 to n, which will be turned to False if not prime
    primes = [True for e in range(2,n+1)] 
    p = 2
    while p <= int((n+1)**0.5):
        if primes[p-2]:
            for p_mults in range(2*p, n+1, p):
                primes[p_mults-2] = False
        p+=1
    return return_primes(primes)

print(sieve(120))

