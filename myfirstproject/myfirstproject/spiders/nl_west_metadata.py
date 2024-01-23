import scrapy

class NLWestSpider(scrapy.Spider):
    name = 'nl_west_meta'
    start_urls = (
        [f'https://www.baseball-reference.com/teams/SFG/{year}-roster.shtml' for year in range(1958, 2024)] +
        [f'https://www.baseball-reference.com/teams/ARI/{year}-roster.shtml' for year in range(1998, 2024)] +
        [f'https://www.baseball-reference.com/teams/COL/{year}-roster.shtml' for year in range(1993, 2024)] +
        [f'https://www.baseball-reference.com/teams/LAD/{year}-roster.shtml' for year in range(1958, 2024)] +
        [f'https://www.baseball-reference.com/teams/SDP/{year}-roster.shtml' for year in range(1969, 2024)]
    )

    def parse(self, response):
        # Extract the year from the URL
        year = response.url.split('/')[-1].split('-')[0]
        print("processing URL:", response.url)
        # iterate through each row in the roster table
        rows = response.css('#appearances > tbody > tr')
        for row in rows:
            # get all of the data we are interested in
            name = row.css('th > a::text').get()
            age = row.css('td[data-stat="age"]::text').get()
            height = row.css('td[data-stat="height"]::text').get()
            weight = row.css('td[data-stat="weight"]::text').get()
            dob = row.css('td[data-stat="date_of_birth"]::text').get()
            exp = row.css('td[data-stat="experience"]::text').get()
            games_played = row.css('td[data-stat="G_all"]::text').get()
            games_started = row.css('td[data-stat="GS"]::text').get()
            war = row.css('td[data-stat="WAR"]::text').get()
            salary = row.css('td[data-stat="Salary"]::text').get()

            # return the object
            yield {
                'year': year,
                'name': name,
                'age': age,
                'height': height,
                'weight': weight,
                'dob': dob,
                'exp': exp,
                'games_played': games_played,
                'games_started': games_started,
                'WAR': war,
                'yearly salary': salary,
            }
