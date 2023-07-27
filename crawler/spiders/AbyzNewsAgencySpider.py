# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
import yaml

from crawler.loaders.abyz.NewsAgencyUtils import extract_news_agencies

import logging
import logging.config

PREFIX = 'abyz_'

with open(PREFIX + 'logging.yml', 'r') as log_config:
    logging.config.dictConfig(yaml.safe_load(log_config.read()))

links_logger = logging.getLogger('links')
crawled_logger = logging.getLogger('crawled')

class AbyzNewsAgencySpider(scrapy.spiders.Spider):
    name = 'abyz-news-agencies'
    allowed_domains = [
        'www.abyznewslinks.com'
    ]
    start_urls = [
        'http://www.abyznewslinks.com/'
    ]
    allow_patterns = [
        r'https?:\/\/www\.abyznewslinks\.com\/.*'
    ]
    deny_patterns = []

    def __init__(self):
        self.link_extractor = LinkExtractor(
            allow_domains=self.allowed_domains,
            allow=self.allow_patterns,
            deny=self.deny_patterns,
            unique=True)

    def should_crawl_url(self, url):
        return True

    def parse(self, response):
        for item in extract_news_agencies(response):
            yield item
        crawled_logger.info(f'crawled {response.url}')

        for link in self.link_extractor.extract_links(response):
            links_logger.info(f'spotted {link.url}')
            yield scrapy.Request(link.url, callback=self.parse)
