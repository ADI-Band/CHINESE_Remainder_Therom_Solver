from flask import Flask, render_template, request, jsonify
import sys

# Function to compute the gcd of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute the modular inverse of a number
# using the Extended Euclidean Algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Function to solve the Chinese Remainder Theorem
def chinese_remainder_theorem(a, m):
    # Check if the moduli are pairwise coprime
    M = 1
    for mod in m:
        M *= mod
        
    result = 0
    for i in range(len(a)):
        Mi = M // m[i]
        Mi_inv = mod_inverse(Mi, m[i])
        result += a[i] * Mi * Mi_inv

    return result % M

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        n = int(request.form['num_equations'])
        if n <= 0:
            raise ValueError("Number of equations must be greater than 0.")

        a = []
        m = []

        for i in range(n):
            ai = int(request.form[f'a{i + 1}'])
            mi = int(request.form[f'm{i + 1}'])
            
            if mi == 0:
                raise ValueError(f"Modulus m{i + 1} cannot be zero.")
            
            a.append(ai)
            m.append(mi)

        solution = chinese_remainder_theorem(a, m)

        return jsonify({"result": f"The solution to the system is: x = {solution}"})
    
    except ValueError as ve:
        return jsonify({"error": str(ve)})
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."})

if __name__ == "__main__":
    app.run(debug=True)
