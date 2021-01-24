import pandas as pd

from stock_class import STOCK, RATIO_CALCULATOR

def stock_data_builder(ticker_id):
    attributes = ['price', 'fifty_two_week_low', 'fifty_two_week_high', 'currency', 'EV/EBITDA', 'EV/FCF',
                  'PER', 'PEG', 'PB', 'PS', 'ROCE', 'ROIC', 'ROA', 'ROE']
    ticker_id = [ticker.lower() for ticker in ticker_id]
    data_df = pd.DataFrame(data=None, columns=attributes, index=ticker_id)

    for ticker in ticker_id:
        stock = STOCK(ticker.lower())
        ratios = RATIO_CALCULATOR(ticker.lower())

        price = stock.summary_detail()[ticker]['previousClose']
        fifty_two_week_low = stock.summary_detail()[ticker]['fiftyTwoWeekLow']
        fifty_two_week_high = stock.summary_detail()[ticker]['fiftyTwoWeekHigh']
        currency = stock.summary_detail()[ticker]['currency']

        ev_ebitda_ratio = stock.valuation_measures()['EnterprisesValueEBITDARatio'].dropna()[-1]
        ev_fcf_ratio = ratios.ev_fcf()

        pe_ratio = ratios.pe_ratio()
        peg_ratio = ratios.peg_ratio()
        pb_ratio = ratios.pb_ratio()
        ps_ratio = ratios.ps_ratio()

        roce = ratios.roce()
        roic = ratios.roic()
        roa = ratios.roa()
        roe = ratios.roe()

        data = {'price': price, 'fifty_two_week_low': fifty_two_week_low, 'fifty_two_week_high': fifty_two_week_high,
                'currency': currency, 'EV/EBITDA': ev_ebitda_ratio, 'EV/FCF': ev_fcf_ratio, 'PER': pe_ratio,
                'PEG': peg_ratio, 'PB': pb_ratio, 'PS': ps_ratio, 'ROCE': roce, 'ROIC': roic, 'ROA': roa, 'ROE': roe}

        data_df.loc[ticker] = data

    return data_df

if __name__ == '__main__':
    df = stock_data_builder(['aapl', 'AMZN', 'apc.f'])
