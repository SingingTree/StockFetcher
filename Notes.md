# Useful references

## YQL and Yahoo Finance

- http://stackoverflow.com/questions/27543776/yahoo-finance-webservice-api
- http://stackoverflow.com/questions/14795726/getting-data-from-yahoo-finance
- http://stackoverflow.com/questions/5246843/how-to-get-a-complete-list-of-ticker-symbols-from-yahoo-finance

## Crawling ticker codes

- https://github.com/Benny-/Yahoo-ticker-symbol-downloader
- Looks like hitting https://finance.yahoo.com/lookup limits the number of results available to 2000~. So if you attempt to search and then crawl the search result pages you may end up missing alot of codes due to this.
- Historically yahoo had APIs available to query ticker codes, but as of 2016 sounds like these have been closed.