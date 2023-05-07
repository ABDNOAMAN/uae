import time
import scrapy
from scrapy.utils.reactor import install_reactor 
install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
from scrapy import Selector
from scrapy_playwright.page import PageMethod
import logging
from datetime import datetime
#from data import links
#from data import number



def get_headers(s, sep=': ', strip_cookie=True, strip_cl=True, strip_headers: list = []) -> dict():
    d = dict()
    for kv in s.split('\n'):
        kv = kv.strip()
        if kv and sep in kv:
            v=''
            k = kv.split(sep)[0]
            if len(kv.split(sep)) == 1:
                v = ''
            else:
                v = kv.split(sep)[1]
            if v == '\'\'':
                v =''
            # v = kv.split(sep)[1]
            if strip_cookie and k.lower() == 'cookie': continue
            if strip_cl and k.lower() == 'content-length': continue
            if k in strip_headers: continue
            d[k] = v
    return d

def should_abort_request(req):

    if req.resource_type == "image":
        logging.log(logging.INFO, f"Ignoring Image {req.url}")
        return True
    if req.method.lower() == 'post':
        logging.log(logging.INFO, f"Ignoring {req.method} {req.url} ")
        return True

    return False




class XSpider(scrapy.Spider):
    name = "x"
    custom_settings = {
        
        #'DOWNLOAD_DELAY': 10, # 2 seconds of delay 

        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "headless": True,
#            "proxy": {
 #               "server": "socks5://127.0.0.1:9050"

  #          },

#            "proxy": {
#                "server": "https://proxy.scrapeops.io/:5353" ,
#                "username": "scrapeops.headless_browser_mode=true",
#                "password": "e4ea08af-ef35-4354-885d-e75b34979a52",
#            },

        },
        

        'FEEDS': {
#            f'links-{datetime.now()}.csv': 
             'emiratesbd-ffffinal.csv':
            {
                'format': 'csv'
            }},
        'PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT': '100000',
        'PLAYWRIGHT_ABORT_REQUEST': should_abort_request ,

    }


    def start_requests(self):



#        for k,l in zip(links() , number()) :
#            for i in range (1, ((int(l))+1)):
#                yield scrapy.Request(
#                    url=f"{k}-{i}",
             yield scrapy.Request(
#        
              url = 'https://emiratesbd.ae/dubai/place/150032/mariot-kitchen-equipment' ,
               #  headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Content-Type': 'application/x-www-form-urlencoded', 'Dnt': '1', 'Origin': 'https://www.zumiez.com', 'Referer': 'https://www.zumiez.com/mens.html?p=1&__cf_chl_tk=_aUAK4lbDSe_FaJ6C9jEdHWUfixKAb43zS1E1ALT9jQ-1683380057-0-gaNycGzNDxA', 'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '"Linux"', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'},

           dont_filter=True,
            callback=self.parse,
                meta=dict(
                playwright = True,
                playwright_include_page = True ,
                playwright_page_methods = [


                    #PageMethod('click', selector='//*[@id="challenge-stage"]/div/label/input'),               
                    



                         ],
                errback =self.errback ,
                                
                
            ))
            

    async def parse(self, response):
                
        page = response.meta["playwright_page"]

        a = response.css('.listar-btnquickinfo').xpath('a/text()').get()
        b = response.css('.listar-reviewcategory')
        print('#################################################################################')
        print(b)
        await page.close()
      

#        yield{
#             'Category': a,
#             'Business Name' : b ,
#             'Website' : c , 
#             'Facebok' : d ,
#             'Instagram' : e ,
#             'Twitter' : f ,
#             'LinkedIn' : g ,
#             'YouTube' : h ,
#             'Tiktok' : i ,
#             'Email' : k ,
#             'Contact No.' : l ,
#             'Address' : m ,
#             'Location' : n ,
#             'Map' : o ,
#             'Link' : r
#        }
        
        
    async def errback(self,failure) :
        page = failure.request.meta["playwright_page"]
        await page.close()



