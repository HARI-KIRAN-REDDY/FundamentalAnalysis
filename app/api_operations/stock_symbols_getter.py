import csv

def save_symbol_to_company_dict(csv_file_path):
    # Dictionary to hold the symbol and company name
    symbol_to_company = {}

    # Read the CSV file
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) > 1:  # Ensure the row has enough columns
                symbol = (row[0]+'.NS').strip()
                company_name = row[1].strip()
                symbol_to_company[symbol] = company_name

    # Write the dictionary to a Python file
    with open('stocks_dict.py', 'w', encoding='utf-8') as py_file:
        py_file.write('symbol_to_company = ' + str(symbol_to_company) + '\n')

# Example usage
csv_file_path = 'EQUITY_L.csv'
save_symbol_to_company_dict(csv_file_path)