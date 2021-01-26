import pandas as pd

from stock_class import STOCK, RATIO_CALCULATOR

def stock_data_builder(ticker_id):
    attributes = ['price', 'fifty_two_week_low', 'fifty_two_week_high', 'currency', 'EV/EBITDA', 'EV/FCF',
                  'PER', 'PEG', 'PB', 'PS', 'ROCE', 'Reinvesting Rate', 'Annual Profit Growth Forecast', 'ROIC', 'ROA', 'ROE',
                  'Debt / EBITDA', 'Gross Marging', 'Operating Marging']
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
        reinvesting_rate = ratios.reinvesting_rate()
        annual_profit_growth_forecast = roce * reinvesting_rate
        roic = ratios.roic()
        roa = ratios.roa()
        roe = ratios.roe()

        debt_ebitda_ratio = ratios.debt_ebitda_ratio()
        gross_marging = ratios.gross_marging()
        operating_marging = ratios.operating_marging()

        data = {'price': price, 'fifty_two_week_low': fifty_two_week_low, 'fifty_two_week_high': fifty_two_week_high,
                'currency': currency, 'EV/EBITDA': ev_ebitda_ratio, 'EV/FCF': ev_fcf_ratio, 'PER': pe_ratio,
                'PEG': peg_ratio, 'PB': pb_ratio, 'PS': ps_ratio, 'ROCE': roce, 'Reinvesting Rate': reinvesting_rate,
                'Annual Profit Growth Forecast': annual_profit_growth_forecast, 'ROIC': roic, 'ROA': roa, 'ROE': roe,
                'Debt / EBITDA': debt_ebitda_ratio, 'Gross Marging': gross_marging, 'Operating Marging': operating_marging}

        data_df.loc[ticker] = data

    return data_df

if __name__ == '__main__':
    df = stock_data_builder(['aapl', 'AMZN', 'apc.f'])
