import sys

def factorize(number):
    p, q = 1, number
    for i in range(2, number + 1):
        if number % i == 0:
            p = i
            q = number // i
            break
    return p, q

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            for line in file:
                number = int(line.strip())
                p, q = factorize(number)
                print(f"{number}={p}*{q}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError:
        print("Error: Invalid input in the file.")

if __name__ == "__main__":
    main()
