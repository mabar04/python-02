def check_temperature(temp_str: str) -> int | None:
    """
    In this function we check if the value we entered is acceptable or not
    it's handeling the errors that could crash our program and catch them
    for the first try except block we try to see if the varriable entered
    is an int and can be used if not we catch a ValueError (for those who
    think that we need to catch a TypeError because we entered a string
    instead of int it;s not the case because the int accepts string the
    int is the one that converts it so in both cases we did enter
    a string and we try to convert it so if's it an int it's correct else
    it's a ValueError)
    """
    try:
        x = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    """
    Now we try to raise an Error writing by as,what raise means is to create
    an object from the Error class that stored ours and throw it
    """
    if x < 0:
        raise ValueError(f"Error: {x}°C is too cold for plants (min 0°C)")
    elif x > 40:
        raise ValueError(f"Error: {x}°C is too hot for plants (max 40°C)")
    print(f"Temperature {x}°C is perfect for plants!")
    return x


"""
in this function,we try to test our error handeling function t osee if
it's working,first we try a normal tamperature nothing happens,
testing with 'abc' it will be handeled as an Error in the first function
In the other tests we need to catch the raised error for stopping
the program from crashing
"""


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    print("Testing temperature: 25")
    check_temperature("25")
    print()
    print("Testing temperature: abc")
    check_temperature("abc")
    print()
    print("Testing temperature: 100")
    try:
        check_temperature("100")
    except ValueError as e:
        print(e)
    print()
    print("Testing temperature: -50")
    try:
        check_temperature("-50")
    except ValueError as e:
        print(e)
    print()
    print("All tests completed - program didn't crash!")


test_temperature_input()
