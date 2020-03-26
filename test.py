def count_primes(num):
    primes = []
    for i in range(2, num+1):
        for prime in primes:
            if i%prime==0:
                break
        else:
            primes.append(i)
    return len(primes)


print(count_primes(100))
