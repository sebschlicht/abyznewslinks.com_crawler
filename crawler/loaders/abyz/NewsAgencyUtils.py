# -*- coding: utf-8 -*-
import re
from scrapy.loader import ItemLoader

from crawler.items import NewsAgency

pattern_breadcrumbs_name_prefix = re.compile(r'.+>')
pattern_line_break = re.compile(r'\n')
pattern_html_br = re.compile(r'<br/?>')
pattern_leading_html_elements = re.compile(r'^(<[^>]+>\s*)*')
pattern_trailing_html_elements = re.compile(r'(<[^>]+>\s*)*$')
pattern_newlines = re.compile(r'\n')

def extract_name_from_breadcrumbs(breadcrumbs_text):
    return pattern_breadcrumbs_name_prefix.sub('', breadcrumbs_text, 1).strip()

def strip_wrapping_html_elements(html):
    return pattern_trailing_html_elements.sub('', pattern_leading_html_elements.sub('', html))

def split_by_br(html):
    return pattern_html_br.split(html)

def strip_newlines(text):
    return pattern_newlines.sub('', text)

def split_lines_in_column(element):
    return [strip_wrapping_html_elements(strip_newlines(text)) for text in split_by_br(element.get())]

def extract_news_agencies(response):
    country = extract_name_from_breadcrumbs(response.xpath('normalize-space(string((//div)[3]))').get())
    if country:
        print(f'extracting news agencies of {country} from {response.url}')
        for tr in response.xpath('//tr'):
            tds = tr.xpath('td')
            if len(tds) >= 5:
                scopes = split_lines_in_column(tds[0])
                names = split_lines_in_column(tds[1])
                urls = tds[1].xpath('.//a/@href').getall()
                categories = split_lines_in_column(tds[2])
                focuses = split_lines_in_column(tds[3])
                languages = split_lines_in_column(tds[4])

                num_lines = min(len(scopes), len(names), len(urls), len(categories), len(focuses), len(languages))
                for i in range(num_lines):
                    loader = ItemLoader(item=NewsAgency(), response=response)
                    loader.add_value('country', country)
                    loader.add_value('scope', scopes[i])
                    loader.add_value('name', names[i])
                    loader.add_value('url', urls[i])
                    loader.add_value('category', categories[i])
                    loader.add_value('focus', focuses[i])
                    loader.add_value('language', languages[i])
                    loader.add_value('source_url', response.url)
                    if names[i] != 'Add Modify Link' and names[i] != 'Search ABYZ':
                        if len(names[i]) > 0:
                            yield loader.load_item()
