def is_prime(n):
    if n == 1:
        return False
    factors = 0
    for i in range(1, n+1):
        if n % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f'The value must be positive, you entered {number_of_primes}')
    list = []
    next_number = 0
    while len(list) < number_of_primes:
        if is_prime(next_number):
            list.append(next_number)
        
        next_number = next_number + 1
    return list
