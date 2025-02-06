from flask import Flask, request, jsonify
import requests
from collections import OrderedDict

app = Flask(__name__)

def is_prime(n):
    if  n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d**len(digits) for d in digits) == n

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_str = request.args.get('number')

    if not number_str or not number_str.isdigit():
        return jsonify({"number": number_str, "error": True}), 400

    number = int(number_str)
    properties = []

    if is_prime(number):
        properties.append("prime")
    if is_perfect(number):
        properties.append("perfect")
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    digit_sum = sum(int(d) for d in str(abs(number)))

    
    try:
        response = requests.get(f"http://numbersapi.com/{number}")
        fun_fact = response.text if response.status_code == 200 else "No fun fact available."
    except requests.RequestException:
        fun_fact = "Error fetching fun fact."

    response_data = OrderedDict([
        ("number", number),
        ("is_prime", is_prime(number)),
        ("is_perfect", is_perfect(number)),
        ("properties", properties),
        ("digit_sum", digit_sum),
        ("fun_fact", fun_fact)
    ])
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
