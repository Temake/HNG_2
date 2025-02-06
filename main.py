from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
def is_armstrong(n):
    n=abs(n)
    digits = [int(d) for d in str(n) if d.isdigit()]
    return sum(pow(d, len(digits)) for d in digits) == n
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_str = request.args.get('number')

    try:
        number = int(number_str)  
    except (ValueError, TypeError):
        return jsonify({"number": number_str, "error": True }), 400

    number = int(number_str)
    properties = []

    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    if number % 2 != 0:
        properties.append("odd")

    digit_sum = sum(int(d) for d in str(number) if d.isdigit())

    try:
        response = requests.get(f"http://numbersapi.com/{number}", timeout=3)
        fun_fact = response.text if response.status_code == 200 else "No fun fact available."
    except requests.RequestException:
        fun_fact = "No fun fact available."

    return jsonify({
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    })

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)