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
    return [food["name"] for food in spicy_foods]

print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    #get heat levels
   return [food for food in spicy_foods if food["heat_level"] > 5]
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    spicy_meals = []
    for food in spicy_foods:
        heat_level_chillies = "🌶" * food["heat_level"]
        food_line = f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_chillies}"
        spicy_meals.append(food_line)
        
    # Use "\n" to join the lines for proper formatting
    print("\n".join(spicy_meals))


print(print_spicy_foods(spicy_foods))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food
    return None
print(get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
    spicy_meals = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = "🌶" * food["heat_level"]
            food_line = f"{name} ({cuisine}) | Heat Level: {heat_level}"
            spicy_meals.append(food_line)  

    # Join with "\n" and print the result
    print("\n".join(spicy_meals))

print_spiciest_foods(spicy_foods)        

def get_average_heat_level(spicy_foods):
    total= 0
    for food in spicy_foods:
        total+= food["heat_level"]
    return total / len(spicy_foods)

print(get_average_heat_level(spicy_foods))

food = { "name": "Nasi Lemak",
        "cuisine": "Malaysian",
        "heat_level": 8 }
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

print(create_spicy_food(spicy_foods, food))