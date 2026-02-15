import pandas as pd
import os
from typing import Tuple, Optional, List, Dict

def get_data_paths() -> Tuple[str, str]:
    """Returns absolute paths for prices and events data."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Adjust this path based on your actual folder structure
    prices_path = os.path.abspath(os.path.join(base_dir, '../../data/brentoilprices.csv'))
    events_path = os.path.abspath(os.path.join(base_dir, '../../data/events.csv'))
    return prices_path, events_path

def load_data() -> Tuple[Optional[pd.DataFrame], Optional[pd.DataFrame]]:
    """
    Loads and cleans oil price data.
    Returns: (prices_df, events_df)
    """
    prices_path, events_path = get_data_paths()
    try:
        # Load Prices
        prices = pd.read_csv(prices_path)
        prices['Date'] = pd.to_datetime(prices['Date'], format='%d-%b-%y', errors='coerce')
        prices = prices.dropna(subset=['Date'])
        
        # Load Events
        events = pd.read_csv(events_path)
        return prices, events
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

def calculate_summary(prices: pd.DataFrame) -> Dict[str, float]:
    """Calculates financial summary metrics."""
    return {
        "average_price": round(prices['Price'].mean(), 2),
        "max_price": prices['Price'].max(),
        "min_price": prices['Price'].min(),
        "total_days": len(prices)
    }