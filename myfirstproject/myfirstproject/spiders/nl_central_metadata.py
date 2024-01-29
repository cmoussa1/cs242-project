from .base_spider import BaseSpider

class NLCentralSpider(BaseSpider):
    name = 'nl_central_meta'
    start_urls = (
        [f'https://www.baseball-reference.com/teams/MIL/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/CIN/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/CHC/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/PIT/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/STL/{year}-roster.shtml' for year in range(2003, 2024)]
    )
