from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Placeholder response
    return "<h1>Weather ML App is Running!</h1><p>Placeholder page for Task 1 completion.</p>"

@app.route('/predict')
def predict():
    # Placeholder prediction endpoint
    data = {
        "status": "success",
        "model_result": "Simulated sunny day",
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
