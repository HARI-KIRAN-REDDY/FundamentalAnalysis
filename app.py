from flask import render_template, Flask, request, jsonify
import yfinance as yf
from app.api_operations.stocks_dict import symbol_to_company
from app.api_operations.StockDetails import StockDetails

app = Flask(__name__)

@app.route('/suggestions')
def get_suggestions():
    query = request.args.get('query', '').strip().lower()
    if not query or len(query) < 3:
        return jsonify([])  # Return empty if query is too short

    # Search both in stock symbols and company names
    matches = [
        {"symbol": symbol, "name": name}
        for symbol, name in symbol_to_company.items()
        if query in symbol.lower() or query in name.lower()
    ]

    return jsonify(matches[:5])


@app.route('/')
def home():
    return render_template('templates/index.html')

@app.route('/data')
def display_data():
    query = request.args.get('query', '')
    data = {}
    if query:
        data = StockDetails(query).get_standardized_data()
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=False)
