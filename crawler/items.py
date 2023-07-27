# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

class Recipe(scrapy.Item):
    recipe_url = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field(output_processor=TakeFirst())
    instructions = scrapy.Field()
    ingredients = scrapy.Field()
    online_rating = scrapy.Field(output_processor=TakeFirst())
    metadata = scrapy.Field(output_processor=TakeFirst())

class NewsAgency(scrapy.Item):
    country = scrapy.Field(output_processor=TakeFirst())
    scope = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field(output_processor=TakeFirst())
    focus = scrapy.Field(output_processor=TakeFirst())
    language = scrapy.Field(output_processor=TakeFirst())
    source_url = scrapy.Field(output_processor=TakeFirst())
