import requests



stock_code = 'FPH.NZ'

def fetch_quote_for_stock(stock_code):
    URL_ROOT = "http://query.yahooapis.com/v1/public/yql"
    params = {'q': 'select * from yahoo.finance.quotes where symbol = "%s"' % stock_code, 'format': 'json',
              'env': 'http://datatables.org/alltables.env'}
    r = requests.get(URL_ROOT, params)
    return r.json()
