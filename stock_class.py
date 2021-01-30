import yahooquery as yq

aapl = yq.Ticker('aapl')
# income_stat = aapl.income_statement()

class STOCK:

    def __init__(self, ticker_id):
        self.ticker = yq.Ticker(ticker_id)
        self.ticker_id = ticker_id

    def balance_sheet(self):
        """
        A balance sheet is a financial statement that reports a company's assets, liabilities and shareholders' equity
        at a specific point in time, and provides a basis for computing rates of return and evaluating its capital structure.
        It is a financial statement that provides a snapshot of what a company owns and owes, as well as the amount invested by shareholders.
        The balance sheet is a snapshot representing the state of a company's finances at a moment in time. By itself, it cannot give a sense of the trends that are playing out over a longer period. For this reason, the balance sheet should be compared with those of previous periods. It should also be compared with those of other businesses in the same industry since different industries have unique approaches to financing.

        A number of ratios can be derived from the balance sheet, helping investors get a sense of how healthy a company is. These include the debt-to-equity ratio and the acid-test ratio, along with many others. The income statement and statement of cash flows also provide valuable context for assessing a company's finances, as do any notes or addenda in an earnings report that might refer back to the balance sheet.

        ASSETS
        Within the assets segment, accounts are listed from top to bottom in order of their liquidity – that is, the ease with which they can be converted into cash. They are divided into current assets, which can be converted to cash in one year or less; and non-current or long-term assets, which cannot.
        Here is the general order of accounts within current assets:

            * CASH AND CASH EQUIVALENTS: are the most liquid assets and can include Treasury bills and short-term certificates of deposit,
             as well as hard currency.
            * MARKEATABLE SECURITIES: are equity and debt securities for which there is a liquid market.
            * ACCOUNTS RECEIVABLE: refers to money that customers owe the company, perhaps including an allowance for doubtful accounts since a certain proportion of customers can be expected not to pay.
            * INVENTORY: is goods available for sale, valued at the lower of the cost or market price.
            * PREPAID EXPENSES: represent the value that has already been paid for, such as insurance, advertising contracts or rent.
            * LONG-TERM ASSETS: include the following:

                - LONG_TERM INVESTMENTS: are securities that will not or cannot be liquidated in the next year.
                - FIXED ASSETS: include land, machinery, equipment, buildings and other durable, generally capital-intensive assets.
                - INTANGIBLE ASSETS: include non-physical (but still valuable) assets such as intellectual property and goodwill. In general, intangible assets are only listed on the balance sheet if they are acquired, rather than developed in-house. Their value may thus be wildly understated – by not including a globally recognized logo, for example – or just as wildly overstated.

        LIABILITIES
            Liabilities are the money that a company owes to outside parties, from bills it has to pay to suppliers to interest on bonds it has issued to creditors to rent, utilities and salaries. Current liabilities are those that are due within one year and are listed in order of their due date. Long-term liabilities are due at any point after one year.

            Current liabilities accounts might include:

                * current portion of long-term debt
                * bank indebtedness
                * interest payable
                * wages payable
                * customer prepayments
                * dividends payable and others
                * earned and unearned premiums
                * accounts payable

            Long-term liabilities can include:

                * Long-term debt: interest and principal on bonds issued
                * Pension fund liability: the money a company is required to pay into its employees' retirement accounts
                * Deferred tax liability: taxes that have been accrued but will not be paid for another year (Besides timing, this figure reconciles differences between requirements for financial reporting and the way tax is assessed, such as depreciation calculations.)
                * Some liabilities are considered off the balance sheet, meaning that they will not appear on the balance sheet.

        Shareholders' Equity
            Shareholders' equity is the money attributable to a business' owners, meaning its shareholders. It is also
            known as "net assets," since it is equivalent to the total assets of a company minus its liabilities, that is,
             the debt it owes to non-shareholders.

            Retained earnings are the net earnings a company either reinvests in the business or use to pay off debt;
            the rest is distributed to shareholders in the form of dividends.
            Treasury stock is the stock a company has repurchased. It can be sold at a later date to raise cash or reserved
             to repel a hostile takeover.
            Some companies issue preferred stock, which will be listed separately from common stock under shareholders' equity.
             Preferred stock is assigned an arbitrary par value – as is common stock, in some cases – that has no bearing
             on the market value of the shares (often, par value is just $0.01). The "common stock" and "preferred stock"
             accounts are calculated by multiplying the par value by the number of shares issued.

            Additional paid-in capital or capital surplus represents the amount shareholders have invested in excess of
            the "common stock" or "preferred stock" accounts, which are based on par value rather than market price.
            Shareholders' equity is not directly related to a company's market capitalization: the latter is based on the
            current price of a stock, while paid-in capital is the sum of the equity that has been purchased at any price.

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

    def major_holders(self):
        major_holders = self.ticker.major_holders

        return major_holders




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

    def researchanddevelopment(self):
        research_and_development = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['ResearchAndDevelopment'].iloc[-1]

        return research_and_development

    def insiderspercentheld(self):
        insiders = self.stock.major_holders()[self.ticker_id]['insidersPercentHeld']

        return insiders

    def institutionspercentheld(self):
        institutionspercentheld = self.stock.major_holders()[self.ticker_id]['institutionsPercentHeld']

        return institutionspercentheld

if __name__== '__main__':
    stock = STOCK("aapl".lower())
    # beta = stock.beta()
    # ev_ebitda = stock.valuation_measures()['EnterprisesValueEBITDARatio']
    # ebitda = stock.income_statement()['EBITDA']
    # ev = stock.valuation_measures()['EnterpriseValue']
    ratios = RATIO_CALCULATOR('aapl')
    # ratios.roce()
    ratios.reinvesting_rate()


