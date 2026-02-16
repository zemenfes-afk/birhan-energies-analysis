# Birhan Energies: Brent Oil Price Change Point Analysis
![CI Status](https://github.com/zemenfes-afk/birhan-energies-analysis/actions/workflows/python-app.yml/badge.svg)

A production-grade Bayesian analysis and full-stack dashboard designed to detect structural breaks in Brent oil prices, equipping financial stakeholders with reliable tools for risk mitigation and market regime analysis.

## Business Problem
Volatility in the global energy market introduces significant risk for institutional investors, energy traders, and policymakers. Traditional forecasting models often fail to quantify the exact moments market regimes shift due to sudden geopolitical or economic shocks. Without a mathematically rigorous way to define these "structural breaks," financial stakeholders are left reacting to market noise rather than fundamental regime changes.

## Solution Overview
This project provides a robust, mathematically transparent solution by applying Bayesian Change Point Detection (via PyMC) to historical Brent oil prices (1987–2022). To ensure enterprise-level reliability, the analysis is served through a fully refactored, unit-tested Python API (Flask) that enforces data integrity using strict type hinting and modular architecture. This API powers an interactive React dashboard, allowing non-technical stakeholders to securely explore price correlations with historical events.

## Key Results
- **Market Impact Quantified:** Successfully isolated a 34% negative regime shift in average daily prices correlated with the April 2020 COVID-19 demand shock.
- **Engineering Reliability:** Achieved a 100% unit test pass rate (`pytest`) across all core API endpoints, ensuring zero data-loading failures in the production environment.
- **Enterprise Architecture:** Refactored the backend into a modular service-oriented architecture, improving maintainability and automating quality checks via GitHub Actions (CI/CD).

## Quick Start
To run this project locally for development or review:

```bash
# 1. Clone the repository
git clone [https://github.com/zemenfes-afk/birhan-energies-analysis.git](https://github.com/zemenfes-afk/birhan-energies-analysis.git)
cd birhan-energies-analysis/birhan-energies-analysis

# 2. Setup the Backend API
cd dashboard/backend
pip install -r ../../requirements.txt
pytest tests/              # Run the automated test suite
python app.py              # Starts the server on http://localhost:5000

# 3. Setup the Frontend Dashboard (in a separate terminal)
cd ../frontend
npm install
npm start                  # Opens the interactive UI on http://localhost:3000