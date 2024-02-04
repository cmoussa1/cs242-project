import scrapy

class BaseSpider(scrapy.Spider):
    def parse(self, response):
        # extract the year from the URL
        year = response.url.split('/')[-1].split('-')[0]
        host = 'https://www.baseball-reference.com'
        print("processing URL:", response.url)
        # iterate through each row in the roster table
        rows = response.css('#appearances > tbody > tr')
        for row in rows:
            # get metadata from the parent table that contains active roster
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

            # var to determine if player is pitcher or not by looking at
            # number of games they were announced as a pitcher in
            num_games_pitched = row.css('td[data-stat="G_p_app"]::text').get()
            
            # extract the player's home page link from parent table
            player_link = row.css('th > a::attr(href)').get()

            # begin construction of JSON object to store scraped data
            player = {
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
                'yearly_salary': salary,
            }
            
            yield scrapy.Request(host + player_link, 
                                 callback=self.parse_individual_stats,
                                 cb_kwargs={
                                    'player': player,
                                    'isPitcher': num_games_pitched != "0",
                                    'year': year,
                                 },
                                 dont_filter = True)

    def parse_individual_stats(self, response, player, isPitcher, year):
        player['html_body'] = response.text

        # add the is_pitcher attr to the payload before anything else
        player['is_pitcher'] = isPitcher

        # scrape individual stats for the year in question
        # we use the isPitcher boolean to determine which stats to add to the payload
        if isPitcher:
            individualRow = response.css('#pitching_standard\.' + year)
            player['wins'] = individualRow.css('td[data-stat="W"]::text').get()
            player['losses'] = individualRow.css('td[data-stat="L"]::text').get()
            player['win_loss_pct'] = individualRow.css('td[data-stat="win_loss_perc"]::text').get()
            player['earned_run_avg'] = individualRow.css('td[data-stat="earned_run_avg"]::text').get()
            player['complete_games'] = individualRow.css('td[data-stat="CG"]::text').get()
            player['shutouts'] = individualRow.css('td[data-stat="SHO"]::text').get()
            player['saves'] = individualRow.css('td[data-stat="SV"]::text').get()
            player['innings_pitched'] = individualRow.css('td[data-stat="IP"]::text').get()
            player['hits_allowed'] = individualRow.css('td[data-stat="H"]::text').get()
            player['runs_allowed'] = individualRow.css('td[data-stat="R"]::text').get()
            player['earned_runs_allowed'] = individualRow.css('td[data-stat="ER"]::text').get()
            player['home_runs_allowed'] = individualRow.css('td[data-stat="HR"]::text').get()
            player['pitcher_walks'] = individualRow.css('td[data-stat="BB"]::text').get()
            player['pitcher_intentional_walks'] = individualRow.css('td[data-stat="IBB"]::text').get()
            player['pitcher_strikeouts'] = individualRow.css('td[data-stat="SO"]::text').get()
            player['pitcher_hbp'] = individualRow.css('td[data-stat="HBP"]::text').get()
            player['balks'] = individualRow.css('td[data-stat="BK"]::text').get()
            player['wild_pitches'] = individualRow.css('td[data-stat="WP"]::text').get()
            player['batters_faced'] = individualRow.css('td[data-stat="batters_faced"]::text').get()
            player['earned_run_avg_plus'] = individualRow.css('td[data-stat="earned_run_avg_plus"]::text').get()
            player['fip'] = individualRow.css('td[data-stat="fip"]::text').get()
            player['whip'] = individualRow.css('td[data-stat="whip"]::text').get()
            player['hits_per_nine'] = individualRow.css('td[data-stat="hits_per_nine"]::text').get()
            player['home_runs_per_nine'] = individualRow.css('td[data-stat="home_runs_per_nine"]::text').get()
            player['bases_on_balls_per_nine'] = individualRow.css('td[data-stat="bases_on_balls_per_nine"]::text').get()
            player['strikeouts_per_nine'] = individualRow.css('td[data-stat="strikeouts_per_nine"]::text').get()
            player['strikeouts_per_base_on_balls'] = individualRow.css('td[data-stat="strikeouts_per_base_on_balls"]::text').get()
            player['home_runs_per_nine'] = individualRow.css('td[data-stat="home_runs_per_nine"]::text').get()
            #TODO: need to update the selector for awards_summary to return an array
            #grabbing just the text does not work, they do some special logic to build up award lists for players
            player['award_summary'] = individualRow.css('td[data-stat="award_summary"]::text').get()

        else:
            individualRow = response.css('#batting_standard\.' + year)
            player['plate_attempts'] = individualRow.css('td[data-stat="PA"]::text').get()
            player['at_bats'] = individualRow.css('td[data-stat="AB"]::text').get()
            player['runs'] = individualRow.css('td[data-stat="R"]::text').get()
            player['hits'] = individualRow.css('td[data-stat="H"]::text').get()
            player['doubles'] = individualRow.css('td[data-stat="2B"]::text').get()
            player['triples'] = individualRow.css('td[data-stat="3B"]::text').get()
            player['home_runs'] = individualRow.css('td[data-stat="HR"]::text').get()
            player['runs_batted_in'] = individualRow.css('td[data-stat="RBI"]::text').get()
            player['stolen_bases'] = individualRow.css('td[data-stat="SB"]::text').get()
            player['caught_stealing'] = individualRow.css('td[data-stat="CS"]::text').get()
            player['batter_walks'] = individualRow.css('td[data-stat="BB"]::text').get()
            player['batter_strikeouts'] = individualRow.css('td[data-stat="SO"]::text').get()
            player['batting_avg'] = individualRow.css('td[data-stat="batting_avg"]::text').get()
            player['onbase_pct'] = individualRow.css('td[data-stat="onbase_perc"]::text').get()
            player['slugging_pct'] = individualRow.css('td[data-stat="slugging_perc"]::text').get()
            player['onbase_plus_slugging_pct'] = individualRow.css('td[data-stat="onbase_plus_slugging"]::text').get()
            player['onbase_plus_slugging_plus'] = individualRow.css('td[data-stat="onbase_plus_slugging_plus"]::text').get()
            player['total_bases'] = individualRow.css('td[data-stat="TB"]::text').get()
            player['double_plays_grounded_into'] = individualRow.css('td[data-stat="GIDP"]::text').get()
            player['batter_hbp'] = individualRow.css('td[data-stat="HBP"]::text').get()
            player['sac_hits'] = individualRow.css('td[data-stat="SH"]::text').get()
            player['sac_flies'] = individualRow.css('td[data-stat="SF"]::text').get()
            player['batter_intentional_walks'] = individualRow.css('td[data-stat="IBB"]::text').get()
            #TODO: need to update the selector for awards_summary to return an array
            #grabbing just the text does not work, they do some special logic to build up award lists for players
            player['award_summary'] = individualRow.css('td[data-stat="award_summary"]::text').get()

        # get hyperlink to player's wiki page on Baseball-Reference
        player_info_link = response.xpath('//a[contains(text(), "View Player Info")]/@href').get()

        # check if link exists
        if player_info_link:
            yield scrapy.Request(
                response.urljoin(player_info_link),
                callback=self.parse_player_info,
                cb_kwargs={'player': player},
                dont_filter = True
            )
        else:
            # if the link does not exist, just yield the player info we already have
            yield player

    def parse_player_info(self, response, player):
        # Locate the <h2> tag with the <span> ID 'Biographical Information'
        # and select following <p> tags until another header is reached
        bio_paragraphs = response.xpath('//h2[span/@id="Biographical_Information"]/following-sibling::p[preceding-sibling::h2[1][span/@id="Biographical_Information"]]')

        # extract only the text content from each paragraph, excluding <a> tags or other elements
        bio_text = ' '.join([''.join(para.xpath('.//text()').getall()) for para in bio_paragraphs])
        # add the bio to the player object that is yielded
        player['biographical_information'] = bio_text.strip()

        yield player

    #multiple webpages from one spider YT vid: https://www.youtube.com/watch?v=LfSsbJtby-M (found this helpful)

