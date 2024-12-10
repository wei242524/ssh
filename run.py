from app import create_app
from app.database import db
from app.models import Ingredient, Recipe  # Import the models

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure all tables are created
    app.run(debug=True, port=5000)
