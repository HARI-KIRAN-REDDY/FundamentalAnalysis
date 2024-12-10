import plotly.graph_objects as go
import plotly.io as pio
import numpy as np


class CashflowGraphGenerator:
    def __init__(self, details):
        print(details)
        self.years = details['years']
        self.data_items = details['data_items']
        self.net_cashflow = details['net cashflow']
        self.company_code = details['company_code']
        self.cash_flow_type = details['cash_flow_type']

    def add_to_html(self, fig):
        pio.write_html(fig, file=f"temp.html", auto_open=False)
        with open('temp.html', 'r', encoding='utf-8') as temp_file:
            with open(f'html_files/{self.company_code}_cashflow.html', 'a', encoding='utf-8') as report:
                report.write(temp_file.read())


    def plot_data(self):
        fig = go.Figure()

        # Add stacked bar traces for each data item
        for item, values in self.data_items.items():
            fig.add_trace(go.Bar(
                x=self.years,
                y=values,
                name=item,
                text=[f"{v}" for v in values],  # Optional: show values on hover
                hoverinfo='x+y+text'
            ))

        # Add a line for net cashflow
        fig.add_trace(go.Scatter(
            x=self.years,
            y=self.net_cashflow,
            mode='lines+markers',
            name=f'Net {self.cash_flow_type}',
            line=dict(color='black', width=3),
            marker=dict(size=8),
            hoverinfo='x+y'
        ))

        # Update layout for better visualization
        fig.update_layout(
            title=f'{self.cash_flow_type}, {self.company_code}',
            xaxis_title='Financial Year',
            yaxis_title='Rupees in Crs',
            barmode='relative',  # Stack bars
            template='seaborn',
            legend_title='DataItems'
        )
        self.add_to_html(fig)


    def plot_grouped_bar_graph(self):
        bar_traces = []
        for label, values in self.data_items.items():
            bar_traces.append(
                go.Bar(
                    x=self.years,
                    y=values,
                    name=label,
                    marker=dict(
                        pattern=dict(
                            shape="/"  # Options: "/" "\" "x" "|" "-" "+" "." "none"
                        )
                    )
                )
            )

        # Create the line trace for net cashflow
        line_trace = go.Scatter(
            x=self.years,
            y=self.net_cashflow,
            mode='lines+markers',
            name='Net Cashflow',
            line=dict(color='black', width=2)
        )

        # Combine all traces
        fig = go.Figure(data=bar_traces + [line_trace])

        # Update layout for better visualization
        fig.update_layout(
            title=f"{self.cash_flow_type} of {self.company_code}",
            xaxis_title="Years",
            yaxis_title="Cash Flow in Crs",
            barmode='group',  # Grouped bar chart
            legend=dict(title="Overall cashflow"),
            template="seaborn"
        )
        self.add_to_html(fig)