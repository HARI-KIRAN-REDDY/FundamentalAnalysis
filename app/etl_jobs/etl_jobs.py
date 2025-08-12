import requests
import pandas as pd
import numpy as np
import io
import json

def daily_bulk_deals_update_transformation():
    response = requests.get("https://raw.githubusercontent.com/HARI-KIRAN-REDDY/FIIDIIData/main/bulk.csv")
    df = pd.read_csv(io.StringIO(response.text))
    df.columns = df.columns.str.strip()

    df['Price'] = df['Trade Price / Wght. Avg. Price']
    df['Quantity'] = df['Quantity Traded']

    df['Trade Value'] = np.where(df['Buy/Sell'] == 'BUY',
                                 df['Price'] * df['Quantity'],
                                 df['Price'] * df['Quantity'] * -1) / 10000000

    net_quantity_value = round(df.groupby('Symbol', as_index=False)['Trade Value'].sum(), 2)
    net_quantity_value.rename(columns={'Trade Value': 'Net Trade Value'}, inplace=True)
    result = round(df.groupby(['Symbol', 'Client Name'], as_index=False)['Trade Value'].sum(), 2)
    result = result.merge(net_quantity_value, on='Symbol')
    result['Transaction'] = result['Trade Value'].apply(lambda x: 'Sold' if x <= 0 else 'Bought')
    filtered = result[(result['Trade Value'] >= 2) | (result['Trade Value'] <= -2)]
    json_output = filtered.to_dict(orient='records')
    print(json_output)
    return json.dumps(json_output, indent=2)
