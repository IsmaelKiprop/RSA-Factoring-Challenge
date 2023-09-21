#!/usr/bin/env python3

import sys

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def factorize_to_primes(number):
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i) and is_prime(number // i):
            return i, number // i

def main():
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        return

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            for line in file:
                number = int(line.strip())
                p, q = factorize_to_primes(number)
                print(f"{number}={p}*{q}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Invalid input in the file.")

if __name__ == "__main__":
    main()
