from app.api_operations.custom_quires import *
import yfinance as yf
class StockScreens:
    @staticmethod
    def get_large_cap_value_stocks():
        response = yf.screen(ind_value_large_cap).get('quotes')
        return response

    @staticmethod
    def get_mid_cap_value_stocks():
        response = yf.screen(ind_value_mid_cap).get('quotes')
        return response

    @staticmethod
    def get_small_cap_aggressive_stocks():
        response = yf.screen(ind_aggressive_small_cap, sortField='pegratio_5y').get('quotes')
        return response

    @staticmethod
    def get_mid_cap_aggressive_stocks():
        response = yf.screen(ind_aggressive_mid_cap, sortField='pegratio_5y').get('quotes')
        return response
