def water_plants(plant_list: list[str]) -> None:
    """
    Simulates watering a list of plants.

    Parameters
    ----------
    plant_list : list
        A list of plant names to be watered. Items should be strings.
        If a non-string value is encountered, a TypeError may occur.

    Behavior
    --------
    - Prints each plant as it is watered.
    - Catches TypeError if an invalid plant (like None or a number)
    is processed.
    - Executes a `finally` block to close the watering system.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


"""
Function to test the finally block
"""


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    list = ["tomato", "lettuce", "carrots"]
    water_plants(list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    list2 = ["tomato", None]
    water_plants(list2)
    print()
    print("Cleanup always happens, even with errors!")


test_watering_system()
