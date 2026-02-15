from flask import Flask, jsonify
from flask_cors import CORS
from services import load_data, calculate_summary

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "online", "message": "Birhan Energies Financial API"})

@app.route('/api/prices', methods=['GET'])
def get_prices():
    prices, _ = load_data()
    if prices is None:
        return jsonify({"error": "Data source unavailable"}), 500
    
    # Return last 500 records for performance
    recent_data = prices.tail(500).copy()
    recent_data['Date'] = recent_data['Date'].dt.strftime('%Y-%m-%d')
    return jsonify(recent_data.to_dict(orient='records'))

@app.route('/api/events', methods=['GET'])
def get_events():
    _, events = load_data()
    if events is None:
        return jsonify({"error": "Events data unavailable"}), 500
    return jsonify(events.to_dict(orient='records'))

@app.route('/api/analysis-summary', methods=['GET'])
def get_summary():
    prices, _ = load_data()
    if prices is None:
        return jsonify({"error": "Data unavailable"}), 500
    
    summary = calculate_summary(prices)
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True, port=5000)