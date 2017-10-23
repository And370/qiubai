# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import time
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request

class QiubaiImagePipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        print('\n\n\n\n\n开始请求了!!!!!!!!!!!!!!!!!\n\n\n\n\n')
        for image_url in item['image_urls']:
            yield Request('http:'+image_url)
        print('\n\n\n\n\n开始存图了!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n\n')
        
    def item_completed(self,results,item,info):
        image_paths=[x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem('图片未下载好%s'%image_paths)
        item['image_paths']=image_paths
        print('\n\n\n正在保存图片!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n')
        return item
class QiubaiPipeline(object):
    def open_spider(self,spider):
        self.file = codecs.open('qiubai0.0.json', 'w', encoding='utf-8')
        
    def process_item(self, item, spider):
        #print (time)
        #localtime = asctime(localtime(time.time())
        #print (strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        line='the content is:'+'\n'
        for i in range(len(item['content'])):
            content={'content':item['content'][i]}
            #content={'content':item['content'][i].replace(' ','').replace('\n','').replace('<span>','').replace('<br>','').replace('</span>','')}
            line=line+json.dumps(content,ensure_ascii=False)+'\n'
        line=line+'the url is:'+'\n'
        for i in range(len(item['image_urls'])):
            image_urls={'image_urls':item['image_urls'][i]}
            line=line+json.dumps(image_urls,ensure_ascii=False)+'\n'
        self.file.write(line)
        return item

    def closed_spider(self, spider):
        self.file.close()
