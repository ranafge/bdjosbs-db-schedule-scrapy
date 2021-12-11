# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

class BdjobscircularItem(scrapy.Item):
    # define the fields for your item here like:
    jobTitle = scrapy.Field(input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),)
    jobDetailsLink = scrapy.Field(input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),)
    companyName = scrapy.Field(input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),)
    
    # def __str__(self) -> str:
    #     return f'xxxxxxxxxxxxxxxxxxxxxxxx {self.jobTitle}'
    
