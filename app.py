from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock API URL (replace this with the actual backend API URL)
API_BASE_URL = "http://127.0.0.1:5000/api"

@app.route('/')
def dashboard():
    import requests
    try:
        # Call the backend API to fetch data
        response = requests.get(f"{API_BASE_URL}/ingredients")
        ingredients = response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        ingredients = []

    return render_template('dashboard.html', ingredients=ingredients)

@app.route('/add-ingredient', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'POST':
        name = request.form['name']
        expiration_date = request.form['expiration_date']
        quantity = request.form['quantity']

        # Send data to the backend API
        import requests
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

if __name__ == '__main__':
    app.run(debug=True)
