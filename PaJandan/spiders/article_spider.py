import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.loader import ItemLoader
from PaJandan.items import ArticleItem

import time as Time
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

    def __init__(self, month=None, *args, **kwargs):
        super(ArtSpider, self).__init__(*args, **kwargs)
        ArtSpider.start_urls = []
        # If month not indecated, set to `this month` 
        if not month:
           month = Time.strftime("%Y/%m")
        # Traversal the days
        date = month.split('/')
        Y, m = int(date[0]), int(date[1])
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dayrange = range(1, days[m]+1)
        if m == 2 and (Y%400==0 or (Y%4==0 and Y%100!=0)):
            dayrange.append(29)
        digit = lambda s: str(s) if len(str(s))==2 else '0'+str(s)
        for d in dayrange:
            datestr = str(Y) + '/' + digit(m) + '/' + digit(d)
            ArtSpider.start_urls.append("http://jandan.net/%s" % datestr)
        
    
    def parse_art(self, response):

        time_str = re.search(r'/([0-9]+/){3}', response.url)
        time = Time.strptime(time_str.group(0), "/%Y/%m/%d/")

        # Load Item
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
