from flask import Flask, render_template, request, send_from_directory
from executor import generate_cashflow_report

app = Flask(__name__)

# Home route to render input form
@app.route('/')
def index():
    return render_template('index.html')

# Generate report route
@app.route('/generate', methods=['POST'])
def generate():
    stock_code = request.form['stock_code']  # Get stock code from form
    html_path = generate_cashflow_report(stock_code)  # Call executor logic
    return f"<a href='/static/{html_path}' target='_blank'>View Report</a>"  # Provide download link

if __name__ == "__main__":
    app.run(debug=True)
