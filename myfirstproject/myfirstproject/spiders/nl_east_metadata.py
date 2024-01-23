from .base_spider import BaseSpider

class NLEastSpider(BaseSpider):
    name = 'nl_east_meta'
    start_urls = (
        [f'https://www.baseball-reference.com/teams/NYM/{year}-roster.shtml' for year in range(1962, 2024)] +
        [f'https://www.baseball-reference.com/teams/MIA/{year}-roster.shtml' for year in range(2012, 2024)] +
        [f'https://www.baseball-reference.com/teams/PHI/{year}-roster.shtml' for year in range(1886, 2024)] +
        [f'https://www.baseball-reference.com/teams/ATL/{year}-roster.shtml' for year in range(1966, 2024)] +
        [f'https://www.baseball-reference.com/teams/WSN/{year}-roster.shtml' for year in range(2005, 2024)]
    )
