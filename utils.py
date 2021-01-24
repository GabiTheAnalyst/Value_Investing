import pandas as pd

from stock_class import STOCK, RATIO_CALCULATOR


def get_stock_fundamentals(stock_list):
    """
    :param list stock_list: list with tickers from stock values

    :return pandas.DataFrame: stock values containing the fundamental analysis ratios
    """
    fundamental_ratios = ['roce', 'ev_fcf', 'momentum', 'div', 'beta']
    fundamental_results = pd.DataFrame(data=None, columns=fundamental_ratios, index=stock_list)

    for i in stock_list:
        stock = STOCK(i.lower())
        ratios = RATIO_CALCULATOR(i.lower())
        fundamental_results['roce'].loc[i] = ratios.roce()
        fundamental_results['ev_fcf'].loc[i] = ratios.ev_fcf()
        fundamental_results['momentum'].loc[i] = stock.momentum()
        fundamental_results['div'].loc[i] = ratios.dividend_yield()
        fundamental_results['beta'].loc[i] = stock.beta()

    return fundamental_results


def filter_stocks(ratios_filter, stocks_df):
    """
   :param dict ratios_filter: dictionary containing the fundamental analysis ratios to be filtered
    :param pandas.DataFrame stocks_df: stock values containing fundamental analysis information
    :return pandas.DataFrame: stock values but filtered by the ratios given
    """
    selected_values = stocks_df[(stocks_df['roce'] > ratios_filter['roce']) & (stocks_df['ev_fcf'] < ratios_filter['ev_fcf'])
                                & (stocks_df['momentum'] < ratios_filter['momentum']) & (stocks_df['beta'] < ratios_filter['beta'])]

    return selected_values
