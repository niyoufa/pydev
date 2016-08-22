#coding=utf-8
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import Request
from newbie.items import NewbieItem
import newbie.mongo as mongo

import sys,pdb

domain = "http://toutiao.io/"
subject = 73104
subject_coll = mongo.get_coll("subject")

class MyShareSpider(Spider):
    name = "myshare_spider"
    allowed_domains = ["toutiao.io"]
    subjects = subject_coll.find()
    start_urls  = []
    for subject in subjects:
        start_urls.append("http://toutiao.io/subjects/"+str(subject['number']))

    def parse(self, response):
        sel = Selector(response)
        pagination = sel.xpath("//div[@class='text-center']/ul/li[@class='last']/a")
        page = int(pagination.xpath("@href").extract()[0].split("=")[1])
        share_url = pagination.xpath("@href").extract()[0].split("=")[0]
        new_share_urls = []
        for i in range(page):
            new_share_urls.append(domain + share_url + "=" +str(i+1))
        print new_share_urls

        for new_url in new_share_urls:
            yield Request(url=new_url, callback=self.parse_post)

    def parse_post(self,response):
        sel = Selector(response)
        posts = sel.xpath("//div[@class='posts']/div[@class='post']")
        items = []
        coll = mongo.get_coll("link")
        for post in posts:
            articel = post.xpath("div[@class='content']")
            title = articel.xpath("h3/a/text()").extract()[0].strip()
            href= articel.xpath("h3/a[@href]").xpath("@href").extract()[0].strip()
            source =  articel.xpath("div[@class='meta']/text()").extract()[0].strip()
            item = NewbieItem()
            item["title"] = title
            item["href"] = href
            item["source"] = source
            item["subject"] = subject
            item["type"] = "toutiao.share"
            items.append(item)
            query_params = {
                "href":href,
                "subject":subject,
            }
            if coll.find(query_params).count()>0:
                continue
            else:
                coll.save(item)
        return items
