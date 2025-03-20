import yfinance as yf

import plotly.graph_objects as go
import os


def plot_graph(stock_code, time_period):
    intervals = {'1d': '2m',
                 '5d': '1h',
                 '1mo': '1h',
                 '3mo': '1d',
                 '6mo': '1d',
                 'ytd': '5d',
                 '1y': '5d',
                 '2y': '5d',
                 '5y': '1wk',
                 '10y': '3mo',
                 'max': '3mo'}
    df = yf.download(stock_code, period=time_period, interval=intervals[time_period])
    df = df.tz_convert('Asia/Kolkata')
    max_close = round(df.iloc[:, 0].max(), 2)
    min_close = round(df.iloc[:, 0].min(), 2)

    if df.empty:
        print("No data available for the given stock and time period.")
        return

    fig = go.Figure()

    # Add a line graph for 'Close' price
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df.iloc[:, 0],
        mode='lines',
        name="Stock Price",
        line=dict(color='dodgerblue', width=2.5)  # Slightly thicker line for better visibility
    ))

    # Set layout with a professional template
    fig.update_layout(
        title=dict(text=f"{stock_code} Stock Price", font=dict(size=22), x=0.5),
        xaxis=dict(
            title="Date",
            showgrid=True,
            gridcolor="rgba(211, 211, 211, 0.5)",  # Light gray grid lines
            tickangle=45,
            type='date',
            showline=True,
            linewidth=1,
            linecolor='gray'
        ),
        yaxis=dict(
            title="Close Price",
            showgrid=True,
            gridcolor="rgba(211, 211, 211, 0.5)",  # Light gray grid
            zeroline=True,
            zerolinewidth=1,
            zerolinecolor="gray"
        ),
        template="seaborn",  # Professional look (Try "plotly_dark", "ggplot2", etc.)
        hovermode="x unified",
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="black"),
        margin=dict(l=40, r=40, t=60, b=40),  # Adjust margins for better fit
    )

    fig.show()
    # Define the output file path
    output_file = os.path.join("templates/static", f"{stock_code}.html")

    # Save the figure as an HTML file
    fig.write_html(output_file)

    # Read the existing HTML content
    with open(output_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Add max & min close price info at the bottom center
    html_content = f"""
    <html>
    <head>
        <title>{stock_code} Stock Price</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 0;
                position: relative;
            }}
            .footer {{
                position: absolute;
                bottom: 10px;
                left: 50%;
                transform: translateX(-50%);
                font-size: 18px;
                font-weight: bold;
                background: rgba(0, 0, 0, 0.8);
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
            }}
        </style>
    </head>
    <body>
        {html_content}  <!-- Embed original Plotly graph -->
        <div class="footer">
            {time_period} High: {max_close} | {time_period} Low: {min_close}
        </div>
    </body>
    </html>
    """

    # Write back the modified HTML content
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    return f"{stock_code}.html"


plot_graph('HINDALCO.NS', '1d')
