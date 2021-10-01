import scrapy
# from ..items import QuotetutorailItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re


class MailSpider(CrawlSpider):
    name = 'mails'
    allowed_domains = ['scrapebay.com']
    start_urls = [
        'http://scrapebay.com/'
    ]

    rules = (
        Rule(LinkExtractor(), callback='parse',
             follow=True),
             )

    def parse(self, response):
        emails = re.findall(r'[\w\.]+@[\w\.]+', response.text)

        for email in emails:
            if 'bootstrap' not in email:
                yield {
                    'URL': response.url,
                    'Email': email
                }



