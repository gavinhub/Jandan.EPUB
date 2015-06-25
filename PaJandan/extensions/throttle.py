from scrapy.contrib.throttle import AutoThrottle
from scrapy import log
import re
# should use a adapter to wrap AutoThrottle, but I am lazy....

class AutoThrottleWithList(AutoThrottle):
	''' AutoThrottle with a name list so that the spider limits its 
		speed only for the sites on the list '''

	# param: site_list: list contains the domain to be limited 
	def __init__(self, crawler):
		self.limit_list = crawler.settings.getdict("LIMIT_SITES")
		log.msg("lode AutoThrottle", level=log.INFO)
		super(AutoThrottleWithList, self).__init__(crawler)

	def _adjust_delay(self, slot, latency, response):
		"""override AutoThrottle._adjust_delay()"""
		reg = re.search(r'http[s]?://([^/]+).*', response.url)
		res_domain = reg.group(1)
		if res_domain in self.limit_list:
			new_delay = min(max(self.mindelay, latency, (slot.delay + latency) / 2.0), self.maxdelay)
			# Dont adjust delay if response status != 200 and new delay is smaller
			# than old one, as error pages (and redirections) are usually small and
			# so tend to reduce latency, thus provoking a positive feedback by
			# reducing delay instead of increase.
			if response.status == 200 or new_delay > slot.delay:
			    slot.delay = new_delay
		else:
			slot.delay = 0.0