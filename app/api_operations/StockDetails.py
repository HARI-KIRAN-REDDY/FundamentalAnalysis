import yfinance as yf
from app.api_operations.custom_quires import *

class StockDetails:
    def __init__(self, stock_code):
        self.stock = yf.Ticker(stock_code)
        self.data = {}
        self.standardized_data = {}
        self.detail_keys = {
        'Company Details': ['website', 'industry', 'sector', 'longBusinessSummary', 'longName'],
        'Stock price detail': ['previousClose', 'open', 'dayLow', 'dayHigh', 'currentPrice', 'fiftyTwoWeekLow',
                               'fiftyTwoWeekHigh'],
        'Share Holding': ['marketCap', 'currency', 'enterpriseValue', 'floatShares', 'sharesOutstanding',
                            'impliedSharesOutstanding', 'heldPercentInsiders', 'heldPercentInstitutions'],
        'Ratios': ['bookValue', 'priceToBook', 'debtToEquity', 'revenuePerShare', 'returnOnAssets', 'returnOnEquity',
                  'trailingEps', 'forwardEps'],
        'Targets': ['currentPrice', 'targetLowPrice', 'targetHighPrice', 'targetMeanPrice', 'targetMedianPrice',
                   'numberOfAnalystOpinions', 'recommendationKey'],
        'Financials': ['grossProfits', 'freeCashflow', 'operatingCashflow', 'grossMargins' 'ebitdaMargins',
                      'operatingMargins']
        }

    def get_data(self):
        for detail_key in self.detail_keys:
            detail_dict = {}
            for d_key in self.detail_keys[detail_key]:
                detail_dict[d_key] = self.stock.info.get(d_key, 'N/A')
            self.data[detail_key] = detail_dict
        return self.data

    def get_standardized_data(self):
        self.get_data()
        print(self.data)
        self.standardized_data['Company Details'] = self.data.get('Company Details')
        self.stock_price_standardization()
        self.share_holding_standardization()
        self.targets_standardization()
        self.ratios_standardization()
        self.standardized_data['Financials'] = self.data.get('Financials')
        return self.standardized_data

    def stock_price_standardization(self):
        try:
            data = self.data.get('Stock price detail')
            updated_data = {}
            updated_data['Current Price'] = data.get('currentPrice')
            updated_data['Previous Close'] = data.get('previousClose')
            updated_data['Open'] = data.get('open')
            updated_data['Day Low'] = data.get('dayLow')
            updated_data['Day High'] = data.get('dayHigh')
            updated_data['52-Week Low'] = data.get('fiftyTwoWeekLow')
            updated_data['52-Week High'] = data.get('fiftyTwoWeekHigh')
            self.standardized_data['Stock price detail'] = updated_data
        except Exception as e:
            self.standardized_data['Stock price detail'] = data = self.data.get('Stock price detail')

    def share_holding_standardization(self):
        try:
            data = self.data.get('Share Holding')
            updated_data = {}
            try:
                updated_data['Market Capital'] = str(round(int(data.get('marketCap'))/10000000, 2))+'Crs'
            except Exception as E:
                updated_data['Market Capital'] = data.get('marketCap')
            updated_data['Shares Outstanding'] = data.get('sharesOutstanding')
            updated_data['Float Share'] = data.get('floatShares')
            try:
                updated_data['Enterprise Value'] = str(round(int(data.get('enterpriseValue'))/10000000, 2))+'Crs'
            except Exception as e:
                updated_data['Enterprise Value'] = data.get('enterpriseValue')
            try:
                updated_data['Promoters Holding'] = round(float(data.get('heldPercentInsiders'))*100, 2)
                updated_data['Institutions Holding'] = round(float(data.get('heldPercentInstitutions'))*100, 2)
                updated_data['Others Holding'] = round(100-(updated_data['Institutions Holding']+updated_data['Promoters Holding']),2)
            except Exception as e:
                updated_data['Promoters Holding'] = data.get('heldPercentInsiders')
                updated_data['Institutions Holding'] = data.get('heldPercentInstitutions')

            updated_data['Currency'] = data.get('currency')
            self.standardized_data['Share Holding'] = updated_data
        except Exception as e:
            self.standardized_data['Share Holding'] = self.data.get('Share Holding')

    def targets_standardization(self):
        try:
            data = self.data.get('Targets')
            updated_data = {}
            updated_data['Current Price'] = data.get('currentPrice')
            updated_data['Lowest Target Price'] = data.get('targetLowPrice')
            updated_data['Highest Target Price'] = data.get('targetHighPrice')
            updated_data['Average Target Price'] = data.get('targetMeanPrice')
            updated_data['Median Target Price'] = data.get('targetMedianPrice')
            updated_data['No of Analyst Opinions'] = data.get('numberOfAnalystOpinions')
            updated_data['Recommendation'] = data.get('recommendationKey')
            self.standardized_data['Targets'] = updated_data
        except Exception as e:
            self.standardized_data['Targets'] = self.data.get('Targets')

    def __ratio_helper_get_standardized_value(self, value, isRoe=False):
        try:
            if isRoe:
                return str(round(float(value)*100, 2))+'%'
            return round(float(value), 2)
        except Exception as e:
            return value


    def ratios_standardization(self):
        data = self.data.get('Ratios')
        updated_data = {}
        updated_data['Book Value'] = self.__ratio_helper_get_standardized_value(data.get('bookValue'))
        updated_data['Price to Book'] = self.__ratio_helper_get_standardized_value(data.get('priceToBook'))
        updated_data['Debt to Equity'] = self.__ratio_helper_get_standardized_value(data.get('debtToEquity'))
        updated_data['Revenue per Share'] = self.__ratio_helper_get_standardized_value(data.get('revenuePerShare'))
        updated_data['Return on Assets'] = self.__ratio_helper_get_standardized_value(data.get('returnOnAssets'), True)
        updated_data['Return on Equity'] = self.__ratio_helper_get_standardized_value(data.get('returnOnEquity'), True)
        updated_data['Trailing EPS'] = self.__ratio_helper_get_standardized_value(data.get('trailingEps'))
        updated_data['Forward EPS'] = self.__ratio_helper_get_standardized_value(data.get('forwardEps'))
        self.standardized_data['Ratios'] = updated_data

if __name__ == '__main__':
    # s= StockDetails('GPIL.NS').stock
    # split_factor = 1
    # sh = s.history(start='2000-01-01')
    # sh['Adj Close'] = 0  # Create a new column 'Adj Close' initialized to 0
    #
    # for index, row in sh.iterrows():
    #     if row['Stock Splits'] != 0:
    #         split_factor *= row['Stock Splits']
    #         print('SF: ', split_factor)
    #     sh.at[index, 'Adj Close'] = row['Close'] / split_factor
    #
    # print(sh[['Close', 'Stock Splits', 'Adj Close']])
    # sh.to_csv('stock_data.csv', index=False)
    # import yfinance as yf
    # response = yf.screen(indian_aggressive_small_cap)
    # print(response)
    pass





