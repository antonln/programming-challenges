def prime_generator(n):
    """
    Generate all prime numbers up to n.
    """
    
    all_primes = [2]

    for j in range(2,n+1):
        k = 0
        for prime in all_primes:
            if j % prime == 0:
                k += 1

        if k == 0:
            all_primes.append(int(j))

    print("Primes are ", all_primes)

prime_generator(int(input("Up to which number do you want to \
generate primes? ")))