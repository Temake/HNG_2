from flask import Flask, request, jsonify
import requests
from collections import OrderedDict
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
def is_armstrong(n):
    digits = [int(d) for d in str(n) if d.isdigit()]  
    return sum(pow(d, len(digits)) for d in digits) == n

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_str = request.args.get('number')

    try:
        number = int(number_str) 
    except (ValueError, TypeError):
        return jsonify({"number": number_str, "error": "Invalid number format"}), 400

    is_armstrong_number = is_armstrong(number)
    is_even = (number % 2 == 0)

   
    if is_armstrong_number:
        properties = ["armstrong", "even"] if is_even else ["armstrong", "odd"]
    else:
        properties = ["even"] if is_even else ["odd"]

    digit_sum = sum(int(d) for d in str(number) if d.isdigit())  

    try:
        response = requests.get(f"http://numbersapi.com/{number}", timeout=3)
        fun_fact = response.text if response.status_code == 200 else "No fun fact available."
    except requests.RequestException:
        fun_fact = "No fun fact available."

    response_data = OrderedDict([
        ("number", number),
        ("properties", properties),
        ("digit_sum", digit_sum),
        ("fun_fact", fun_fact)
    ])

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)