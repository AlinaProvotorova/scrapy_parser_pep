import re
import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEPS_DOMAIN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEPS_DOMAIN]
    start_urls = [f'https://{PEPS_DOMAIN}/']

    def parse(self, response):
        for pep_link in response.css('section#pep-content tr a::attr(href)'):
            yield response.follow(pep_link, callback=self.parse_pep)

    @staticmethod
    def parse_pep(response):
        number, name = response.css(
            '.page-title::text').get().split(' – ', 1)
        yield PepParseItem({
            'number': re.sub(r'\D', r'', number),
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        })
