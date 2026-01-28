class GardenError(Exception):
    """
    Base exception class for all garden-related errors.
    Used to group and catch any type of garden exception.
    """
    pass


class PlantError(GardenError):
    """
    Represents errors related to plants (e.g., growth issues, disease).
    Inherits from GardenError so it can be caught generically.
    """
    pass


class WaterError(PlantError):
    """
    Represents watering-related plant issues (e.g., dehydration or overflow).
    Inherits from PlantError to show specialization.
    """
    pass


def test_planterror() -> None:
    """
    Raise a PlantError for demonstration.
    """
    raise PlantError("The tomato plant is wilting!")


def test_watererror() -> None:
    """
    Raise a WaterError for demonstration.
    """
    raise WaterError("Not enough water in the tank!")


print("=== Custom Garden Errors Demo ===\n")
print("Testing PlantError...")
try:
    test_planterror()
except PlantError as e:
    print("Caught PlantError: ", e)
print("\nTesting WaterError...")
try:
    test_watererror()
except WaterError as e:
    print("Caught WaterError: ", e)
print("\nTesting catching all garden errors...")
try:
    test_planterror()
except GardenError as e:
    print("Caught a garden error:", e)
try:
    test_watererror()
except GardenError as e:
    print("Caught a garden error:", e)
print("\nAll custom error types work correctly!")
