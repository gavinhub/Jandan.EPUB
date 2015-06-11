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
    pat = re.compile(r"src=[\'\"](http[^ ]+)[\'\"]")
    for line in range(len(content)):
        aim = pat.search(content[line])
        if aim:
            aim = aim.group(1)
            hashobj = hashlib.sha1()
            try:
                hashobj.update(str(aim))
            except Exception, e:
                scrapy.log.msg("===============>" + aim + "<================")
            
            content[line] = re.sub(aim, "../images/" + hashobj.hexdigest() + ".jpg", content[line])
    return "".join(content)

def art_image_serialize(image_urls):
    names = []
    for url in image_urls:
        hashobj = hashlib.sha1()
        hashobj.update(url)
        names.append(hashobj.hexdigest())
    return names

def art_none_serialize(obj):
    return None


class ArticleItem(scrapy.Item):
    # Maybe used in pipeline... :]
    ITEM_TYPE = "art"
    
    # define the fields for your item here like:
    title   = scrapy.Field(serializer=art_serialize_text) # list [Unicode]
    author  = scrapy.Field(serializer=art_serialize_text) # list [Unicode]
    date    = scrapy.Field(serializer=art_serialize_date) # list [time.struct_time]
    tag     = scrapy.Field(serializer=art_serialize_text) # list [Unicode]
    origin  = scrapy.Field(serializer=art_serialize_text) # list [Unicode]
    en_title= scrapy.Field(serializer=art_serialize_text) # list [Unicode]
    content = scrapy.Field(serializer=art_serialize_content) # content
    images  = scrapy.Field(serializer=art_none_serialize) # containing images' information
    image_urls = scrapy.Field(serializer=art_image_serialize) # images' url
