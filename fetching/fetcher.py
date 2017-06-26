import requests
import yql

def fetch_quote_for_stock(stock_code):
    params = {'q': 'select * from yahoo.finance.quotes where symbol = "%s"' % stock_code,
              'format': 'json',
              'env': 'http://datatables.org/alltables.env'}
    r = requests.get(yql.get_url_root(), params)
    return r.json()
