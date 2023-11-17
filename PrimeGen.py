limit = 1000
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    num = 1
    while num <= limit:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def write_to_file(primes, filename):
    with open(filename, 'w') as file:
        for prime in primes:
            file.write(str(prime) + '\n')

prime_numbers = generate_primes(limit)
write_to_file(prime_numbers, 'primes.txt')
