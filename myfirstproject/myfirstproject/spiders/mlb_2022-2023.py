from .base_spider import BaseSpider

class MLB2022_2023Spider(BaseSpider):
    name = 'mlb_2022_2023'
    start_urls = (
        # NL West
        [f'https://www.baseball-reference.com/teams/SFG/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/ARI/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/COL/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/LAD/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/SDP/{year}-roster.shtml' for year in range(2022, 2024)] +
        # NL Central
        [f'https://www.baseball-reference.com/teams/MIL/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/CIN/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/CHC/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/PIT/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/STL/{year}-roster.shtml' for year in range(2022, 2024)] +
        # NL East
        [f'https://www.baseball-reference.com/teams/NYM/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/MIA/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/PHI/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/ATL/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/WSN/{year}-roster.shtml' for year in range(2022, 2024)] +
        # AL West
        [f'https://www.baseball-reference.com/teams/OAK/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/HOU/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/LAA/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/SEA/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/TEX/{year}-roster.shtml' for year in range(2022, 2024)] +
        # AL Central
        [f'https://www.baseball-reference.com/teams/CLE/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/MIN/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/DET/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/CHW/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/KCR/{year}-roster.shtml' for year in range(2022, 2024)] +
        # AL East
        [f'https://www.baseball-reference.com/teams/NYY/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/BOS/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/TBR/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/TOR/{year}-roster.shtml' for year in range(2022, 2024)] +
        [f'https://www.baseball-reference.com/teams/BAL/{year}-roster.shtml' for year in range(2022, 2024)]
    )
