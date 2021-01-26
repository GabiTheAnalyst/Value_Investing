import yahooquery as yq

aapl = yq.Ticker('aapl')
# income_stat = aapl.income_statement()

class STOCK:

    def __init__(self, ticker_id):
        self.ticker = yq.Ticker(ticker_id)
        self.ticker_id = ticker_id

    def balance_sheet(self):
        """
        keys:
        ['asOfDate', 'periodType', 'AccountsPayable', 'AccountsReceivable',
       'AccumulatedDepreciation', 'AllowanceForDoubtfulAccountsReceivable',
       'AvailableForSaleSecurities', 'CapitalStock', 'CashAndCashEquivalents',
       'CashCashEquivalentsAndShortTermInvestments', 'CashEquivalents',
       'CashFinancial', 'CommercialPaper', 'CommonStock', 'CommonStockEquity',
       'CurrentAccruedExpenses', 'CurrentAssets', 'CurrentDebt',
       'CurrentDebtAndCapitalLeaseObligation', 'CurrentDeferredLiabilities',
       'CurrentDeferredRevenue', 'CurrentLiabilities',
       'GainsLossesNotAffectingRetainedEarnings', 'Goodwill',
       'GoodwillAndOtherIntangibleAssets', 'GrossAccountsReceivable',
       'GrossPPE', 'Inventory', 'InvestedCapital',
       'InvestmentinFinancialAssets', 'InvestmentsAndAdvances',
       'LandAndImprovements', 'Leases', 'LongTermDebt',
       'LongTermDebtAndCapitalLeaseObligation', 'MachineryFurnitureEquipment',
       'NetDebt', 'NetPPE', 'NetTangibleAssets',
       'NonCurrentDeferredLiabilities', 'NonCurrentDeferredRevenue',
       'NonCurrentDeferredTaxesLiabilities', 'OrdinarySharesNumber',
       'OtherCurrentAssets', 'OtherCurrentBorrowings',
       'OtherCurrentLiabilities', 'OtherIntangibleAssets',
       'OtherNonCurrentAssets', 'OtherNonCurrentLiabilities',
       'OtherReceivables', 'OtherShortTermInvestments', 'Payables',
       'PayablesAndAccruedExpenses', 'Properties', 'Receivables',
       'RetainedEarnings', 'ShareIssued', 'StockholdersEquity',
       'TangibleBookValue', 'TotalAssets', 'TotalCapitalization', 'TotalDebt',
       'TotalEquityGrossMinorityInterest',
       'TotalLiabilitiesNetMinorityInterest', 'TotalNonCurrentAssets',
       'TotalNonCurrentLiabilitiesNetMinorityInterest',
       'TradeandOtherPayablesNonCurrent', 'WorkingCapital']
        """
        return self.ticker.balance_sheet()

    def cash_flow(self):
        """
        keys:
        ['asOfDate', 'periodType', 'BeginningCashPosition', 'CapitalExpenditure',
       'CashDividendsPaid', 'CashFlowFromContinuingFinancingActivities',
       'ChangeInAccountPayable', 'ChangeInCashSupplementalAsReported',
       'ChangeInInventory', 'ChangeInWorkingCapital',
       'ChangesInAccountReceivables', 'CommonStockIssuance',
       'DeferredIncomeTax', 'DepreciationAndAmortization', 'EndCashPosition',
       'FreeCashFlow', 'InvestingCashFlow', 'NetIncome',
       'NetOtherFinancingCharges', 'NetOtherInvestingChanges',
       'OperatingCashFlow', 'OtherNonCashItems', 'PurchaseOfBusiness',
       'PurchaseOfInvestment', 'RepaymentOfDebt', 'RepurchaseOfCapitalStock',
       'SaleOfInvestment', 'StockBasedCompensation']
        """
        return self.ticker.cash_flow()

    def income_statement(self):
        """
        keys:
        ['asOfDate', 'periodType', 'BasicAverageShares', 'BasicEPS',
       'CostOfRevenue', 'DilutedAverageShares', 'DilutedEPS',
       'DilutedNIAvailtoComStockholders', 'EBIT', 'EBITDA', 'GrossProfit',
       'InterestExpense', 'InterestExpenseNonOperating', 'InterestIncome',
       'InterestIncomeNonOperating', 'NetIncome',
       'NetIncomeCommonStockholders', 'NetIncomeContinuousOperations',
       'NetIncomeFromContinuingAndDiscontinuedOperation',
       'NetIncomeFromContinuingOperationNetMinorityInterest',
       'NetIncomeIncludingNoncontrollingInterests', 'NetInterestIncome',
       'NetNonOperatingInterestIncomeExpense', 'NormalizedEBITDA',
       'NormalizedIncome', 'OperatingExpense', 'OperatingIncome',
       'OperatingRevenue', 'OtherIncomeExpense',
       'OtherNonOperatingIncomeExpenses', 'PretaxIncome',
       'ReconciledCostOfRevenue', 'ReconciledDepreciation',
       'ResearchAndDevelopment', 'SellingGeneralAndAdministration',
       'TaxEffectOfUnusualItems', 'TaxProvision', 'TaxRateForCalcs',
       'TotalExpenses', 'TotalOperatingIncomeAsReported', 'TotalRevenue']
        """
        return self.ticker.income_statement()

    def valuation_measures(self):
        """
        keys:
        ['asOfDate', 'periodType', 'EnterpriseValue',
       'EnterprisesValueEBITDARatio', 'EnterprisesValueRevenueRatio',
       'ForwardPeRatio', 'MarketCap', 'PbRatio', 'PeRatio', 'PegRatio',
       'PsRatio']
        """
        return self.ticker.valuation_measures

    def all_financial_data(self):
        """
        keys:
        ['asOfDate', 'periodType', 'AccountsPayable', 'AccountsReceivable',
       'AccumulatedDepreciation', 'AllowanceForDoubtfulAccountsReceivable',
       'AvailableForSaleSecurities', 'BasicAverageShares', 'BasicEPS',
       'BeginningCashPosition', 'CapitalExpenditure', 'CapitalStock',
       'CashAndCashEquivalents', 'CashCashEquivalentsAndShortTermInvestments',
       'CashDividendsPaid', 'CashEquivalents', 'CashFinancial',
       'CashFlowFromContinuingFinancingActivities', 'ChangeInAccountPayable',
       'ChangeInCashSupplementalAsReported', 'ChangeInInventory',
       'ChangeInWorkingCapital', 'ChangesInAccountReceivables',
       'CommercialPaper', 'CommonStock', 'CommonStockEquity',
       'CommonStockIssuance', 'CostOfRevenue', 'CurrentAccruedExpenses',
       'CurrentAssets', 'CurrentDebt', 'CurrentDebtAndCapitalLeaseObligation',
       'CurrentDeferredLiabilities', 'CurrentDeferredRevenue',
       'CurrentLiabilities', 'DeferredIncomeTax',
       'DepreciationAndAmortization', 'DilutedAverageShares', 'DilutedEPS',
       'DilutedNIAvailtoComStockholders', 'EBIT', 'EndCashPosition',
       'EnterpriseValue', 'EnterprisesValueEBITDARatio',
       'EnterprisesValueRevenueRatio', 'ForwardPeRatio', 'FreeCashFlow',
       'GainsLossesNotAffectingRetainedEarnings', 'Goodwill',
       'GoodwillAndOtherIntangibleAssets', 'GrossAccountsReceivable',
       'GrossPPE', 'GrossProfit', 'InterestExpense',
       'InterestExpenseNonOperating', 'InterestIncome',
       'InterestIncomeNonOperating', 'Inventory', 'InvestedCapital',
       'InvestingCashFlow', 'InvestmentinFinancialAssets',
       'InvestmentsAndAdvances', 'LandAndImprovements', 'Leases',
       'LongTermDebt', 'LongTermDebtAndCapitalLeaseObligation',
       'MachineryFurnitureEquipment', 'MarketCap', 'NetDebt', 'NetIncome',
       'NetIncomeCommonStockholders',
       'NetIncomeContinuousOperations',
       'NetIncomeFromContinuingAndDiscontinuedOperation',
       'NetIncomeFromContinuingOperationNetMinorityInterest',
       'NetIncomeIncludingNoncontrollingInterests', 'NetInterestIncome',
       'NetNonOperatingInterestIncomeExpense', 'NetOtherFinancingCharges',
       'NetOtherInvestingChanges', 'NetPPE', 'NetTangibleAssets',
       'NonCurrentDeferredLiabilities', 'NonCurrentDeferredRevenue',
       'NonCurrentDeferredTaxesLiabilities', 'NormalizedEBITDA',
       'NormalizedIncome', 'OperatingCashFlow', 'OperatingExpense',
       'OperatingIncome', 'OperatingRevenue', 'OrdinarySharesNumber',
       'OtherCurrentAssets', 'OtherCurrentBorrowings',
       'OtherCurrentLiabilities', 'OtherIncomeExpense',
       'OtherIntangibleAssets', 'OtherNonCashItems', 'OtherNonCurrentAssets',
       'OtherNonCurrentLiabilities', 'OtherNonOperatingIncomeExpenses',
       'OtherReceivables', 'OtherShortTermInvestments', 'Payables',
       'PayablesAndAccruedExpenses', 'PbRatio', 'PeRatio', 'PegRatio',
       'PretaxIncome', 'Properties', 'PsRatio', 'PurchaseOfBusiness',
       'PurchaseOfInvestment', 'Receivables', 'ReconciledCostOfRevenue',
       'ReconciledDepreciation', 'RepaymentOfDebt', 'RepurchaseOfCapitalStock',
       'ResearchAndDevelopment', 'RetainedEarnings', 'SaleOfInvestment',
       'SellingGeneralAndAdministration', 'ShareIssued',
       'StockBasedCompensation', 'StockholdersEquity', 'TangibleBookValue',
       'TaxEffectOfUnusualItems', 'TaxProvision', 'TaxRateForCalcs',
       'TotalAssets', 'TotalCapitalization', 'TotalDebt',
       'TotalEquityGrossMinorityInterest', 'TotalExpenses',
       'TotalLiabilitiesNetMinorityInterest', 'TotalNonCurrentAssets',
       'TotalNonCurrentLiabilitiesNetMinorityInterest',
       'TotalOperatingIncomeAsReported', 'TotalRevenue',
       'TradeandOtherPayablesNonCurrent', 'WorkingCapital']
        """
        return self.ticker.all_financial_data()

    def summary_detail(self):
        """
        {'aapl': {'maxAge': 1,
          'priceHint': 2,
          'previousClose': 132.03,
          'open': 133.8,
          'dayLow': 133.59,
          'dayHigh': 136.4,
          'regularMarketPreviousClose': 132.03,
          'regularMarketOpen': 133.8,
          'regularMarketDayLow': 133.59,
          'regularMarketDayHigh': 136.4,
          'dividendRate': 0.82,
          'dividendYield': 0.0062,
          'exDividendDate': '2020-11-06 01:00:00',
          'payoutRatio': 0.24239999,
          'fiveYearAvgDividendYield': 1.46,
          'beta': 1.283613,
          'trailingPE': 41.582317,
          'forwardPE': 31.210527,
          'volume': 77563827,
          'regularMarketVolume': 77563827,
          'averageVolume': 107957417,
          'averageVolume10days': 96812442,
          'averageDailyVolume10Day': 96812442,
          'bid': 136.18,
          'ask': 136.2,
          'bidSize': 1100,
          'askSize': 1100,
          'marketCap': 2294529916928,
          'fiftyTwoWeekLow': 53.1525,
          'fiftyTwoWeekHigh': 138.79,
          'priceToSalesTrailing12Months': 8.358486,
          'fiftyDayAverage': 128.2497,
          'twoHundredDayAverage': 116.33259,
          'trailingAnnualDividendRate': 0.795,
          'trailingAnnualDividendYield': 0.006021359,
          'currency': 'USD',
          'fromCurrency': None,
          'toCurrency': None,
          'lastMarket': None,
          'algorithm': None,
          'tradeable': False}}
        """
        summary_detail = self.ticker.summary_detail

        return summary_detail

    def momentum(self):
        price_history_last_year = self.ticker.history(period='1y')['close']
        momentum = (price_history_last_year[-1] / price_history_last_year[0]) - 1

        return momentum

    def beta(self):
        module = 'defaultKeyStatistics'
        values = self.ticker.get_modules(module)
        beta = values[self.ticker_id]['beta']

        return beta




