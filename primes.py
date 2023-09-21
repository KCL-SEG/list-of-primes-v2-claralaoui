def primes(number_of_primes):
    if number_of_primes < 0:
        raise ValueError(f'The value must be positive, you entered {number_of_primes}')
    list = []
    next_number = 0
    while len(list) < number_of_primes:
        if is_prime(next_number):
            list.append(next_number)
        
        next_number = next_number + 1
    return list
