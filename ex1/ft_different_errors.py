"""
in this exercise, we try to implement different Error types
and catch them, the garden_operations function where we try
to implement errors and send them to the Test function where
we write our code to catch some Errors like:
-ValueError
-ZeroDivisionError
-FileNotFoundError
-KeyError
"""


def garden_operations(task: str) -> None:
    if task == "abc":
        int("abc")
    elif task == "divide_by_zero":
        10 / 0
    elif task == "File_not_Found":
        open("missing.txt")
    elif task == "keyerror":
        a = {"blue": 4, "green": 5}
        print(a["red"])


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        garden_operations("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        garden_operations("divide_by_zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("File_not_Found")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    print("Testing KeyError..")
    try:
        garden_operations("keyerror")
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    print("Testing multiple errors together...")
    try:
        garden_operations("divide_by_zero")
    except (ValueError, KeyError, FileNotFoundError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


test_error_types()
