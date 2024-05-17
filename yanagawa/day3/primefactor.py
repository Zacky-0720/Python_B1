import sys

args = sys.argv

num = int(args[1])

primes = []
i = 2

while num > 1:
    if num % i == 0:
        primes.append(i)
        num /= i
    else:
        i += 1

print(primes, end="")
