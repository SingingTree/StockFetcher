import requests

URL_ROOT = "http://query.yahooapis.com/v1/public/yql"

stock_code = 'FPH.NZ'

params = {'q': 'select * from yahoo.finance.quotes where symbol = "%s"' % stock_code, 'format': 'json', 'env': 'http://datatables.org/alltables.env' }

r = requests.get(URL_ROOT, params)
print(r.json())