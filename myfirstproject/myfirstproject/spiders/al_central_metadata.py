from .base_spider import BaseSpider

class ALCentralSpider(BaseSpider):
    name = 'al_central_meta'
    start_urls = (
        [f'https://www.baseball-reference.com/teams/CLE/2023-roster.shtml']
    )