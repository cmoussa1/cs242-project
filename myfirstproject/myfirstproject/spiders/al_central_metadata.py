from .base_spider import BaseSpider

class ALCentralSpider(BaseSpider):
    name = 'al_central_meta'
    start_urls = (
        [f'https://www.baseball-reference.com/teams/CLE/2023-roster.shtml'] +
        [f'https://www.baseball-reference.com/teams/MIN/2023-roster.shtml'] +
        [f'https://www.baseball-reference.com/teams/DET/2023-roster.shtml'] +
        [f'https://www.baseball-reference.com/teams/CHW/2023-roster.shtml'] +
        [f'https://www.baseball-reference.com/teams/KCR/2023-roster.shtml']
    )
