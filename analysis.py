from utils import get_basic_stock_fundamentals, filter_stocks, stock_data_builder, assets_info

if __name__ == '__main__':
    # Basic fundamentals for a list of stocks
    stock_list = ['aapl', 'AMZN']
    stocks_df = get_basic_stock_fundamentals(stock_list)

    # Filter stock values by ratios filter
    ratios_filter = {'roce': 0.2, 'ev_fcf': 45, 'momentum': 1, 'beta': 2}
    stocks_filtered = filter_stocks(ratios_filter, stocks_df)

    # Get the fundamentals for one or more stock values
    all_fundamentals = stock_data_builder(['aapl'])
    df = stock_data_builder(['aapl', 'AMZN', 'apc.f'])

    # Get assets info
    assets_info = assets_info(stock_list)
