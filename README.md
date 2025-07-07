# Chinese Remainder Theorem Solver Web App
A Flask-based web app that solves systems of congruences using the Chinese Remainder Theorem. Users can select the number of equations and input values to compute a unique solution instantly.

This is a Flask-based web application that solves systems of linear congruences using the **Chinese Remainder Theorem**.

🔧 Features
- Input any number of equations dynamically.
- Automatically computes and displays the unique solution (if it exists).
- Frontend built with HTML, CSS, and JavaScript.
- Backend built with Python and Flask.

📁 Project Structure
project/
│

├── app.py # Flask backend with CRT logic

├── templates/

│ └── index.html # Frontend form for user interaction


🚀 Getting Started
### Prerequisites
- Python 3.x
- Flask

### Installation
1. Clone this repository or download the files.
2. Navigate to the project directory.
3. Install Flask if not already installed:
   pip install flask
4. Run the app:
   python app.py
5. Open your browser and go to http://127.0.0.1:5000

📌 Usage
1. Enter the number of equations you want to solve.
2. For each equation, input the remainder (a) and modulus (m) values.
3. Click Solve to compute the result.
4. The app will return the value of x that satisfies all the given congruences.

⚠️ Notes
-- Make sure that all moduli entered are pairwise coprime for the Chinese Remainder Theorem to be valid.
-- The result is calculated using the Extended Euclidean Algorithm to find modular inverses.


