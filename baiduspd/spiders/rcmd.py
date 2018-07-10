#!/usr/bin/python
# -*- coding: UTF-8 -*-

import scrapy

from baiduspd.items import BaiduspdItem



class RcmdSpider(scrapy.Spider):
    name = "rcmd"
    allowed_domains = ["baidu.com"]
    start_urls = []
    def __init__(self):
        src = "q.list"
        base = "http://www.baidu.com/s?wd="
        # start_urls = []
        f = open(src, "r")
        for l in f:
            self.start_urls.append(base+l)
        f.close()

    def parse(self, resp):
        item = BaiduspdItem()
        title = resp.xpath("//title/text()").extract_first(default="none_baidu")
        title = title.split("_")[0]
        item['query'] = title
        print title
        print resp.url
        topics = []
        for sel in resp.css(".cr-title.c-clearfix"):
            # item['topic'] +
            topics.append(sel.xpath('span/text()').extract_first())
            # item['topic'] = map(lambda x: x.encode("utf-8"), item['topic'])
            # print item['topic'][0]
            # item['query'] = 'q'
        item['topic'] = topics
        print item
        yield item
