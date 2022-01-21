def isprime(n):
    if n < 2:
        return False
    if n == 2 :
        return True
    else:
        for i in range(2, int(n**(1/2))+1):
            if 0 == n % i:
                return False
    return True
            