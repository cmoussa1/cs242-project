from .base_spider import BaseSpider

class ALCentralSpider(BaseSpider):
    name = 'al_central_meta'
    start_urls = (
        [f'https://www.baseball-reference.com/teams/CLE/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/MIN/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/DET/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/CHW/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/KCR/{year}-roster.shtml' for year in range(2003, 2024)]
    )
