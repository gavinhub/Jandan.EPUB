import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.loader import ItemLoader
from PaJandan.items import ArticleItem

import time as Time
import datetime
import re

class ArtSpider(CrawlSpider):
    name = 'jandan-article'
    spider_status = {'running': True}
    allowed_domains = ['jandan.net']
    start_urls = None  # initialize in __init__

    rules = [
            # Article pages, don't follow
            Rule(LinkExtractor(allow=['/([0-9]+/){3}.+html']), callback='parse_art', follow=False),
        ]

    def __init__(self, dates="DAYS", *args, **kwargs):
        super(ArtSpider, self).__init__(*args, **kwargs)
        # Spider starts from `start ruls`
        #   add urls to this list
        ArtSpider.start_urls = []

        date_list = []
        date_length = 0
        if dates == "DAYS" and kwargs['length']:
            ft = datetime.datetime.now()
            length = int(kwargs['length'])
        elif dates == "RANGE" and kwargs['from'] and ['to']:
            ft = datetime.datetime.strptime(kwargs['from'], '%Y/%m/%d')
            edt = datetime.datetime.strptime(kwargs['to'], '%Y/%m/%d')
            length = (Time.mktime(edt.timetuple()) - Time.mktime(ft.timetuple())) / 86400 + 1
        else:
            raise Exception("Option Error")

        for i in range(length-1, -1, -1):
            date_list.append((ft - datetime.timedelta(days=i)).strftime("%Y/%m/%d"))

        # translate int to 2-digits number
        # digit = lambda s: str(s) if len(str(s))==2 else '0'+str(s)
        for d in date_list:
            ArtSpider.start_urls.append("http://jandan.net/%s/" % d)
    
    # There can be several parse functions to be used according to Rules
    # But we don't need it in this project :]

    # Deal with response
    def parse_art(self, response):

        time_str = re.search(r'/([0-9]+/){3}', response.url)
        time = Time.strptime(time_str.group(0), "/%Y/%m/%d/")

        # Load Item with `ItemLoader`
        l = ItemLoader(item=ArticleItem(), response=response)
        l.add_xpath("title", "//div[@class='post f']/h1/a/text()")
        l.add_xpath("author", "//div[@class='post f']/div[@class='time_s']/a/text()")
        l.add_value("date", time)
        l.add_xpath("tag", "//a[@rel='tag']/text()")
        l.add_xpath("origin", "//div[@class='post f']/p/em/a[2]/@href")
        # content
        content = response.xpath("//div[@class='post f'][1]/*")[4:-4]
        l.add_value("content", content.extract())
        # images: put urls into image_urls[], then pipline will download them.
        imgs = content.xpath("img/@src")
        l.add_value("image_urls", imgs.extract())
        # English Title, cut from url
        en_title = re.search(r'([^/]+)\.html', response.url).group(1)
        l.add_value("en_title", [en_title])
        return l.load_item()
