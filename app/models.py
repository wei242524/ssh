from .database import db

# Model for Ingredients
class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Ingredient {self.name}>"

# Model for Recipes
class Recipe(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)  # Store ingredients as comma-separated text
    instructions = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Recipe {self.name}>"

