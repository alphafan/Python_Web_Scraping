# A simple example for scrapy

import scrapy


class AlphaFanSpider(scrapy.Spider):

    name = 'alphafan'
    start_urls = [
        'https://alphafan.github.io/'
    ]

    def parse(self, response):
        yield {     # return some results
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ""),
            'url': response.url,
        }

        urls = response.css('a::attr(href)').re(r'^/.+?/$')     # find all sub urls
        for url in urls:
            yield response.follow(url, callback=self.parse)     # it will filter duplication automatically
