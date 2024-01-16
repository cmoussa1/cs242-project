import scrapy
import sys

# run 'scrapy crawl posey_stats' to run this crawler
class PoseyStatsSpider(scrapy.Spider):
    name = "posey_stats"
    allowed_domains = ["www.baseball-reference.com"]
    # web page for Buster Posey's career statistics on Baseball-Reference
    start_urls = ["https://www.baseball-reference.com/players/p/poseybu01.shtml"]

    def parse(self, response):
        # define CSS selectors to extract the data desired

        # example 1: scraping the player's full name
        name = response.css("#meta > div:nth-child(2) > h1 > span::text").get()
        # example 2: getting the player's career HR total using XPath
        hr_total = response.css("#info > div.stats_pullout > div.p1 > div:nth-child(4) > p::text").get()
        # example 3: getting the player's career AVG
        ba_career = response.css("#batting_standard > tfoot > tr:nth-child(1) > td:nth-child(15)::text").get()

        # get the size of each item
        name_size = sys.getsizeof(str(name))
        hr_total_size = sys.getsizeof(str(hr_total))
        ba_career_size = sys.getsizeof(str(ba_career))

        total_data_size = (name_size + hr_total_size + ba_career_size) / 1048576

        # data will be returned as a Python dict
        yield {
            'player\'s full name' : name,
            'total home runs' : hr_total,
            'career batting average' : ba_career,
            'total data size (MB)' : total_data_size,
        }

