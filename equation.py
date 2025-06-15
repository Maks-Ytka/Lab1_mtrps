import math
import sys


def solve_quadratic(a, b, c):
    if a == 0:
        print("Error. a cannot be 0")
        sys.exit(1)

    d = b ** 2 - 4 * a * c

    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")

    if d > 0:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print("There are 2 roots")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif d == 0:
        x = -b / (2 * a)
        print("There are 1 roots")
        print(f"x1 = {x}")
    else:
        print("There are 0 roots")


def parse_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            val = input_value = input(prompt)
            print(f"Error. Expected a valid real number, got {val} instead")


def run_interactive():
    a = parse_float_input("a = ")
    while a == 0:
        print("Error. a cannot be 0")
        a = parse_float_input("a = ")
    b = parse_float_input("b = ")
    c = parse_float_input("c = ")

    solve_quadratic(a, b, c)


def run_file_mode(filename):
    try:
        with open(filename, 'r') as f:
            line = f.readline().strip()
            parts = line.split()
            if len(parts) != 3:
                raise ValueError("invalid file format")
            a, b, c = map(float, parts)
            if a == 0:
                print("Error. a cannot be 0")
                sys.exit(1)
            solve_quadratic(a, b, c)
    except FileNotFoundError:
        print(f"file {filename} does not exist")
        sys.exit(1)
    except ValueError as e:
        print(str(e))
        sys.exit(1)


def main():
    if len(sys.argv) == 1:
        run_interactive()
    elif len(sys.argv) == 2:
        run_file_mode(sys.argv[1])
    else:
        print("Usage: python equation.py [file]")


if __name__ == "__main__":
    main()