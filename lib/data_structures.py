spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_emojis = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        heat_emojis = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emojis}")

def get_average_heat_level(spicy_foods):
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

# Example usage
if __name__ == "__main__":
    # Print the names of all spicy foods
    print(get_names(spicy_foods))

    # Print the spiciest foods (heat level > 5)
    print(get_spiciest_foods(spicy_foods))

    # Print all spicy foods with emojis
    print_spicy_foods(spicy_foods)

    # Get spicy food by cuisine
    print(get_spicy_food_by_cuisine(spicy_foods, "American"))

    # Print the spiciest foods with emojis
    print_spiciest_foods(spicy_foods)

    # Get the average heat level
    print(get_average_heat_level(spicy_foods))

    # Add a new spicy food and print the updated list
    new_food = {
        "name": "Griot",
        "cuisine": "Haitian",
        "heat_level": 10,
    }
    print(create_spicy_food(spicy_foods, new_food))
