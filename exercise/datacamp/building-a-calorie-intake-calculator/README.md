Sure, here is a README.md for this code:

# Calorie and Nutrition Calculator

This Python code calculates and displays total calories, sugars, fats, and other nutritional values for different foods based on user input. 

## Dataset

The code uses a JSON dataset named `nutrition.json` that contains the necessary nutritional information for various foods. Each value in the dataset is per **100 grams** of the food item.

## Code

The code first opens the `nutrition.json` file and loads its content into a dictionary. Then, it defines a function called `nutritional_summary` that takes a dictionary as input, where the keys are the names of the foods and the values are the quantities in grams. The function iterates through the user-provided dictionary and calculates the total calories, sugars, fats, protein and carbohydrates based on the information in the `nutrition_dict`.

## Running the Code

1. Save the code as a Python file (e.g., `calorie_calculator.py`).
2. Make sure you have the `json` library installed (`pip install json`).
3. Run the script from your terminal: `python calorie_calculator.py`

The code will prompt you for user input. Enter the names of the foods and their quantities in grams separated by commas. For example:

```
Croissants, cheese: 150, Orange juice, raw: 250
```

The code will then calculate and display the total nutritional information for the entered foods.

## Example Output

```
{'calories': 513.0, 'total_fat': 10.05, 'protein': 8.75, 'carbohydrate': 103.75, 'sugars': 50.0}
```

In this example, the output shows the total calories, fat, protein, carbohydrates, and sugars for 150 grams of croissants, cheese and 250 grams of orange juice.

## Additional Notes

* The code currently assumes that all food names in the user input exactly match the names in the `nutrition_dict`.
* You can modify the code to handle cases where food names don't match exactly or to provide more user-friendly output.
