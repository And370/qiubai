import scrapy
from qiubai.items import QiubaiItem


class qiubaispider(scrapy.Spider):
    name = 'qiubai'
    print('\n\n\n\n这是一只测试爬虫。\n\n\n\n交流AND370yeah@163.com\n\n\n')
    start_urls = ['https://www.qiushibaike.com/']
    def parse(self, response):
    
        content =response.xpath("//div[@class='content']/span").extract()
        newcontent=[cont.replace(' ','').replace('\n','').replace('<span>','').replace('<br>','').replace('</span>','').replace('<spanclass="contentForALL">查看全文','') for cont in content]
        qb_image_url=response.xpath("//div[@id='content-left']//div[@class='thumb']//img/@src").extract()
        
        item=QiubaiItem()
        item['content']=newcontent
        item['image_urls']=qb_image_url
        yield item
