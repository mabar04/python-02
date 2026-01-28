class GardenManager(Exception):
    """
    Manages plants and watering operations in a simple garden simulation.

    Attributes
    ----------
    plants : list
        List of plants with name, water requirement, and sunlight hours.
    tank : int
        Represents available water in the watering tank.
    """
    def __init__(self) -> None:
        self.plants: list = []
        self.tank = 50

    def add_plant(self, plant_name: str, water_level: int | float,
                  sunlight_hours: int | float) -> None:
        """
        Add a plant to the garden after validating its health parameters.

        Raises
        ------
        ValueError
            If sunlight_hours or water_level are out of valid range, or
            if plant_name is empty.
        """
        if plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             f"is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             f"is too high (max 12)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level}"
                             f"is too high (max 10)")
        if water_level < 1:
            raise ValueError(f"Water level {water_level}"
                             f"is too low (min 1)")
        self.plants = self.plants + [{"name": plant_name,
                                      "water": water_level,
                                      "sunlight": sunlight_hours}]
        print(f"Added {plant_name} successfully")

    def watering_plant(self) -> None:
        """
        Simulate watering plants and update their water levels.
        """
        print("Watering plants...")
        try:
            print("Opening watering system")
            i = 0
            for plant in self.plants:
                print(f"Watering {plant["name"]} - success")
                if plant["name"] == "lettuce":
                    plant["water"] += 2
                plant["water"] += 3
                self.tank -= 15
                i += 1
        except Exception as e:
            print(f"Error occured {e}")
        finally:
            print("Closing watering system (cleanup)")

    def checking_plant_health(self) -> None:
        """
        Validate that plants have healthy water levels.

        Raises
        ------
        ValueError
            If any plant has too low or too high water levels.
        """
        print("Checking plant health...")
        for plant in self.plants:
            if plant["water"] < 1:
                raise ValueError(f"Error checking {plant["name"]}: Water level"
                                 f"{plant["water"]} is too low (min 1)")
            elif plant["water"] > 10:
                raise ValueError(f"Error checking {plant["name"]}: Water level"
                                 f" {plant["water"]} is too high (max 10)")
            print(f"{plant["name"]}:  healthy (water: {plant["water"]}, "
                  f"sun: {plant["sunlight"]})")

    def testing_errors(self) -> None:
        """
        Test error recovery by simulating a low-tank scenario.

        Behavior
        --------
        - Raises a ValueError if the tank is too low.
        - Recovers by refilling the tank.
        """
        try:
            if self.tank < 30:
                raise ValueError("Caught GardenError: Not enough "
                                 "water in tank")
        except ValueError as e:
            print(e)
            self.tank += 50
            print("System recovered and continuing...")


def test_garden_management() -> None:
    """
    Demonstrate the complete garden management workflow:
    - Adding plants
    - Watering plants
    - Checking health
    - Handling errors
    """
    g = GardenManager()
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    try:
        g.add_plant("Tomato", 2, 8)
        g.add_plant("lettuce", 10, 6)
        g.add_plant("", 15, 8)
    except ValueError as e:
        print("Error adding plant: ", e)
    print()
    g.watering_plant()
    print()
    try:
        g.checking_plant_health()
    except ValueError as e:
        print(e)
    print()
    print("Testing error recovery...")
    g.testing_errors()
    print("\nGarden management system test complete!")


test_garden_management()
