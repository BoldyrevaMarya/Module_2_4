numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers:
    if number == 1:
        continue
    is_prime = True
    count = 0

    for delitel in range(2, number):
         if number % delitel == 0:
            is_prime = False
            count += 1
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
print(f"{primes=}")
print(f"{not_primes=}")