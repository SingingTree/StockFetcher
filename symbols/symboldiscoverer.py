import itertools
import string

class SymbolDiscoverer:
    def __init__(self, min_symbol_length, max_symbol_length, prefix='', suffix=''):
        self.min_symbol_length = min_symbol_length
        self.max_symbol_length = max_symbol_length
        self.prefix = prefix
        self.suffix = suffix

    def next_symbol(self):
        for length in range(self.min_symbol_length, self.max_symbol_length):
            for perm in itertools.permutations(string.ascii_uppercase, length):
                yield perm
