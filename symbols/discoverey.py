import itertools
import string
import requests
from persistence import StockSymbolAndName
import yql.yqlutil

class SymbolGenerator:
    def __init__(self, min_symbol_length, max_symbol_length, prefix='', suffix=''):
        self.min_symbol_length = min_symbol_length
        self.max_symbol_length = max_symbol_length
        self.prefix = prefix
        self.suffix = suffix

    def possible_symbols(self):
        for length in range(self.min_symbol_length, self.max_symbol_length):
            for perm in itertools.permutations(string.ascii_uppercase, length):
                yield self.prefix + ''.join(perm) + self.suffix

    def check_symbol_exists_via_url(self, symbol):
        r = requests.get('https://finance.yahoo.com/q?s=' + symbol, allow_redirects=False)
        # Okay indicates the code exists, redirect to search will happen if that specific code isn't found
        return r.status_code == requests.codes.ok


class IndustryDiscoverer:
    def discover_industries(self):
        params = {'q': 'use "http://singingtree.io/yahoo.finance.sectors.xml" as yahoo.finance.sectors; '
                       'select * from yahoo.finance.sectors',
                  'format': 'json',
                  'diagnostics': 'true',
                  'env': 'store://datatables.org/alltableswithkeys',
                  }
        r = requests.get(yql.get_url_root(), params)
        sectors = r.json()['query']['results']['sector']
        for sector in sectors:
            industry = sector['industry']
            if isinstance(industry, list):
                for item in industry:
                    yield item
            else:
                yield industry

    def discover_symbols_for_industry_id(self, id):
        params = {'q': 'select * from yahoo.finance.industry where id="%s"' %id,
                  'format': 'json',
                  'diagnostics': 'true',
                  'env': 'store://datatables.org/alltableswithkeys',
                  }
        r = requests.get(yql.get_url_root(), params)
        industry = r.json()['query']['results']['industry']
        for company in industry['company']:
            if isinstance(company, list):
                for item in company:
                    yield StockSymbolAndName(symbol=item['symbol'], name=item['name'].replace('\n', ' '))
            else:
                yield StockSymbolAndName(symbol=company['symbol'], name=company['name'].replace('\n', ' '))