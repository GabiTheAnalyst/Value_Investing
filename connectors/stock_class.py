import yahooquery as yq

aapl = yq.Ticker('aapl')
# income_stat = aapl.income_statement()

class STOCK:

    def __init__(self, ticker_id):
        self.ticker = yq.Ticker(ticker_id)
        self.ticker_id = ticker_id

    def income_statement(self):
        """
        Also known as the profit and loss statement or the statement of revenue and expense, the income statement
        primarily focuses on the company’s revenues and expenses during a particular period.
        Net Income = (Total Revenue + Gains) – (Total Expenses + Losses)
            Total revenue is the sum of both operating and non-operating revenues while total expenses include those
            incurred by primary and secondary activities.
            Revenues are not receipts. Revenue is earned and reported on the income statement. Receipts (cash received or paid out)
            are not.
            An income statement provides valuable insights into a company’s operations, the efficiency of its management,
            under-performing sectors and its performance relative to industry peers.

        The income statement focuses on four key items: revenue, expenses, gains, and losses. It does not differentiate between cash and non-cash receipts (sales in cash versus sales on credit) or the cash versus non-cash payments/disbursements (purchases in cash versus purchases on credit). It starts with the details of sales, and then works down to compute the net income and eventually the earnings per share (EPS). Essentially, it gives an account of how the net revenue realized by the company gets transformed into net earnings (profit or loss).

        REVENUES AND GAINS
        The following are covered in the income statement, though its format may vary depending upon the local regulatory
         requirements, the diversified scope of the business and the associated operating activities:

            * Operating Revenue
            Revenue realized through primary activities is often referred to as operating revenue. For a company manufacturing
             a product, or for a wholesaler, distributor or retailer involved in the business of selling that product,
             the revenue from primary activities refers to revenue achieved from the sale of the product. Similarly, for
             a company (or its franchisees) in the business of offering services, revenue from primary activities refers
             to the revenue or fees earned in exchange of offering those services.

            * Non-Operating Revenue
            Revenues realized through secondary, non-core business activities are often referred to as non-operating
            recurring revenues. These revenues are sourced from the earnings which are outside of the purchase and sale
            of goods and services and may include income from interest earned on business capital lying in the bank,
            rental income from business property, income from strategic partnerships like royalty payment receipts or
            income from an advertisement display placed on business property.

            * Gains
            Also called other income, gains indicate the net money made from other activities, like the sale of long-term
            assets. These include the net income realized from one-time non-business activities, like a company selling
            its old transportation van, unused land, or a subsidiary company.

            Revenue should not be confused with receipts. Revenue is usually accounted for in the period when sales are made or services are delivered. Receipts are the cash received and are accounted for when the money is actually received. For instance, a customer may take goods/services from a company on 28 September, which will lead to the revenue being accounted for in the month of September. Owing to his good reputation, the customer may be given a 30-day payment window. It will give him time till 28 October to make the payment, which is when the receipts are accounted for.

        EXPENSES AND LOSES
        The cost for a business to continue operation and turn a profit is known as an expense. Some of these expenses
        may be written off on a tax return if they meet the IRS guidelines.

            * Primary Activity Expenses
            All expenses incurred for earning the normal operating revenue linked to the primary activity of the business.
            They include the cost of goods sold (COGS), selling, general and administrative expenses (SG&A), depreciation
            or amortization, and research and development (R&D) expenses. Typical items that make up the list are employee
             wages, sales commissions, and expenses for utilities like electricity and transportation.

            * Secondary Activity Expenses
            All expenses linked to non-core business activities, like interest paid on loan money.

           * Losses as Expenses
            All expenses that go towards a loss-making sale of long-term assets, one-time or any other unusual costs, or
            expenses towards lawsuits.

            While primary revenue and expenses offer insights into how well the company’s core business is performing, the
            secondary revenue and expenses account for the company’s involvement and its expertise in managing the ad-hoc,
            non-core activities. Compared to the income from the sale of manufactured goods, a substantially high-interest
            income from money lying in the bank indicates that the business may not be utilizing the available cash to
            its full potential by expanding the production capacity, or it is facing challenges in increasing its market
            share amid competition. Recurring rental income gained by hosting billboards at the company factory situated
            along a highway indicates that the management is capitalizing upon the available resources and assets for
            additional profitability.

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
        A cash flow statement is a financial statement that provides aggregate data regarding all cash inflows a company
        receives from its ongoing operations and external investment sources. It also includes all cash outflows that
        pay for business activities and investments during a given period.

        A company's financial statements offer investors and analysts a portrait of all the transactions that go through the
        business, where every transaction contributes to its success. The cash flow statement is believed to be the most
        intuitive of all the financial statements because it follows the cash made by the business in three main ways—through
        operations, investment, and financing. The sum of these three segments is called net cash flow.

        These three different sections of the cash flow statement can help investors determine the value of a company's stock
        or the company as a whole.

        A cash flow statement provides data regarding all cash inflows a company receives from its ongoing operations and
        external investment sources.
        The cash flow statement includes cash made by the business through operations, investment, and financing—the sum of
        which is called net cash flow.
        The first section of the cash flow statement is cash flow from operations, which includes transactions from all
        operational business activities.
        Cash flow from investment is the second section of the cash flow statement, and is the result of investment gains
        and losses.
        Cash flow from financing is the final section, which provides an overview of cash used from debt and equity.

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

        return self.ticker.summary_detail

    def beta(self):
        """
        Beta is a measure of a stock's volatility in relation to the overall market. By definition, the market, such as
        the S&P 500 Index, has a beta of 1.0, and individual stocks are ranked according to how much they deviate from
        the market.

        A stock that swings more than the market over time has a beta above 1.0. If a stock moves less than the market,
        the stock's beta is less than 1.0. High-beta stocks are supposed to be riskier but provide higher return
        potential; low-beta stocks pose less risk but also lower returns.

        :return: float
        """
        module = 'defaultKeyStatistics'
        values = self.ticker.get_modules(module)
        beta = values[self.ticker_id]['beta']

        return beta

    def major_holders(self):
        """
        :return: Data showing breakdown of owners of given symbol(s), insiders, institutions, etc.
        """

        return self.ticker.major_holders

    def history(self, period=None):
        """
        :return: Historical pricing data
        """
        return self.ticker.history(period)

    def quotes(self):
        """
        {'AAPL': {'language': 'en-US',
                  'region': 'US',
                  'quoteType': 'EQUITY',
                  'quoteSourceName': 'Nasdaq Real Time Price',
                  'triggerable': True,
                  'currency': 'USD',
                  'firstTradeDateMilliseconds': 345479400000,
                  'priceHint': 2,
                  'postMarketPrice': 131.78,
                  'postMarketChange': -0.180008,
                  'regularMarketChange': -5.1299896,
                  'regularMarketChangePercent': -3.7420597,
                  'regularMarketTime': 1611954002,
                  'earningsTimestampEnd': 1620043200,
                  'trailingAnnualDividendRate': 0.807,
                  'trailingPE': 35.79062,
                  'trailingAnnualDividendYield': 0.0058866437,
                  'epsTrailingTwelveMonths': 3.687,
                  'epsForward': 4.6,
                  'epsCurrentYear': 4.35,
                  'priceEpsCurrentYear': 30.335634,
                  'sharesOutstanding': 16788100096,
                  'bookValue': 3.936,
                  'fiftyDayAverage': 131.92313,
                  'fiftyDayAverageChange': 0.036880493,
                  'fiftyDayAverageChangePercent': 0.00027956048,
                  'twoHundredDayAverage': 118.55683,
                  'twoHundredDayAverageChange': 13.403175,
                  'twoHundredDayAverageChangePercent': 0.11305275,
                  'marketCap': 2215357710336,
                  'forwardPE': 28.686958,
                  'priceToBook': 33.526424,
                  'sourceInterval': 15,
                  'exchangeDataDelayedBy': 0,
                  'exchange': 'NMS',
                  'shortName': 'Apple Inc.',
                  'longName': 'Apple Inc.',
                  'messageBoardId': 'finmb_24937',
                  'exchangeTimezoneName': 'America/New_York',
                  'exchangeTimezoneShortName': 'EST',
                  'gmtOffSetMilliseconds': -18000000,
                  'market': 'us_market',
                  'esgPopulated': False,
                  'postMarketChangePercent': -0.136411,
                  'postMarketTime': 1611968399,
                  'tradeable': False,
                  'marketState': 'CLOSED',
                  'regularMarketPrice': 131.96,
                  'regularMarketDayHigh': 136.74,
                  'regularMarketDayRange': '130.21 - 136.74',
                  'regularMarketDayLow': 130.21,
                  'regularMarketVolume': 177523812,
                  'regularMarketPreviousClose': 137.09,
                  'bid': 131.75,
                  'ask': 131.78,
                  'bidSize': 8,
                  'askSize': 10,
                  'fullExchangeName': 'NasdaqGS',
                  'financialCurrency': 'USD',
                  'regularMarketOpen': 135.83,
                  'averageDailyVolume3Month': 109613798,
                  'averageDailyVolume10Day': 135948100,
                  'fiftyTwoWeekLowChange': 78.80751,
                  'fiftyTwoWeekLowChangePercent': 1.482668,
                  'fiftyTwoWeekRange': '53.1525 - 145.09',
                  'fiftyTwoWeekHighChange': -13.12999,
                  'fiftyTwoWeekHighChangePercent': -0.09049548,
                  'fiftyTwoWeekLow': 53.1525,
                  'fiftyTwoWeekHigh': 145.09,
                  'dividendDate': 1605139200,
                  'earningsTimestamp': 1611765000,
                  'earningsTimestampStart': 1619607540,
                  'displayName': 'Apple'}}

        :return:
        """
        return self.ticker.quotes

    def asset_profile(self):
        """
        {'aapl': {'address1': 'One Apple Park Way',
              'city': 'Cupertino',
              'state': 'CA',
              'zip': '95014',
              'country': 'United States',
              'phone': '408-996-1010',
              'website': 'http://www.apple.com',
              'industry': 'Consumer Electronics',
              'sector': 'Technology',
              'longBusinessSummary': 'Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. It also sells various related services. The company offers iPhone, a line of smartphones; Mac, a line of personal computers; iPad, a line of multi-purpose tablets; and wearables, home, and accessories comprising AirPods, Apple TV, Apple Watch, Beats products, HomePod, iPod touch, and other Apple-branded and third-party accessories. It also provides AppleCare support services; cloud services store services; and operates various platforms, including the App Store, that allow customers to discover and download applications and digital content, such as books, music, video, games, and podcasts. In addition, the company offers various services, such as Apple Arcade, a game subscription service; Apple Music, which offers users a curated listening experience with on-demand radio stations; Apple News+, a subscription news and magazine service; Apple TV+, which offers exclusive original content; Apple Card, a co-branded credit card; and Apple Pay, a cashless payment service, as well as licenses its intellectual property. The company serves consumers, and small and mid-sized businesses; and the education, enterprise, and government markets. It sells and delivers third-party applications for its products through the App Store. The company also sells its products through its retail and online stores, and direct sales force; and third-party cellular network carriers, wholesalers, retailers, and resellers. Apple Inc. was founded in 1977 and is headquartered in Cupertino, California.',
              'fullTimeEmployees': 147000,
              'companyOfficers': [{'maxAge': 1,
                'name': 'Mr. Timothy D. Cook',
                'age': 59,
                'title': 'CEO & Director',
                'yearBorn': 1961,
                'fiscalYear': 2020,
                'totalPay': 14769259,
                'exercisedValue': 0,
                'unexercisedValue': 0},
               {'maxAge': 1,
                'name': 'Mr. Luca  Maestri',
                'age': 56,
                'title': 'CFO & Sr. VP',
                'yearBorn': 1964,
                'fiscalYear': 2020,
                'totalPay': 4595583,
                'exercisedValue': 0,
                'unexercisedValue': 0},
               {'maxAge': 1,
                'name': 'Mr. Jeffrey E. Williams',
                'age': 56,
                'title': 'Chief Operating Officer',
                'yearBorn': 1964,
                'fiscalYear': 2020,
                'totalPay': 4594137,
                'exercisedValue': 0,
                'unexercisedValue': 0},
               {'maxAge': 1,
                'name': 'Ms. Katherine L. Adams',
                'age': 56,
                'title': 'Sr. VP, Gen. Counsel & Sec.',
                'yearBorn': 1964,
                'fiscalYear': 2020,
                'totalPay': 4591310,
                'exercisedValue': 0,
                'unexercisedValue': 0},
               {'maxAge': 1,
                'name': "Ms. Deirdre  O'Brien",
                'age': 53,
                'title': 'Sr. VP of People & Retail',
                'yearBorn': 1967,
                'fiscalYear': 2020,
                'totalPay': 4614684,
                'exercisedValue': 0,
                'unexercisedValue': 0},
               {'maxAge': 1,
                'name': 'Mr. Chris  Kondo',
                'title': 'Sr. Director of Corp. Accounting',
                'exercisedValue': 0,
                'unexercisedValue': 0},
               {'maxAge': 1,
                'name': 'Mr. James  Wilson',
                'title': 'Chief Technology Officer',
                'exercisedValue': 0,
                'unexercisedValue': 0},
               {'maxAge': 1,
                'name': 'Ms. Mary  Demby',
                'title': 'Chief Information Officer',
                'exercisedValue': 0,
                'unexercisedValue': 0},
               {'maxAge': 1,
                'name': 'Ms. Nancy  Paxton',
                'title': 'Sr. Director of Investor Relations & Treasury',
                'exercisedValue': 0,
                'unexercisedValue': 0},
               {'maxAge': 1,
                'name': 'Mr. Greg  Joswiak',
                'title': 'Sr. VP of Worldwide Marketing',
                'exercisedValue': 0,
                'unexercisedValue': 0}],
              'auditRisk': 1,
              'boardRisk': 1,
              'compensationRisk': 3,
              'shareHolderRightsRisk': 1,
              'overallRisk': 1,
              'governanceEpochDate': '2021-01-22 01:00:00',
              'compensationAsOfEpochDate': '2020-12-31 01:00:00',
              'maxAge': 86400}}

        :return:
        """
        return self.ticker.asset_profile

class RATIO_CALCULATOR(STOCK):

    def __init__(self, ticker_id):
        self.stock = STOCK(ticker_id.lower())
        self.ticker_id = ticker_id.lower()

    def price(self):
        """
        :return: Last day price
        """

        return self.stock.history()['close'].iloc[-1]

    def momentum(self):
        """
        Momentum investing is a system of buying stocks or other securities that have had high returns over the past
        three to twelve months, and selling those that have had poor returns over the same period.

        :return: percentage
        """
        price_history_last_year = self.stock.history(period='1y')['close']
        momentum = (price_history_last_year[-1] / price_history_last_year[0]) - 1

        return momentum

    def dividend_yield(self):
        """
        The dividend yield is a financial ratio that tells you the percentage of a company’s share price that it pays
        out in dividends each year. For example, if a company has a $20 share price and pays a dividend of $1.00 per
        year, its dividend yield would be 5%. If a company’s dividend yield has been steadily increasing, this could be
        because they are increasing their dividend, because their share price is declining, or both. Depending on the
        circumstances, this may be seen as either a positive or a negative sign by investors.

        Is a high dividend yield good?
        Yield-oriented investors will generally look for companies that offer high dividend yields, but it is important
        to dig deeper in order to understand the circumstances leading to the high yield. One approach taken by
        investors is to focus on companies that have a long track-record of maintaining or raising their dividends,
        while also verifying that those companies have the underlying financial strength to continue paying dividends
        well into the future. To do so, investors can refer to other metrics such as the current ratio and the dividend
        payout ratio.

        Why is dividend yield important?
        Some investors, such as retirees, are heavily reliant on dividends for their income. For these investors, the
        dividend yield of their portfolio could have a meaningful effect on their personal finances, making it very
        important for these investors to select dividend-paying companies with long track records and clear financial
        strength. For other investors, dividend yield may be less significant, such as for younger investors who are
        more interested in growth companies that can retain their earnings and use them to finance their growth.

        :return: float as percentage
        """
        try:
            dividend_yield = self.stock.summary_detail()[self.ticker_id]['dividendYield']
        except:
            dividend_yield = None

        return dividend_yield

    def ev_fcf(self):
        """
        Enterprise Value to Free Cash Flow compares the total valuation of the company with its ability to generate
        cashflow. It is the inverse of the Free Cash Flow Yield. The lower the ratio of enterprise value to the free
        cash flow figures, the faster a company can pay back the cost of its acquisition or generate cash to reinvest
        in its business.

        Enterprise value is arguably a more accurate measure of the value of a firm, as it includes the debt, value of
        preferred shares and minority interest, but minus cash and cash equivalents.

        :return:
        """
        ev = self.stock.all_financial_data()['EnterpriseValue'][-1]
        fcf = self.stock.all_financial_data()['FreeCashFlow'][-1]

        return ev / fcf

    def pe_ratio(self):
        """
        The price-to-earnings ratio (P/E ratio) is the ratio for valuing a company that measures its current share price
        relative to its per-share earnings (EPS). The price-to-earnings ratio is also sometimes known as the price
        multiple or the earnings multiple.

        P/E ratios are used by investors and analysts to determine the relative value of a company's shares in an
        apples-to-apples comparison. It can also be used to compare a company against its own historical record or to
        compare aggregate markets against one another or over time.

        The price-earnings ratio (P/E ratio) relates a company's share price to its earnings per share.
        A high P/E ratio could mean that a company's stock is over-valued, or else that investors are expecting high
        growth rates in the future.
        Companies that have no earnings or that are losing money do not have a P/E ratio since there is nothing to put
        in the denominator.
        Two kinds of P/E ratios - forward and trailing P/E - are used in practice.

        Analysts and investors review a company's P/E ratio when they determine if the share price accurately represents
        the projected earnings per share. The formula and calculation used for this process follow.
        ​	P/E ratio = Market value per share / Earnings per share

        :return: float
        """

        return self.stock.valuation_measures()['PeRatio'].dropna().iloc[-1]

    def peg_ratio(self):
        """
        The price/earnings to growth ratio (PEG ratio) is a stock's price-to-earnings (P/E) ratio divided by the growth
        rate of its earnings for a specified time period. The PEG ratio is used to determine a stock's value while also
        factoring in the company's expected earnings growth, and it is thought to provide a more complete picture than
        the more standard P/E ratio.

        The PEG ratio enhances the P/E ratio by adding in expected earnings growth into the calculation.
        The PEG ratio is considered to be an indicator of a stock's true value, and similar to the P/E ratio, a lower
        PEG may indicate that a stock is undervalued.
        The PEG for a given company may differ significantly from one reported source to another, depending on which
        growth estimate is used in the calculation, such as one-year or three-year projected growth.

            PEG ratio = (Price / EPS) / EPS Growth
                being EPS = Earnings Per Share

        :return: float
        """

        return self.stock.valuation_measures()['PegRatio'].dropna().iloc[-1]

    def pb_ratio(self):
        """
        Companies use the price-to-book ratio (P/B ratio) to compare a firm's market capitalization to its book value.
        It's calculated by dividing the company's stock price per share by its book value per share (BVPS). An asset's
        book value is equal to its carrying value on the balance sheet, and companies calculate it netting the asset
        against its accumulated depreciation.

        Book value is also the tangible net asset value of a company calculated as total assets minus intangible assets
        (.e.g. patents, goodwill) and liabilities. For the initial outlay of an investment, book value may be net or gross
        of expenses, such as trading costs, sales taxes, and service charges. Some people may know this ratio by its less
        common name, the price-equity ratio.

        P/B ratios under 1 are typically considered solid investments.

        In this equation, book value per share is calculated as follows: (total assets - total liabilities) / number of
        shares outstanding). Market value per share is obtained by simply looking at the share price quote in the market.

        P/B Ratio = Market Price per Share / LBook Value per Share﻿

        A lower P/B ratio could mean the stock is undervalued. However, it could also mean something is fundamentally
        wrong with the company. As with most ratios, this varies by industry. The P/B ratio also indicates whether you're
        paying too much for what would remain if the company went bankrupt immediately.

        :return: float
        """

        return self.stock.valuation_measures()['PbRatio'].dropna().iloc[-1]

    def ps_ratio(self):
        """
        The price-to-sales (P/S) ratio is a valuation ratio that compares a company’s stock price to its revenues.
        It is an indicator of the value that financial markets have placed on each dollar of a company’s sales or revenues.

        The P/S ratio can be calculated either by dividing the company’s market capitalization by its total sales over a
        designated period (usually twelve months) or on a per-share basis by dividing the stock price by sales per share.
        The P/S ratio is also known as a sales multiple or revenue multiple.

        The price-to-sales (P/S) ratio is a key analysis and valuation tool that shows how much investors are willing
        to pay per dollar of sales for a stock.
        The P/S ratio is typically calculated by dividing the stock price by the underlying company's sales per share.
        A low ratio could imply the stock is undervalued while a ratio that is higher-than-average could indicate that
        the stock is overvalued.
        One of the downsides of the P/S ratio is that it doesn’t take into account whether the company makes any
        earnings or whether it will ever make earnings.

            P/S ratio = Market Value Per Sharea / Sales Per Share

        :return: float
        """

        return self.stock.valuation_measures()['PsRatio'].dropna().iloc[-1]

    def roce(self):
        """
        Return on capital employed (ROCE) is a financial ratio that can be used in assessing a company's profitability
        and capital efficiency. In other words, the ratio can help to understand how well a company is generating
        profits from its capital.

        The ROCE ratio is one of several profitability ratios financial managers, stakeholders, and potential investors may use
        when analyzing a company for investment.

        The formula for ROCE is as follows:
            ROCE = EBIT / Capital Employed
                where:
                    EBIT = Earnings Before Interest and Tax
                    Capital Employed = Total Assets - Current Liabilities

            ROCE is a metric for analyzing profitability, and potentially comparing profitability levels across companies in terms
            of capital. There are two components required to calculate return on capital employed: earnings before interest and tax
            and capital employed.

            EBIT, also known as operating income, shows how much a company earns from its operations alone without regard to
            interest or taxes. EBIT is calculated by subtracting the cost of goods sold and operating expenses from revenues.

            Capital employed is very similar to invested capital, which is used in the ROIC calculation. Capital employed is found
            by subtracting total assets from current liabilities, which ultimately gives you shareholders’ equity plus long-term
            debts. Instead of using capital employed at an arbitrary point in time, some analysts and investors may choose to
            calculate ROCE based on the average capital employed, which takes the average of opening and closing capital employed
            for the time period under analysis.

            ROCE can be especially useful when comparing the performance of companies in capital-intensive sectors,
            such as utilities and telecoms. This is because unlike other fundamentals such as return on equity (ROE),
            which only analyzes profitability related to a company’s shareholders’ equity, ROCE considers debt and
            equity. This can help neutralize financial performance analysis for companies with significant debt.

            Ultimately, the calculation of ROCE tells you the amount of profit a company is generating per $1 of capital
            employed. Obviously, the more profit per $1 a company can generate the better. Thus, a higher ROCE indicates
            stronger profitability across company comparisons.

        :return: float
        """

        ebit = self.stock.income_statement()[self.stock.income_statement().periodType == '12M'].iloc[-1]['EBIT']  # Also: self.stock.all_financial_data()['EBIT'][-1]
        total_assets = self.stock.balance_sheet()[self.stock.balance_sheet().periodType == '12M'].iloc[-1]['TotalAssets']
        current_liabilities = self.stock.balance_sheet()[self.stock.balance_sheet().periodType == '12M'].iloc[-1]['CurrentLiabilities']
        roce = ebit / (total_assets - current_liabilities)

        return roce

    def roic(self):
        """
        Return on invested capital (ROIC) is a calculation used to assess a company's efficiency at allocating the
        capital under its control to profitable investments. The return on invested capital ratio gives a sense of how
        well a company is using its money to generate returns. Comparing a company's return on invested capital with
        its weighted average cost of capital (WACC) reveals whether invested capital is being used effectively. This
        measure is also known simply as "return on capital."

        ROIC is the amount of return a company makes above the average cost it pays for its debt and equity capital.
        The return on invested capital can be used as a benchmark to calculate the value of other companies
        A company is creating value if its ROIC exceeds 2% and destroying value if less than 2%.

        The formula for ROIC is (net income - dividend) / (debt + equity). The ROIC formula is calculated by assessing
        the value in the denominator, total capital, which is the sum of a company's debt and equity. There are a number
        of ways to calculate this value. One is to subtract cash and non-interest bearing current liabilities
        (NIBCL)—including tax liabilities and accounts payable, as long as these are not subject to interest or
        fees—from total assets.

        Another way to write the formula includes:

        ROIC = NOPAT / Invested Capital        ​
            where:
            NOPAT=Net operating profit after tax
    ​
        :return: float
        """
        operating_income = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['OperatingIncome'].iloc[-1]
        tax_rate = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['TaxRateForCalcs'].iloc[-1]

        average_invested_capital = self.stock.balance_sheet()[self.stock.balance_sheet().periodType == '12M']['InvestedCapital'][-2:,].sum() / 2

        roic = operating_income * (1 + tax_rate) / average_invested_capital

        return roic

    def roa(self):
        """
        Return on assets (ROA) is an indicator of how profitable a company is relative to its total assets. ROA gives
        a manager, investor, or analyst an idea as to how efficient a company's management is at using its assets to
        generate earnings. Return on assets is displayed as a percentage.

        Return on Assets (ROA) is an indicator of how well a company utilizes its assets, by determining how profitable
        a company is relative to its total assets.
        ROA is best used when comparing similar companies or comparing a company to its previous performance.
        ROA takes into account a company’s debt, unlike other metrics, such as Return on Equity (ROE).

        Businesses (at least the ones that survive) are ultimately about efficiency: squeezing the most out of limited
        resources. Comparing profits to revenue is a useful operational metric, but comparing them to the resources a
        company used to earn them cuts to the very feasibility of that company's’ existence. Return on assets (ROA) is
        the simplest of such corporate bang-for-the-buck measures.

            ROA = Net Income / Total Assets

        Higher ROA indicates more asset efficiency.

        :return: float
        """
        net_income = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['NetIncome'].iloc[-1]
        average_total_assets = self.stock.balance_sheet()[self.stock.balance_sheet().periodType == '12M']['TotalAssets'][-2:,].sum() / 2

        roa = net_income / average_total_assets

        return roa

    def roe(self):
        """
        Return on equity (ROE) is a measure of financial performance calculated by dividing net income by shareholders'
        equity. Because shareholders' equity is equal to a company’s assets minus its debt, ROE is considered the return
        on net assets. ROE is considered a measure of the profitability of a corporation in relation to stockholders’ equity.

        Return on equity (ROE) measures how the profitability of a corporation in relation to stockholders’ equity.
        Whether an ROE is considered satisfactory will depend on what is normal for the industry or company peers.
        As a shortcut, investors can consider an ROE near the long-term average of the S&P 500 (14%) as an acceptable
        ratio and anything less than 10% as poor.

        ROE is expressed as a percentage and can be calculated for any company if net income and equity are both
        positive numbers. Net income is calculated before dividends paid to common shareholders and after dividends to
        preferred shareholders and interest to lenders.
            ROE = Net Income / Average Shareholder's Equity

        Net income is the amount of income, net of expense, and taxes that a company generates for a given period.
        Average shareholders' equity is calculated by adding equity at the beginning of the period. The beginning and
        end of the period should coincide with the period during which the net income is earned.

        Net income over the last full fiscal year, or trailing 12 months, is found on the income statement—a sum of financial
        activity over that period. Shareholders' equity comes from the balance sheet—a running balance of a company’s entire
        history of changes in assets and liabilities.

        It is considered best practice to calculate ROE based on average equity over a period because of the mismatch between
        the income statement and the balance sheet.

        :return: float
        """
        net_income = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['NetIncome'].iloc[-1]
        average_stock_holder_equity = self.stock.balance_sheet()[self.stock.balance_sheet().periodType == '12M']['StockholdersEquity'][-2:,].sum() / 2

        roe = net_income / average_stock_holder_equity

        return roe

    def reinvesting_rate(self):
        """
        ESTO AÚN NO ESTÁ FINO!!!!
        The reinvesting rate is calculated as the division between Investing cash flow and Operating cash flow. However,
        it may happen that Investing cash flow is positive due to sales of investments or net other investment changes.
        Hence, I have deducted the positive values from Operating cash flow so only proper investing values (negative)
        are taking into account.

        :return: Reinvesting rate
        """
        operating_cash_flow = self.stock.cash_flow()[self.stock.cash_flow().periodType == '12M']['OperatingCashFlow']

        investing_cash_flow = self.stock.cash_flow()[self.stock.cash_flow().periodType == '12M']['InvestingCashFlow']
        try:
            sale_of_investment = self.stock.cash_flow()[self.stock.cash_flow().periodType == '12M']['SaleOfInvestment']
        except:
            sale_of_investment = 0
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
        """
        Debt/EBITDA—earnings before interest, taxes, depreciation, and amortization—is a ratio measuring the amount of
        income generated and available to pay down debt before covering interest, taxes, depreciation, and amortization
        expenses. Debt/EBITDA measures a company's ability to pay off its incurred debt. A high ratio result could
        indicate a company has a too-heavy debt load.

        Banks often include a certain debt/EBITDA target in the covenants for business loans, and a company must maintain this
        agreed-upon level or risk having the entire loan become due immediately. This metric is commonly used by credit rating
        agencies to assess a company's probability of defaulting on issued debt, and firms with a high debt/EBITDA ratio may not
        be able to service their debt in an appropriate manner, leading to a lowered credit rating.

        The debt/EBITDA ratio compares a company's total obligations, including debt and other liabilities, to the
        actual cash the company brings in and reveals how capable the firm is of paying its debt and other liabilities.

        When lenders and analysts look at a company's debt/EBITDA ratio, they want to know how well the firm can cover
        its debts. EBITDA represents a company's earnings or income, and it's an acronym for earnings before interest,
        taxes, depreciation, and amortization. It's calculated by adding back interest, taxes, depreciation, and
        amortization expenses to net income.

        Analysts often look at EBITDA as a more accurate measure of earnings from the firm's operations, rather than
        net income. Some analysts see interest, taxes, depreciation, and amortization as an impediment to real cash
        flows. In other words, they see EBITDA as a cleaner representation of the real cash flows available to pay off debt.

        :return: float
        """
        total_debt = self.stock.balance_sheet()[self.stock.balance_sheet().periodType== '12M']['TotalDebt'].iloc[-1]
        ebitda = self.stock.income_statement()['EBITDA'].iloc[-1]

        debt_ebitda_ratio = total_debt / ebitda

        return debt_ebitda_ratio

    def gross_margin(self):
        """
        Gross margin is a company's net sales revenue minus its cost of goods sold (COGS). In other words, it is the
        sales revenue a company retains after incurring the direct costs associated with producing the goods it sells,
        and the services it provides. The higher the gross margin, the more capital a company retains on each dollar of
        sales, which it can then use to pay other costs or satisfy debt obligations. The net sales figure is simply
        gross revenue, less the returns, allowances, and discounts.

        Gross Margin = Net Sales - COGS
            where:
                COGS = Cost of Goods Sold
                Net Sales=Equivalent to revenue, or the total amount of money generated from sales for the period. It
                can also be called net sales because it can include discounts and deductions from returned merchandise.
                Revenue is typically called the top line because it sits on top of the income statement. Costs are
                subtracted from revenue to calculate net income or the bottom line.
                COGS=Cost of goods sold. The direct costs associated with producing goods. Includes both direct labor
                costs, and any costs of materials used in producing or manufacturing a company’s products.
                            ​

        :return: float
        """
        total_revenue = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['TotalRevenue'].iloc[-1]
        gross_profit = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['GrossProfit'].iloc[-1]

        gross_margin = gross_profit / total_revenue

        return gross_margin

    def operating_margin(self):
        """
        Operating margin measures how much profit a company makes on a dollar of sales after paying for variable costs
        of production, such as wages and raw materials, but before paying interest or tax. It is calculated by dividing
        a company’s operating income by its net sales.

        A company’s operating margin, also known as return on sales, is a good indicator of how well it is being managed
        and how risky it is. It shows the proportion of revenues that are available to cover non-operating costs, like
        paying interest, which is why investors and lenders pay close attention to it.

        Highly variable operating margins are a prime indicator of business risk. By the same token, looking at a
        company’s past operating margins is a good way to gauge whether a company's performance has been getting better.
        Operating margin can improve through better management controls, more efficient use of resources, improved
        pricing, and more effective marketing.

        In its essence, operating margin is how much profit a company makes from its core business in relation to its
        total revenues. This allows investors to see if a company is generating income primarily from its core
        operations or from other means, such as investing.

        General Motors (GM) was a prime example of this. In the 1980s and 1990s, GM was making the bulk of its profits
        from financing cars as opposed to making and selling actual cars, its core operations. Therefore, its operating
        margins were very low. Since then, its automotive business generates more income than its financing business.

            Operating Margin = Operating Earnings / Revenue

            When calculating operating margin, operating earnings is the same as earnings before interest and taxes
            (EBIT). EBIT, or operating earnings, is revenue minus cost of goods sold and the regular selling, general,
            and administrative costs of running a business, excluding interest and taxes.

        The operating income might be either positive or negative (profit or loss)

        :return: float
        """
        total_revenue = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['TotalRevenue'].iloc[-1]
        operating_income = self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['OperatingIncome'].iloc[-1]

        operating_margin = operating_income / total_revenue

        return operating_margin

    def researchanddevelopment(self):
        """
        :return: Amount that the business destinates to research and development.
        """

        return self.stock.income_statement()[self.stock.income_statement().periodType == '12M']['ResearchAndDevelopment'].iloc[-1]


    def insiderspercentheld(self):
        """
        :return: Percentage held by the executive board.
        """

        return self.stock.major_holders()[self.ticker_id]['insidersPercentHeld']

    def institutionspercentheld(self):
        """
        :return: Percentage held by Institutions.
        """

        return self.stock.major_holders()[self.ticker_id]['institutionsPercentHeld']

class STOCK_INFO(STOCK):

    def __init__(self, ticker_id):
        self.stock = STOCK(ticker_id.lower())
        self.ticker_id = ticker_id.lower()

    def name(self):
        return self.stock.quotes()[self.ticker_id.upper()]['longName']

    def currency(self):
        return self.stock.quotes()[self.ticker_id.upper()]['currency']

    def market(self):
        return self.stock.quotes()[self.ticker_id.upper()]['market']

    def sector(self):
        return self.stock.asset_profile()[self.ticker_id]['sector']

    def industry(self):
        return self.stock.asset_profile()[self.ticker_id]['industry']

    def region(self):
        return self.stock.quotes()[self.ticker_id.upper()]['region']

    def longbusinesssummary(self):
        return self.stock.asset_profile()[self.ticker_id]['longBusinessSummary']

    def fulltimeemployees(self):
        return self.stock.asset_profile()[self.ticker_id]['fullTimeEmployees']

    def website(self):
        return self.stock.asset_profile()[self.ticker_id]['website']



if __name__== '__main__':
    stock = STOCK("aapl".lower())
    # beta = stock.beta()
    ratios = RATIO_CALCULATOR('aapl')
    # ratios.roce()
    # ratios.reinvesting_rate()
    info = STOCK_INFO('aapl'.lower())


