import itertools
import string
import requests


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
        r = requests.get('https://query.yahooapis.com/v1/public/yql?q=use%20%22http%3A%2F%2Fsingingtree.io%2Fyahoo.finance.sectors.xml%22%20as%20yahoo.finance.sectors%3B%20select%20*%20from%20yahoo.finance.sectors%3B&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=')
        sectors = r.json()['query']['results']['sector']
        for sector in sectors:
            industry = sector['industry']
            if isinstance(industry, list):
                for item in industry:
                    yield item
            else:
                yield industry

    def discover_symbols_for_industry_id(self, id):
        r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.industry%20where%20id%3D%22' + str(id) + '%22&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=')
        industry = r.json()['query']['results']['industry']
        for company in industry['company']:
            if isinstance(company, list):
                for item in company:
                    yield item
            else:
                yield company