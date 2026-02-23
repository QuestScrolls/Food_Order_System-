from typing import Dict, List, Optional

# Menu data structure: cuisine -> list of dishes
MENUS: Dict[str, List[str]] = {
    "italian": ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"],
    "indian": ["Curry", "Chutney", "Samosa", "Naan"]
}
VALID_CUISINES = list(MENUS.keys())

def display_available_meals(cuisine: str) -> None:
    """Print all meals for a given cuisine."""
    meals = MENUS.get(cuisine.lower())
    if meals:
        print(f"\nAvailable {cuisine.capitalize()} meals:")
        for meal in meals:
            print(f"  - {meal}")
    else:
        print(f"Sorry, we don't have '{cuisine}' cuisine. Choose from: {', '.join(VALID_CUISINES)}")

def find_meal(cuisine: str, meal_name: str) -> Optional[str]:
    """
    Find a meal in the given cuisine's menu (case‑insensitive).
    Returns the properly cased meal name if found, else None.
    """
    meals = MENUS.get(cuisine.lower())
    if not meals:
        return None
    for meal in meals:
        if meal.lower() == meal_name.lower():
            return meal
    return None

def get_positive_integer(prompt: str) -> int:
    """Prompt user until a positive integer is entered."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_cuisine_choice() -> str:
    """Prompt user for a valid cuisine."""
    while True:
        cuisine = input("Choose cuisine type (Italian/Indian): ").strip().lower()
        if cuisine in VALID_CUISINES:
            return cuisine
        print(f"Invalid cuisine. Please choose from: {', '.join(VALID_CUISINES)}")

def create_summary(cuisine: str, meal_name: str, amount: int) -> str:
    """
    Generate an order summary string.
    Returns a success message if meal is found, otherwise an error message.
    """
    canonical_meal = find_meal(cuisine, meal_name)
    if canonical_meal:
        # Optional: add pluralization for fun
        meal_display = f"{amount} x {canonical_meal}"
        return f"✅ You ordered: {meal_display}"
    else:
        return f"❌ Meal '{meal_name}' not found in {cuisine.capitalize()} menu."

def main():
    print("🍽️  Welcome to the Food Order System!\n")

    cuisine = get_cuisine_choice()
    display_available_meals(cuisine)

    meal_name = input("\nEnter the name of the meal: ").strip()
    amount = get_positive_integer("Enter the quantity: ")

    result = create_summary(cuisine, meal_name, amount)
    print("\n" + result)

if __name__ == "__main__":
    main()
