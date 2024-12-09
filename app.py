from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__, template_folder='templates', static_folder='static')

# Base URL for the backend API
API_BASE_URL = "http://127.0.0.1:5000/api"

# Frontend: Dashboard
@app.route('/')
def dashboard():
    try:
        response = requests.get(f"{API_BASE_URL}/ingredients")
        response.raise_for_status()  # Raise an error for HTTP errors
        ingredients = response.json()
    except requests.exceptions.RequestException as e:
        ingredients = []
        print(f"Error fetching ingredients: {e}")
    return render_template('dashboard.html', ingredients=ingredients)

# Frontend: Add Ingredient
@app.route('/add-ingredient', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "expiration_date": request.form['expiration_date'],
            "quantity": request.form['quantity']
        }
        try:
            response = requests.post(f"{API_BASE_URL}/ingredients", json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error adding ingredient: {e}")
        return redirect(url_for('dashboard'))
    return render_template('add_ingredient.html')

# Frontend: Remove Ingredient
@app.route('/delete-ingredient/<int:id>', methods=['POST'])
def delete_ingredient(id):
    try:
        response = requests.delete(f"{API_BASE_URL}/ingredients/{id}")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error deleting ingredient: {e}")
    return redirect(url_for('dashboard'))

# Frontend: Recipes
@app.route('/recipes')
def recipes():
    try:
        response = requests.get(f"{API_BASE_URL}/recipes")
        response.raise_for_status()
        recipes = response.json()
    except requests.exceptions.RequestException as e:
        recipes = []
        print(f"Error fetching recipes: {e}")
    return render_template('recipes.html', recipes=recipes)

# Frontend: Add Recipe
@app.route('/add-recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "ingredients": request.form['ingredients'],
            "instructions": request.form['instructions']
        }
        try:
            response = requests.post(f"{API_BASE_URL}/recipes", json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error adding recipe: {e}")
        return redirect(url_for('recipes'))
    return render_template('add_recipe.html')

# Frontend: Remove Recipe
@app.route('/delete-recipe/<int:id>', methods=['POST'])
def delete_recipe(id):
    try:
        response = requests.delete(f"{API_BASE_URL}/recipes/{id}")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error deleting recipe: {e}")
    return redirect(url_for('recipes'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
