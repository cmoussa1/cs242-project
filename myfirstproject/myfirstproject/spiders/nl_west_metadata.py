from .base_spider import BaseSpider

class NLWestSpider(BaseSpider):
    name = 'nl_west_meta'
    start_urls = (
        [f'https://www.baseball-reference.com/teams/SFG/{year}-roster.shtml' for year in range(2003, 2024)]
        [f'https://www.baseball-reference.com/teams/ARI/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/COL/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/LAD/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/SDP/{year}-roster.shtml' for year in range(2003, 2024)]
    )
