def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

number = 31
x = 300
while is_prime(number):
    number += x
    x *= 10
print(number)
