def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(11) == True
assert is_prime(29) == True
assert is_prime(40) == False
