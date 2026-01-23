# sample_pylint_test.py - Save this file and run: pylint sample_pylint_test.py

import sys  # unused import - C0411

def calculate(a, b,     c):  # too many args R0913, invalid spacing E251
    """
    Missing docstring details.
    """
    x = a + b  # redefined-loop-variable if in loop, but here unused-variable W0612
    print(x * c)  # ok
    return x  # inconsistent-return-statements if no error path

def main():
    calculate(1, 2, 3, 4)  # too many positional args E1120
    my_list = [1,2,3,4,5,6,7,8,9,10,11]  # too-many-branches if complex, line-too-long C0301
    for i in my_list:
        if i % 2 == 0:
            print("even")
        else:
            print("odd")
            continue  # ok but demo

if __name__ == "__main__":
    main()
