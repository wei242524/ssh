from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Mock API URL (replace this with your actual backend API URL)
API_BASE_URL = "http://127.0.0.1:5000/api"

# Dashboard: Display ingredients
@app.route('/')
def dashboard():
    try:
        response = requests.get(f"{API_BASE_URL}/ingredients")
        ingredients = response.json()
    except Exception as e:
        print(f"Error fetching ingredients: {e}")
        ingredients = []
    return render_template('dashboard.html', ingredients=ingredients)

# Add Ingredient: Form to add a new ingredient
@app.route('/add-ingredient', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'POST':
        name = request.form['name']
        expiration_date = request.form['expiration_date']
        quantity = request.form['quantity']

        payload = {
            "name": name,
            "expiration_date": expiration_date,
            "quantity": quantity
        }
        try:
            response = requests.post(f"{API_BASE_URL}/ingredients", json=payload)
            if response.status_code == 201:
                return redirect(url_for('dashboard'))
            else:
                print(f"Error adding ingredient: {response.json()}")
        except Exception as e:
            print(f"Error: {e}")
    return render_template('add_ingredient.html')

# Recipes: Display all recipes
@app.route('/recipes')
def recipes():
    try:
        response = requests.get(f"{API_BASE_URL}/recipes")
        recipes = response.json()
    except Exception as e:
        print(f"Error fetching recipes: {e}")
        recipes = []
    return render_template('recipes.html', recipes=recipes)

# Add Recipe: Form to add a new recipe
@app.route('/add-recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']

        payload = {
            "name": name,
            "ingredients": ingredients,
            "instructions": instructions
        }
        try:
            response = requests.post(f"{API_BASE_URL}/recipes", json=payload)
            if response.status_code == 201:
                return redirect(url_for('recipes'))
            else:
                print(f"Error adding recipe: {response.json()}")
        except Exception as e:
            print(f"Error: {e}")
    return render_template('add_recipe.html')

if __name__ == '__main__':
    app.run(debug=True)

