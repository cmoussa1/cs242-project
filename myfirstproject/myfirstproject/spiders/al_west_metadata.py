from .base_spider import BaseSpider

class ALWestSpider(BaseSpider):
    name = 'al_west_meta'
    start_urls = (
        [f'https://www.baseball-reference.com/teams/OAK/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/HOU/{year}-roster.shtml' for year in range(2003, 2024)] +
        # 2003-2004: "California Angels", 2005-Present: "Los Angeles Angels of Anaheim"
        [f'https://www.baseball-reference.com/teams/CAL/{year}-roster.shtml' for year in range(2003, 2005)] +
        [f'https://www.baseball-reference.com/teams/LAA/{year}-roster.shtml' for year in range(2005, 2024)] +
        [f'https://www.baseball-reference.com/teams/SEA/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/TEX/{year}-roster.shtml' for year in range(2003, 2024)]
    )
