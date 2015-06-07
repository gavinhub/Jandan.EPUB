# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import time, re, hashlib

def art_serialize_text(text):
    return text[0]

def art_serialize_date(date):
    return time.strftime("%Y-%m-%d", date[0])

def art_serialize_content(content):
    pat = re.compile(r"src=[\'\"](http.+)[\'\"]")
    for line in range(len(content)):
        aim = pat.search(content[line])
        if aim:
            aim = aim.group(1)
            hashobj = hashlib.sha1()
            hashobj.update(aim.encode('utf-8'))
            content[line] = re.sub(aim, hashobj.hexdigest(), content[line])
    return "".join(content)


class ArticleItem(scrapy.Item):
    # Maybe used in pipeline... :]
    ITEM_TYPE = "art"
    
    # define the fields for your item here like:
    title  = scrapy.Field(serializer=art_serialize_text) # list [Unicode]
    author = scrapy.Field(serializer=art_serialize_text) # list [Unicode]
    date   = scrapy.Field(serializer=art_serialize_date) # list [time.struct_time]
    tag    = scrapy.Field(serializer=art_serialize_text) # list [Unicode]
    origin = scrapy.Field(serializer=art_serialize_text) # list [Unicode]
    content= scrapy.Field(serializer=art_serialize_content) # content
