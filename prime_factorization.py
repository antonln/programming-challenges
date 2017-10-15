def prime_factors(n):
    """
    Find all prime factors of inputted number.
    """

    all_primes = [2]
    p_factors = []

    for j in range(2,n+1):
        k = 0
        for prime in all_primes:
            if j % prime == 0:
                k += 1

        if k == 0:
            all_primes.append(int(j))

    # print("Logged primes are ", all_primes)

    remainder = n

    while remainder not in all_primes:
        for prime in all_primes:
            if remainder % prime == 0:
                remainder = remainder / prime
                p_factors.append(prime)
                break

    else:
        if remainder in all_primes:
            p_factors.append(int(remainder))
        print("The prime factors are: ", p_factors)

    check = 1

    for i in p_factors:
        check = check * i

    print("Check: ", check)

prime_factors(int(input("Choose a number to find its prime factors: ")))
