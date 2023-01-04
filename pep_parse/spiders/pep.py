import re
import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep_link in response.css('section#pep-content tr a::attr(href)'):
            yield response.follow(pep_link, callback=self.parse_pep)

    @staticmethod
    def parse_pep(response):
        yield PepParseItem({
            'number': re.sub(
                r'[^0-9]+', r'',
                response.css('.page-title::text').get()
            ),
            'name': re.sub(
                r'PEP [0-9]+ . ', r'',
                response.css('.page-title::text').get()
            ),
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        })
