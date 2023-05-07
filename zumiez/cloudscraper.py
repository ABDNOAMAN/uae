import cloudscraper

## Create CloudScraper Instance -> Chrome browser // Windows OS // Desktop
scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'ios',
        'desktop': False,
        'mobile': True,
    }
)
 
## Make Request
response = scraper.get("http://somesite.com")
