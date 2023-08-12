from flask import Flask, request, jsonify , render_template, redirect, url_for

app = Flask(__name__)

car_dict={
    "Large": "300.4",
    "Medium": "280.3",
    "Small": "260.2"
}


@app.route('/get_category', methods=['GET'])
def get_car_category():
    return jsonify(car_dict), 200

@app.route('/', methods=['GET', 'POST'])
def update_car_category():
    
    if request.method == 'POST':
        Category = request.form['Category']
        Price = request.form['Price']
        car_dict[Category] = Price

        return redirect(url_for('update_car_category'))

    return render_template('update_car_category.html', car_dict=car_dict)


if __name__ == '__main__':
    app.run()
