import pandas as pd

from connectors.stock_class import STOCK, RATIO_CALCULATOR, STOCK_INFO


def get_basic_stock_fundamentals(stock_list):
    """
    From a given list of stocks (tickers), it outputs the basic fundamental values.

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
        fundamental_results['momentum'].loc[i] = ratios.momentum()
        fundamental_results['div'].loc[i] = ratios.dividend_yield()
        fundamental_results['beta'].loc[i] = stock.beta()

    return fundamental_results


def stock_data_builder(ticker_id):
    """
    From a given list of stocks (tickers), it outputs all the fundamental values for each stock.

    :param list ticker_id: the stocks given by tickers
    :return pandas.DataFrame: fundamental values for each stock
    """
    attributes = ['price', 'momentum', 'fifty_two_week_low', 'fifty_two_week_high', 'currency', 'EV/EBITDA', 'EV/FCF',
                  'PER', 'PEG', 'PB', 'PS', 'ROCE', 'Reinvesting Rate', 'Annual Profit Growth Forecast', 'ROIC', 'ROA', 'ROE',
                  'Debt / EBITDA', 'Gross Margin', 'Operating Margin', 'Research and Development', 'Insiders % Held',
                  'Institutional % Held']
    ticker_id = [ticker.lower() for ticker in ticker_id]
    data_df = pd.DataFrame(data=None, columns=attributes, index=ticker_id)

    for ticker in ticker_id:
        stock = STOCK(ticker.lower())
        ratios = RATIO_CALCULATOR(ticker.lower())

        price = ratios.price()
        momentum = ratios.momentum()
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
        gross_margin = ratios.gross_margin()
        operating_margin = ratios.operating_margin()

        research_and_development = ratios.researchanddevelopment()
        insiderspercentheld = ratios.insiderspercentheld()
        institutionalpercentheld = ratios.institutionspercentheld()

        data = {'price': price, 'momentum':momentum, 'fifty_two_week_low': fifty_two_week_low, 'fifty_two_week_high': fifty_two_week_high,
                'currency': currency, 'EV/EBITDA': ev_ebitda_ratio, 'EV/FCF': ev_fcf_ratio, 'PER': pe_ratio,
                'PEG': peg_ratio, 'PB': pb_ratio, 'PS': ps_ratio, 'ROCE': roce, 'Reinvesting Rate': reinvesting_rate,
                'Annual Profit Growth Forecast': annual_profit_growth_forecast, 'ROIC': roic, 'ROA': roa, 'ROE': roe,
                'Debt / EBITDA': debt_ebitda_ratio, 'Gross Marging': gross_margin, 'Operating Marging': operating_margin,
                'Research and Development': research_and_development, 'Insiders % Held': insiderspercentheld,
                'Institutional % Held': institutionalpercentheld}

        data_df.loc[ticker] = data

    return data_df


def filter_stocks(ratios_filter, stocks_df):
    """
    It filters the stock values that fulfil the given ratios filters.

    :param dict ratios_filter: dictionary containing the fundamental analysis ratios to be filtered. For example:
    ratios_filter = {'roce': 0.2, 'ev_fcf': 45, 'momentum': 1, 'beta': 2}
    :param pandas.DataFrame stocks_df: stock values containing fundamental analysis information
    :return pandas.DataFrame: stock values but filtered by the ratios given
    """
    selected_values = stocks_df[(stocks_df['roce'] > ratios_filter['roce']) & (stocks_df['ev_fcf'] < ratios_filter['ev_fcf'])
                                & (stocks_df['momentum'] < ratios_filter['momentum']) & (stocks_df['beta'] < ratios_filter['beta'])]

    return selected_values

def assets_info(ticker_id_list):
    """
        From a given list of stocks (tickers), it outputs some info.

        :param list ticker_id: the stocks given by tickers
        :return pandas.DataFrame: asset info
        """
    attributes = ['name', 'website', 'region', 'currency', 'market', 'sector', 'industry', 'full time employees',
                  'business summary']
    ticker_id = [ticker.lower() for ticker in ticker_id_list]
    data_df = pd.DataFrame(data=None, columns=attributes, index=ticker_id)

    for ticker in ticker_id:
        stock = STOCK(ticker.lower())
        info = STOCK_INFO(ticker.lower())

        name = info.name()
        website = info.website()
        region = info.region()
        currency = info.currency()
        market = info.market()
        sector = info.sector()
        industry = info.industry()
        fulltimeemployees = info.fulltimeemployees()
        businesssummary = info.longbusinesssummary()

        data = {'name': name, 'website': website, 'region': region, 'currency': currency, 'market': market,
                'sector': sector, 'industry': industry, 'full time employees': fulltimeemployees,
                'business summary': businesssummary
                }

        data_df.loc[ticker] = data

    return data_df
