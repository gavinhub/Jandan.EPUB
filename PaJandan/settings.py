# -*- coding: utf-8 -*-

# Scrapy settings for PaJandan project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'PaJandan'

SPIDER_MODULES = ['PaJandan.spiders']
NEWSPIDER_MODULE = 'PaJandan.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'MyUserAgent/1.0'

# Set download speed
DOWNLOAD_DELAY = 3

# Pipelines
ITEM_PIPELINES = {
	'PaJandan.pipelines.PajandanPipeline': 100,
	'scrapy.contrib.pipeline.images.ImagesPipeline': 1
	}

# Image
IMAGES_STORE = 'images/'
IMAGES_EXPIRES = 90
