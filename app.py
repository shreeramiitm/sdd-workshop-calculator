from flask import Flask, render_template, request, jsonify
import sys

app = Flask(__name__)

@app.route('/')
def index():
    """Serves the main calculator user interface."""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Handles mathematical calculations sent from the client."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        # Validate presence of required keys
        if 'num1' not in data or 'num2' not in data or 'operation' not in data:
            return jsonify({'error': 'Missing required fields: num1, num2, and operation are required'}), 400

        # Retrieve and validate types of numbers
        try:
            num1 = float(data['num1'])
            num2 = float(data['num2'])
        except (ValueError, TypeError):
            return jsonify({'error': 'num1 and num2 must be valid numbers'}), 400

        operation = data['operation']
        if not isinstance(operation, str):
            return jsonify({'error': 'operation must be a string'}), 400

        operation = operation.lower().strip()

        # Execute operations safely
        result = None
        if operation in ('add', '+'):
            result = num1 + num2
        elif operation in ('subtract', '-'):
            result = num1 - num2
        elif operation in ('multiply', 'multiply', '*', 'x', '×'):
            result = num1 * num2
        elif operation in ('divide', '/', '÷'):
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed'}), 422
            result = num1 / num2
        else:
            return jsonify({'error': f"Unsupported operation: '{operation}'"}), 400

        # Check for float overflow/underflow or NaN/Inf
        if result is not None:
            if result == float('inf') or result == float('-inf') or result != result: # check for nan/inf
                return jsonify({'error': 'Calculation resulted in an overflow or invalid number'}), 422
            
            # Format result: convert to int if it is a whole number to look cleaner
            if result.is_integer():
                result = int(result)
            
            return jsonify({'result': result}), 200

    except OverflowError:
        return jsonify({'error': 'Number overflow occurred during calculation'}), 422
    except Exception as e:
        return jsonify({'error': f'An unexpected server error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Start the Flask app
    app.run(debug=True, host='127.0.0.1', port=5000)
