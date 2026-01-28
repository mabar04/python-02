def check_plant_health(plant_name: str, water_level: int | float,
                       sunlight_hours: int | float) -> None:
    """
    Check if a plant's health parameters fall within valid ranges.

    Parameters
    ----------
    plant_name : str
        Name of the plant. Must not be empty.
    water_level : int or float
        Water level from 1 to 10.
    sunlight_hours : int or float
        Sunlight exposure in hours, from 2 to 12.

    Raises
    ------
    ValueError
        If plant name is empty or if any parameter is outside valid ranges.
    """
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         f" is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         f" is too high (max 12)")
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level}"
                         f" is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level}"
                         f" is too low (min 1)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """
    Test the plant health checker with both valid and invalid input values.

    Behavior
    --------
    - Runs a correct/valid case.
    - Tests cases that trigger ValueError due to:
      * empty plant name
      * invalid water level
      * invalid sunlight hours
    - Shows correct exception raising behavior.
    """
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        check_plant_health("tomato", 2.5, 3)
    except ValueError as e:
        print(e)
    print()
    print("Testing empty plant name...")
    try:
        check_plant_health("", 2, 3)
    except ValueError as e:
        print(e)
    print()
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 3)
    except ValueError as e:
        print(e)
    print()
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 10, 0)
    except ValueError as e:
        print(e)
    print("\nAll error raising tests completed!")


test_plant_checks()
