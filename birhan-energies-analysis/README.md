# Birhan Energies: Brent Oil Price Change Point Analysis

This repository contains a full-stack data science solution for analyzing the impact of geopolitical and economic events on Brent oil prices using Bayesian Inference.

## 🚀 Project Structure
- `/data`: Historical Brent oil prices (1987-2022) and researched events CSV.
- `/notebooks`: Jupyter notebook containing EDA and PyMC Bayesian Modeling.
- `/dashboard`:
    - `/backend`: Flask API serving prices, events, and summary statistics.
    - `/frontend`: React dashboard with interactive Recharts visualizations.
- `/docs`: Interim and Final reports.

## 🛠️ Setup & Installation

### Backend (Flask)
1. Navigate to `dashboard/backend`.
2. Install dependencies: `pip install -r ../../requirements.txt`.
3. Start the server: `python app.py` (Runs on port 5000).

### Frontend (React)
1. Navigate to `dashboard/frontend`.
2. Install dependencies: `npm install`.
3. Start the app: `npm start` (Runs on port 3000).

## 📊 Dashboard Features
- **Interactive Visualizations**: Real-time line charts of price trends.
- **Event Highlighting**: Reference lines indicating structural breaks correlated with global events.
- **Filters**: Date range selectors to drill down into specific price regimes.