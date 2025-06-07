from flask import render_template, Flask, request, jsonify
import yfinance as yf
import io
from app.api_operations.StockDetails import StockDetails
from app.api_operations.exchange_codes import get_exchange_country
from app.api_operations.stock_screens import StockScreens
import pandas as pd
import requests

app = Flask(__name__)

# @app.route('/suggestions')
# def get_suggestions():
#     query = request.args.get('query', '').strip().lower()
#     if not query or len(query) < 3:
#         return jsonify([])  # Return empty if query is too short
#
#     # Search both in stock symbols and company names
#     matches = [
#         {"symbol": symbol, "name": name}
#         for symbol, name in symbol_to_company.items()
#         if query in symbol.lower() or query in name.lower()
#     ]
#
#     return jsonify(matches[:5])


@app.route('/suggestions')
def get_suggestions():
    query = request.args.get('query', '').strip().lower()
    if not query or len(query) < 3:
        return jsonify([])  # Return empty if query is too short

    # Use the Yahoo Finance search API to find relevant suggestions
    results = yf.search.Search(query).response.get('quotes', [])

    # Extract only 'symbol' and 'shortname' from the search results, ensuring 'symbol' exists
    suggestions = [
        {"symbol": item["symbol"], "shortname": item.get("shortname", ""), "country_flag": get_exchange_country(item.get('exchange'))[1]}
        for item in results if "symbol" in item
    ]

    return jsonify(suggestions)  # Return all results

@app.route('/')
def home():
    screens = {
    # 'Large Cap Value Stock Screen': StockScreens.get_large_cap_value_stocks(),
    # 'Mid Cap Value Stock Screen': StockScreens.get_mid_cap_value_stocks(),
    # 'Mid Cap Aggressive Stock Screen': StockScreens.get_mid_cap_aggressive_stocks(),
    # 'Small Cap Aggressive Stock Screen': StockScreens.get_small_cap_aggressive_stocks()
    }
    return render_template('index.html', screens=screens)

@app.route('/data')
def display_data():
    query = request.args.get('query', '')
    data = {}
    if query:
        data = StockDetails(query).get_standardized_data()
    return render_template('data.html', data=data)

@app.route('/login')
def login():
    return '<h1>login feature is still in development, please comeback later</h1>'


@app.route('/time_period', methods=['POST'])
def update_stock_graph():
    pass




# Route to serve the HTML page
@app.route("/fiidii")
def fii_dii():
    return render_template("fiidii.html")

@app.route("/api/data")
def get_data():
    try:
        response = requests.get("https://raw.githubusercontent.com/HARI-KIRAN-REDDY/FIIDIIData/main/fii_dii.csv")
        df = pd.read_csv(io.StringIO(response.text))
        data = df.to_dict(orient="records")
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

