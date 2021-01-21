import pandas as pd

from Personal.stock_class import STOCK
from Personal.utils import get_stock_fundamentals, filter_stocks
if __name__ == '__main__':
    stock_list = ['aapl', 'AMZN']

    stocks_df = get_stock_fundamentals(stock_list)

    ratios_filter = {'roce': 0.2, 'ev_fcf': 45, 'momentum': 1, 'beta': 2}

    stocks_filtered = filter_stocks(ratios_filter, stocks_df)

