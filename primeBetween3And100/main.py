prime_numbers = []

def is_prime(number):
    is_prime = True
    for divisor in range(2, number - 1):
        if number % divisor == 0:
            is_prime = False
    return is_prime


for number in range(3, 101):
    if is_prime(number):
        prime_numbers.append(number)
print(f'{prime_numbers}')