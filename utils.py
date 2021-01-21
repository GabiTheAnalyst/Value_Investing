import pandas as pd

from Personal.stock_class import STOCK


def get_stock_fundamentals(stock_list):
    fundamental_ratios = ['roce', 'ev_fcf', 'momentum', 'div', 'beta']
    fundamental_results = pd.DataFrame(data=None, columns=fundamental_ratios, index=stock_list)

    for i in stock_list:
        stock = STOCK(i.lower())
        fundamental_results['roce'].loc[i] = stock.get_roce()
        fundamental_results['ev_fcf'].loc[i] = stock.ev_fcf()
        fundamental_results['momentum'].loc[i] = stock.momentum()
        fundamental_results['div'].loc[i] = stock.dividend_yield()
        fundamental_results['beta'].loc[i] = stock.beta()

    return fundamental_results


def filter_stocks(ratios_filter, stocks_df):
    selected_values = stocks_df[(stocks_df['roce'] > ratios_filter['roce']) & (stocks_df['ev_fcf'] < ratios_filter['ev_fcf'])
                                & (stocks_df['momentum'] < ratios_filter['momentum']) & (stocks_df['beta'] < ratios_filter['beta'])]

    return selected_values
