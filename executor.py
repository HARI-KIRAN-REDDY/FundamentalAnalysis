from cashflow_data_getter import CashflowDataGetter
from cashflow_data_generator_plotly import CashflowGraphGenerator

def generate_cashflow_report(stock_code):
    # Fetch data
    data_getter = CashflowDataGetter(stock_code)
    operating_details = data_getter.get_operating_details()
    investment_details = data_getter.get_investment_details()
    financing_details = data_getter.get_financing_details()
    overall_details = data_getter.get_overall_details()

    # Generate graphs
    CashflowGraphGenerator(operating_details).plot_data()
    CashflowGraphGenerator(investment_details).plot_data()
    CashflowGraphGenerator(financing_details).plot_data()
    CashflowGraphGenerator(overall_details).plot_grouped_bar_graph()

    # Return the path of the generated HTML
    return f'html_files/{overall_details["company_code"]}_cashflow.html'
