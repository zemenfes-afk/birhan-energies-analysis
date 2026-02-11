import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRICES_PATH = os.path.abspath(os.path.join(BASE_DIR, '../../data/brentoilprices.csv'))
EVENTS_PATH = os.path.abspath(os.path.join(BASE_DIR, '../../data/events.csv'))

def load_data():
    try:
        prices_df = pd.read_csv(PRICES_PATH)
        prices_df['Date'] = pd.to_datetime(prices_df['Date'], format='%d-%b-%y', errors='coerce')
        prices_df = prices_df.dropna(subset=['Date'])
        events_df = pd.read_csv(EVENTS_PATH)
        return prices_df, events_df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

@app.route('/')
def home():
    return jsonify({"status": "online", "message": "Birhan Energies API is running"})

@app.route('/api/prices', methods=['GET'])
def get_prices():
    prices, _ = load_data()
    if prices is None: return jsonify({"error": "Data not found"}), 404
    recent = prices.tail(500).copy()
    recent['Date'] = recent['Date'].dt.strftime('%Y-%m-%d')
    return jsonify(recent.to_dict(orient='records'))

@app.route('/api/events', methods=['GET'])
def get_events():
    _, events = load_data()
    return jsonify(events.to_dict(orient='records')) if events is not None else (jsonify({"error": "No events"}), 404)

@app.route('/api/analysis-summary', methods=['GET'])
def get_summary():
    prices, _ = load_data()
    if prices is None: return jsonify({"error": "Data not found"}), 404
    return jsonify({
        "average_price": round(prices['Price'].mean(), 2),
        "max_price": prices['Price'].max(),
        "total_days": len(prices)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)