#!/usr/bin/python
# -*- coding: UTF-8 -*-

import scrapy

from baiduspd.items import BaiduspdItem



class RcmdWapSpider(scrapy.Spider):
    name = "rcmdwap"
    allowed_domains = ["baidu.com"]
    start_urls = []
    def __init__(self):
        src = "q.list"
        # base = "http://m.baidu.com/s?word=%E5%AD%99%E6%82%9F%E7%A9%BA"
        base = "http://m.baidu.com/s?word="
        # self.start_urls = [base]
        # """
        f = open(src, "r")
        for l in f:
            self.start_urls.append(base+l)
        f.close()
        # """

    def parse(self, resp):
        item = BaiduspdItem()
        title = resp.xpath("//title/text()").extract_first(default="none_baidu")
        title = title.split("-")[0].strip()
        item['query'] = title
        print title
        print resp.url
        # print "======="
        # print resp.body
        topics = []
        for sel in resp.css("h3.c-title.c-gap-top-small"):
            # item['topic'] +
            topics.append(sel.xpath('text()').extract_first())
            # item['topic'] = map(lambda x: x.encode("utf-8"), item['topic'])
            # print item['topic'][0]
            # item['query'] = 'q'
        topics = filter(lambda x: x !=None and u"_相关" in x, topics)
        topics = map(lambda x: x.split("_")[-1], topics)
        item['topic'] = topics
        print item
        yield item
