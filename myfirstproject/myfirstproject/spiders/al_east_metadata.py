from .base_spider import BaseSpider

class ALCentralSpider(BaseSpider):
    name = 'al_east_meta'
    start_urls = (
        [f'https://www.baseball-reference.com/teams/NYY/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/BOS/{year}-roster.shtml' for year in range(2003, 2024)] +
        # 2003-2007: "Tampa Bay Devil Rays", 2008-Present: "Tampa Bay Rays"
        [f'https://www.baseball-reference.com/teams/TBD/{year}-roster.shtml' for year in range(2003, 2008)] +
        [f'https://www.baseball-reference.com/teams/TBR/{year}-roster.shtml' for year in range(2008, 2024)] +
        [f'https://www.baseball-reference.com/teams/TOR/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/BAL/{year}-roster.shtml' for year in range(2003, 2024)]
    )
