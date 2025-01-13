# %% [markdown]
# ![image](image.jpg)
# 
# As a Software Engineer in a Health and Leisure company, your task is to add a new feature to the app: a calorie and nutrition calculator. This tool will calculate and display total calories, sugars, fats, and other nutritional values for different foods based on user input.
# 
# You have been provided with the `nutrition.json` dataset, which contains the necessary nutritional information for various foods. Each value in the dataset is per **100 grams** of the food item. The dataset has already been read and loaded for you as the dictionary `nutrition_dict`.
# 
# ## Dataset Summary
# 
# `nutrition.json`
# 
# | Column        | Description                                             |
# |---------------|---------------------------------------------------------|
# | `food` | The name of the food.                                   |
# | `calories`  | The amount of energy provided by the food, measured in kilocalories (kcal) per 100 grams. |
# | `total_fat` | The total fat content in grams per 100 grams.                         |
# | `protein`   | The protein content in grams per 100 grams.                           |
# | `carbohydrate` | The total carbohydrate content in grams per 100 grams.             |
# | `sugars`    | The amount of sugars in grams per 100 grams.                          |
# 
# ### Let's Get Started!
# 
# This project is a great opportunity to build a real-world feature from scratch, showcasing your development skills and making a meaningful impact on users' health and wellness.

# %%
import json  # Import the json module to work with JSON files

# Open the nutrition.json file in read mode and load its content into a dictionary
with open('nutrition.json', 'r') as json_file:
    nutrition_dict = json.load(json_file)  # Load the JSON content into a dictionary
    
# Display the first 3 items of the nutrition dictionary
list(nutrition_dict.items())[:3]

# %%
# Start coding here!
# Use as many cells as you need.
def nutritional_summary(input_dict:dict)->dict:
    data_to_return = {
        'calories': 0.0,
        'total_fat': 0.0,
        'protein': 0.0,
        'carbohydrate': 0.0,
        'sugars': 0.0
    }
    not_exists = []
    for key, value in input_dict.items():
        
        if key in nutrition_dict:
            k_nutrition = nutrition_dict[key]
            data_to_return['calories'] += (k_nutrition['calories'] /100) * value
            data_to_return['total_fat'] += (k_nutrition['total_fat'] /100) * value
            data_to_return['protein'] += (k_nutrition['protein'] /100) * value
            data_to_return['carbohydrate'] += (k_nutrition['carbohydrate'] /100) * value
            data_to_return['sugars'] += (k_nutrition['sugars'] /100) * value
        else:
            not_exists.append(key)
            
    if not_exists:
        return not_exists[0]
    else:
        return data_to_return

# %%
nutritional_summary({"Croissants, cheese": 150, "Orange juice, raw": 250})


