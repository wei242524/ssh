from flask import Blueprint, jsonify, request
from .models import Ingredient, Recipe, db
from datetime import datetime

routes = Blueprint('routes', __name__)

# API: Get all ingredients
@routes.route('/api/ingredients', methods=['GET'])
def get_ingredients():
    ingredients = Ingredient.query.all()
    return jsonify([
        {"id": i.id, "name": i.name, "expiration_date": i.expiration_date.strftime('%Y-%m-%d'), "quantity": i.quantity}
        for i in ingredients
    ])

# API: Add a new ingredient
@routes.route('/api/ingredients', methods=['POST'])
def add_ingredient():
    data = request.json
    new_ingredient = Ingredient(
        name=data['name'],
        expiration_date=datetime.strptime(data['expiration_date'], '%Y-%m-%d').date(),
        quantity=data['quantity']
    )
    db.session.add(new_ingredient)
    db.session.commit()
    return jsonify({"message": "Ingredient added successfully"}), 201

# API: Get all recipes
@routes.route('/api/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([
        {"id": r.id, "name": r.name, "ingredients": r.ingredients, "instructions": r.instructions}
        for r in recipes
    ])

# API: Add a new recipe
@routes.route('/api/recipes', methods=['POST'])
def add_recipe():
    data = request.json
    new_recipe = Recipe(
        name=data['name'],
        ingredients=data['ingredients'],
        instructions=data['instructions']
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({"message": "Recipe added successfully"}), 201

# API: Delete an ingredient
@routes.route('/api/ingredients/<int:id>', methods=['DELETE'])
def delete_ingredient(id):
    ingredient = Ingredient.query.get_or_404(id)
    db.session.delete(ingredient)
    db.session.commit()
    return jsonify({"message": "Ingredient deleted successfully"})

# API: Delete a recipe
@routes.route('/api/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Recipe deleted successfully"})
