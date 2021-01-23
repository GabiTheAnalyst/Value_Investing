import pandas as pd

from stock_class import STOCK

def stock_data_builder(ticker_id):
    stock = STOCK(ticker_id.lower())
    price = stock.summary_detail()[ticker_id]['previousClose']
    fifty_two_week_low = stock.summary_detail()[ticker_id]['fiftyTwoWeekLow']
    fifty_two_week_high = stock.summary_detail()[ticker_id]['fiftyTwoWeekHigh']
    currency = stock.summary_detail()[ticker_id]['currency']

    data = {'price': price, 'fifty_two_week_low': fifty_two_week_low, 'fifty_two_week_high': fifty_two_week_high,
            'currency': currency}
    data_df = pd.DataFrame(data=data, index=[ticker_id])

    return data_df

if __name__ == '__main__':
    df = stock_data_builder('aapl')