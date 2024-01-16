import scrapy

class MLBHitting2014Spider(scrapy.Spider):
    name = '2014_mlb_hitting_np'
    start_urls = [
        # NL West
        'https://www.baseball-reference.com/teams/SFG/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/ARI/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/LAD/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/COL/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/SDP/2014-roster.shtml',
        # NL Central
        'https://www.baseball-reference.com/teams/CHC/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/STL/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/PIT/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/CIN/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/MIL/2014-roster.shtml',
        # NL East
        'https://www.baseball-reference.com/teams/NYM/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/MIA/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/PHI/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/ATL/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/WSN/2014-roster.shtml',
        # AL West
        'https://www.baseball-reference.com/teams/OAK/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/LAA/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/SEA/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/HOU/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/TEX/2014-roster.shtml',
        # AL Central
        'https://www.baseball-reference.com/teams/KCR/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/CLE/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/MIN/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/CHW/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/DET/2014-roster.shtml',
        # AL East
        'https://www.baseball-reference.com/teams/NYY/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/BOS/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/TBR/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/BAL/2014-roster.shtml',
        'https://www.baseball-reference.com/teams/TOR/2014-roster.shtml',
    ]

    def parse(self, response):
        # iterate through each row in the roster table
        rows = response.css('#appearances > tbody > tr')
        for row in rows:
            # since the table does not have the player's primary position, we can
            # instead look at how many games they were "announced as a pitcher"
            # and infer that this means they are a pitcher
            num_games_pitched = row.css('td:nth-child(14)::text').get()
            if num_games_pitched == "0":
                # extract the player link
                player_link = row.css('th > a::attr(href)').get()
                if player_link:
                    # parse player's career table
                    yield response.follow(player_link, self.parse_player)

    def parse_player(self, response):
        # Your existing logic to scrape individual player pages
        name = response.css("#meta > div:nth-child(2) > h1 > span::text").get()
        hr_career = response.css("#batting_standard > tfoot > tr:nth-child(1) > td:nth-child(9)::text").get()
        ba_career = response.css("#batting_standard > tfoot > tr:nth-child(1) > td:nth-child(15)::text").get()
        
        yield {
            'name': name,
            'HR': hr_career,
            'BA': ba_career,
        }
