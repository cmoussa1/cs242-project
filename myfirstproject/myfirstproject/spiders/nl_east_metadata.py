from .base_spider import BaseSpider

class NLEastSpider(BaseSpider):
    name = 'nl_east_meta'
    start_urls = (
        [f'https://www.baseball-reference.com/teams/NYM/{year}-roster.shtml' for year in range(2003, 2024)] +
        # 2003-2011: "Florida Marlins", 2012-Present: "Miami Marlins"
        [f'https://www.baseball-reference.com/teams/FLA/{year}-roster.shtml' for year in range(2003, 2012)] +
        [f'https://www.baseball-reference.com/teams/MIA/{year}-roster.shtml' for year in range(2012, 2024)]
        [f'https://www.baseball-reference.com/teams/PHI/{year}-roster.shtml' for year in range(2003, 2024)] +
        [f'https://www.baseball-reference.com/teams/ATL/{year}-roster.shtml' for year in range(2003, 2024)] +
        # # 2003-2004: "Montreal Expos", 2005-Present: "Washington Nationals"
        [f'https://www.baseball-reference.com/teams/MON/{year}-roster.shtml' for year in range(2003, 2005)] +
        [f'https://www.baseball-reference.com/teams/WSN/{year}-roster.shtml' for year in range(2005, 2024)]
    )
