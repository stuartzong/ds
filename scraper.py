
import scrapy
import requests
from lxml import html

class AdSpider(scrapy.Spider):
    name = 'ad_spider'
    start_urls = ['https://www.vansky.com/info/zfbg09.html']
    def parse(self, response):
        SET_SELECTOR = '.freeAdPadding'
        for ad in response.css(SET_SELECTOR)[:3]:      
            href_selector ='a ::attr(href)'      
            href = ad.css(href_selector).extract_first()
            if href:
                pageContent=requests.get(response.urljoin(href))
                tree = html.fromstring(pageContent.content)
                yield {'phone': tree.xpath('//*[@id="info-phone"]/text()'), 
                       'wechat': tree.xpath('//div[contains(@class, "col-md-5")]/text()')[1].split('\n')[2], 
                       'title': tree.xpath('//*[@class="adsTitleFont"]/text()')
                      }
        
            

#         NEXT_PAGE_SELECTOR = '.freeAdPadding a ::attr(href)'
#         next_page = response.css(NEXT_PAGE_SELECTOR)#.extract_first()
#         if next_page:
#             phone_selector = '//*[@id="info-phone"]'
# #             print('xxxxxxxxxxxxxxxxxxxxxxx')
#             yield {
                
#                 'phone_number': next_page.xpath(phone_selector).extract_first(),
#             }
# #             yield scrapy.Request(
# #                 response.urljoin(next_page),
# #                 callback=self.parse
# #             )
