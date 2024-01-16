import scrapy

class MLBHitting2014Spider(scrapy.Spider):
    name = '2014_mlb_hitting'
    start_urls = ['https://www.baseball-reference.com/teams/KCR/2014-roster.shtml',
                  'https://www.baseball-reference.com/teams/SFG/2014-roster.shtml',
                  'https://www.baseball-reference.com/teams/ARI/2014-roster.shtml']

    def parse(self, response):
        print("URL:", response.url)  # Debugging: Print the current URL
        print("Response body:", response.text[:500])  # Print the first 500 characters of the response

        player_links = response.css('#appearances > tbody > tr > th > a::attr(href)').getall()
        print("Found player links:", len(player_links))  # Debugging: Print the number of links found

        for link in player_links:
            yield response.follow(link, self.parse_player)

    def parse_player(self, response):
        # Your existing logic to scrape individual player pages
        name = response.css("#meta > div:nth-child(2) > h1 > span::text").get()
        hr_career = response.css("#batting_standard > tfoot > tr:nth-child(1) > td:nth-child(9)::text").get()
        ba_career = response.css("#batting_standard > tfoot > tr:nth-child(1) > td:nth-child(15)::text").get()
        
        yield {
            'player\'s full name' : name,
            'career home runs' : hr_career,
            'career batting average' : ba_career,
        }
