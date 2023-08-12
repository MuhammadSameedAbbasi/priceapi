from flask import Flask, request, jsonify , render_template, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = "b'\xb5g\x97C\xebK\xd3EcR\xcb\xf5\x9b\xe1\xe0\xa7\x04X\xf4\xb1\x94Yw\xc9'" # Replace with a secret key
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

car_dict={
    "Large": "300.4",
    "Medium": "280.3",
    "Small": "260.2"
}

VALID_USERNAME = 'admin'
VALID_PASSWORD = 'a'

@app.route('/get_category', methods=['GET'])
def get_car_category():
    return jsonify(car_dict), 200


@app.route('/set_category', methods=['GET', 'POST'])
def update_car_category():
    if session.get('logged_in'):
        if request.method == 'POST':
            Category = request.form['Category']
            Price = request.form['Price']
            
            if Category in car_dict:
                car_dict[Category] = Price
                return redirect(url_for('update_car_category'))
            else:
                return render_template('update_car_category.html', car_dict=car_dict, error_message="Category not found")
        return render_template('update_car_category.html', car_dict=car_dict)
    else:
        return redirect(url_for('login'))



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['logged_in'] = True  # Set session variable for successful login
            return redirect(url_for('update_car_category'))

    return render_template('login.html')


if __name__ == '__main__':
    app.run()