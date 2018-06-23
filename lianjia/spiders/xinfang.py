# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem

class XinfangSpider(scrapy.Spider):
    name = 'xinfang'
   # allowed_domains = ['https://wh.fang.lianjia.com/loupan/pg']
    start_urls = [ ]
    for i in range(1,138):
        url = 'https://wh.fang.lianjia.com/loupan/pg{0}/'.format(i)
        start_urls.append(url)


    def parse(self, response):

        housess = response.css('.resblock-list')
        for house in housess:
            try:
                item = LianjiaItem()
                item['name'] = house.css('.resblock-desc-wrapper .resblock-name .name::text').extract_first()
                item['type'] = house.css('.resblock-desc-wrapper .resblock-name .resblock-type::text').extract_first()
                item['sale'] = house.css('.resblock-desc-wrapper .resblock-name .sale-status::text').extract_first()
                item['site'] = house.css('.resblock-desc-wrapper .resblock-location span::text').extract()
                item['detail_site'] = house.css('.resblock-desc-wrapper .resblock-location a::text').extract_first()
                item['area'] = house.css('.resblock-desc-wrapper .resblock-area span::text').extract_first()
                item['tags'] = house.css('.resblock-desc-wrapper .resblock-tag span::text').extract()
                item['price'] = house.css('.resblock-desc-wrapper .resblock-price .main-price .number::text').extract_first()
                item['all_price'] = house.css('.resblock-desc-wrapper .resblock-price .second::text').extract_first()
            except:
                return None
            yield item
