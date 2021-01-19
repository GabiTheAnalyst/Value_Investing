import yahooquery as yq

aapl = yq.Ticker('aapl')
aapl = Ticker('aapl')
income_stat = aapl.income_statement()

class STOCK:

    def __init__(self, ticker_id):
        self.ticker = yq.Ticker(ticker_id)

    def balance_sheet(self):
        return self.ticker.balance_sheet()

    def cash_flow(self):
        return self.ticker.cash_flow()

    def income_statement(self):
        return self.ticker.income_statement()


    def get_roce(self):
        ebit = stock.income_statement()[stock.income_statement().periodType == '12M'].iloc[-1]['EBIT']
        total_assets = stock.balance_sheet()[stock.balance_sheet().periodType == '12M'].iloc[-1]['TotalAssets']
        current_liabilities = stock.balance_sheet()[stock.balance_sheet().periodType == '12M'].iloc[-1]['CurrentLiabilities']

        roce = ebit / (total_assets - current_liabilities)
        return roce

if __name__== '__main__':
    stock = STOCK("aapl".lower())
    roce = stock.get_roce()