class RATIO_CALCULATOR(STOCK):

    def __init__(self, ticker_id):
        self.stock = STOCK(ticker_id.lower())
        self.ticker_id = ticker_id.lower()

    def dividend_yield(self):
        try:
            dividend_yield = self.stock.summary_detail()[self.ticker_id]['dividendYield']
        except:
            dividend_yield = None

        return dividend_yield

    def ev_fcf(self):
        ev = self.stock.all_financial_data()['EnterpriseValue'][-1]
        fcf = self.stock.all_financial_data()['FreeCashFlow'][-1]

        return ev / fcf

    def pe_ratio(self):
        pe_ratio = self.stock.valuation_measures()['PeRatio'].dropna().iloc[-1]

        return pe_ratio

    def peg_ratio(self):
        peg_ratio = self.stock.valuation_measures()['PegRatio'].dropna().iloc[-1]

        return peg_ratio

    def pb_ratio(self):
        pb_ratio = self.stock.valuation_measures()['PbRatio'].dropna().iloc[-1]

        return pb_ratio

    def ps_ratio(self):
        ps_ratio = self.stock.valuation_measures()['PsRatio'].dropna().iloc[-1]

        return ps_ratio

    def roce(self):
        ebit = self.stock.income_statement()[self.stock.income_statement().periodType == '12M'].iloc[-1]['EBIT']  # Also: self.stock.all_financial_data()['EBIT'][-1]
        total_assets = self.stock.balance_sheet()[self.stock.balance_sheet().periodType == '12M'].iloc[-1]['TotalAssets']
        current_liabilities = self.stock.balance_sheet()[self.stock.balance_sheet().periodType == '12M'].iloc[-1]['CurrentLiabilities']
        roce = ebit / (total_assets - current_liabilities)

        return roce

    def roic(self):
        operating_income = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['OperatingIncome'].iloc[-1]
        tax_rate = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['TaxRateForCalcs'].iloc[-1]

        average_invested_capital = self.stock.balance_sheet()[self.stock.balance_sheet().periodType == '12M']['InvestedCapital'][-2:,].sum() / 2

        roic = operating_income * (1 + tax_rate) / average_invested_capital

        return roic

    def roa(self):
        net_income = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['NetIncome'].iloc[-1]
        average_total_assets = self.stock.balance_sheet()[self.stock.balance_sheet().periodType == '12M']['TotalAssets'][-2:,].sum() / 2

        roa = net_income / average_total_assets

        return roa

    def roe(self):
        net_income = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['NetIncome'].iloc[-1]
        average_stock_holder_equity = self.stock.balance_sheet()[self.stock.balance_sheet().periodType == '12M']['StockholdersEquity'][-2:,].sum() / 2

        roe = net_income / average_stock_holder_equity

        return roe

    def reinvesting_rate(self):
        """
        The reinvesting rate is calculated as the division between Investing cash flow and Operating cash flow. However,
        it may happen that Investing cash flow is positive due to sales of investments or net other investment changes.
        Hence, I have deducted the positive values from Operating cash flow so only proper investing values (negative)
        are taking into account.

        :return: Reinvesting rate
        """
        operating_cash_flow = self.stock.cash_flow()[self.stock.cash_flow().periodType == '12M']['OperatingCashFlow']

        investing_cash_flow = self.stock.cash_flow()[self.stock.cash_flow().periodType == '12M']['InvestingCashFlow']
        sale_of_investment = self.stock.cash_flow()[self.stock.cash_flow().periodType == '12M']['SaleOfInvestment']
        try:
            net_other_investment_changes = self.stock.cash_flow()[self.stock.cash_flow().periodType == '12M']['NetOtherInvestingChanges'].fillna(0)
            net_other_investment_changes = net_other_investment_changes.apply(lambda x: 0 if x < 0 else x)
        except:
            net_other_investment_changes = sale_of_investment.copy()
            net_other_investment_changes.loc[:] = 0

        only_investing_cash_flow = investing_cash_flow - sale_of_investment - net_other_investment_changes

        reinvesting_rate = (abs(only_investing_cash_flow) / operating_cash_flow).mean()

        return reinvesting_rate

    def debt_ebitda_ratio(self):
        total_debt = self.stock.balance_sheet()[self.stock.balance_sheet().periodType== '12M']['TotalDebt'].iloc[-1]
        ebitda = self.stock.income_statement()['EBITDA'].iloc[-1]

        debt_ebitda_ratio = total_debt / ebitda

        return debt_ebitda_ratio

    def gross_marging(self):
        total_revenue = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['TotalRevenue'].iloc[-1]
        gross_profit = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['GrossProfit'].iloc[-1]

        gross_marging = gross_profit / total_revenue

        return gross_marging

    def operating_marging(self):
        """
        The operating income might be either positive or negative (profit or loss
        :return:
        """
        total_revenue = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['TotalRevenue'].iloc[-1]
        operating_income = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['OperatingIncome'].iloc[-1]

        operating_maring = operating_income / total_revenue

        return operating_maring

if __name__== '__main__':
    stock = STOCK("NVDA".lower())
    # beta = stock.beta()
    # ev_ebitda = stock.valuation_measures()['EnterprisesValueEBITDARatio']
    # ebitda = stock.income_statement()['EBITDA']
    # ev = stock.valuation_measures()['EnterpriseValue']
    ratios = RATIO_CALCULATOR('NVDA')
    # ratios.roce()
    ratios.reinvesting_rate()


