import yfinance as yf
from yfinance import EquityQuery

#INDIA
ind_aggressive_small_cap = EquityQuery('and', [
    EquityQuery('is-in', ['exchange', 'NSI']),  # Corrected exchange list
    EquityQuery('GT', ['peratio.lasttwelvemonths', 30]),
    EquityQuery('LT', ['pegratio_5y', 1]),
    EquityQuery('LT', ['lastclosemarketcap.lasttwelvemonths', 50000000000])
])
ind_aggressive_mid_cap = EquityQuery('and', [
    EquityQuery('is-in', ['exchange', 'NSI']),  #
    EquityQuery('GT', ['peratio.lasttwelvemonths', 30]),
    EquityQuery('LT', ['pegratio_5y', 1]),
    EquityQuery('BTWN', ['lastclosemarketcap.lasttwelvemonths', 50000000000, 200000000000])
])

ind_value_large_cap = EquityQuery('AND', [
    EquityQuery('IS-IN', ['exchange', 'NSI']),
    EquityQuery('BTWN', ['peratio.lasttwelvemonths', 0, 21]),
    EquityQuery('LT', ['pegratio_5y', 1]),
    EquityQuery('LT', ['pricebookratio.quarterly', 2]),
    EquityQuery('GTE', ['lastclosemarketcap.lasttwelvemonths', 200000000000])
])

ind_value_mid_cap = EquityQuery('AND', [
    EquityQuery('IS-IN', ['exchange', 'NSI']),
    EquityQuery('BTWN', ['peratio.lasttwelvemonths', 0, 21]),
    EquityQuery('LT', ['pegratio_5y', 1]),
    EquityQuery('LT', ['pricebookratio.quarterly', 2]),
    EquityQuery('BTWN', ['lastclosemarketcap.lasttwelvemonths', 50000000000, 200000000000])
])




if __name__=='__main__':
    response = yf.screen(ind_aggressive_mid_cap, sortField='eodvolume')
    print(response)
