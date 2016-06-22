# Useful references

## YQL and Yahoo Finance

- http://stackoverflow.com/questions/27543776/yahoo-finance-webservice-api
- http://stackoverflow.com/questions/14795726/getting-data-from-yahoo-finance
- http://stackoverflow.com/questions/5246843/how-to-get-a-complete-list-of-ticker-symbols-from-yahoo-finance
- If using the the sectors yql table, the currently deployed binding XML appears to be broken, so you instead need to point to one hosted elsewhere using the `use` statement. E.g. `use "http://singingtree.io/yahoo.finance.sectors.xml" as yahoo.finance.sectors; select * from yahoo.finance.sectors;`

## Crawling ticker codes

- https://github.com/Benny-/Yahoo-ticker-symbol-downloader
- Looks like hitting https://finance.yahoo.com/lookup limits the number of results available to 2000~. So if you attempt to search and then crawl the search result pages you may end up missing alot of codes due to this.
- Historically yahoo had APIs available to query ticker codes, but as of 2016 sounds like these have been closed.
- Brute forcing ticker codes is problematic due to rate limiting on checks available.
  - 2,000 requests per hour for public YQL access, or 20,000 with a cap at 100,000 a day if logged in. This would still take year(s) to crawl 3-5 char ticker codes assuming alphanumeric usage.
  - Possible to read them by going through the sectors and industry tables.

