# -*- coding: utf-8 -*-
import scrapy


class OverwatchItem(scrapy.Item):
    title = scrapy.Field()
    name = scrapy.Field()
