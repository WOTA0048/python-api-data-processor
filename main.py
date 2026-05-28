import requests

def fetch_and_analyze_data():
    # Fetching real-time exchange rate data from a free public API
    url = "https://open.er-api.com/v6/latest/USD"
    print("Connecting to API to fetch live financial data...")
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            rates = data.get("rates", {})
            
            # Simple data filtering and calculation
            target_currencies = ["JPY", "EUR", "GBP"]
            print("\n--- Live Currency Rates (Base: USD) ---")
            for crypto in target_currencies:
                if crypto in rates:
                    print(f"1 USD = {rates[crypto]:.2f} {crypto}")
                    
            # Demonstrating logical conditions
            jpy_rate = rates.get("JPY", 0)
            if jpy_rate > 150:
                print("\nAnalysis: JPY is currently trading weak against the USD.")
            else:
                print("\nAnalysis: JPY is holding strong against the USD.")
                
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_and_analyze_data()