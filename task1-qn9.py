'Given a list of integers, write a function to return a new list containing only the prime numbers from the original list'

def get_primes(num):
    primes = []
    for n in num:
        if n < 2:
            continue
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            primes.append(n)
    return primes
l=[1,2,3,4,5,6,7,8,9,997,47,37]
print(get_primes(l))
