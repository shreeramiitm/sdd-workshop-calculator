from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API Route to handle the math
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    # Grab numbers from the frontend
    try:
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
    except ValueError:
        return jsonify({'error': 'Invalid numbers provided'}), 400

    operation = data.get('operation')
    result = 0

    # Perform the requested operation
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({'error': 'Cannot divide by zero'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)