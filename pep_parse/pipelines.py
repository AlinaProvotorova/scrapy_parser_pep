# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import csv
import datetime as dt

from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_summary = defaultdict(int)

    def process_item(self, item, spider):
        self.status_summary[item['status']] += 1
        return item

    def close_spider(self, spider):
        RESULTS_DIR = BASE_DIR / 'results'
        RESULTS_DIR.mkdir(exist_ok=True)
        now_formatted = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open(
                RESULTS_DIR / f'status_summary_{now_formatted}.csv',
                mode='w', encoding='utf-8'
        ) as f:
            writer = csv.writer(f, dialect=csv.unix_dialect)
            writer.writerows([
                ('Статус', 'Количество'),
                *self.status_summary.items(),
                ('Total', sum(self.status_summary.values())),
            ])
