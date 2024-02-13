## how to run any of the spiders

To run any of the spiders, go to the root of the Scrapy project directory and
run:

```console
$ scrapy crawl posey_stats
```

This will tell Scrapy to start crawling using the `posey_stats` spider. Output
will be printed to the console telling you that the spider is running as well
as the data it is scraping.

To redirect the scraped data to a file, you can run:

```console
$ scrapy crawl posey_stats -o posey_stats_output.json
```

To control the amount of logging level that is output while the spider is
running, use the `-L` option:

```console
scrapy crawl posey_stats -L INFO
```

---

## MLB Data Spider

The `BaseSpider` class contains all of the scraping/parsing code for our
project. We are interested in gathering player data from active MLB rosters
over the course of the 2022 and 2023 MLB seasons. For each player on the active
roster, we crawl to their home profile page and scrape their statistics from
the given season.

Since player statistics are different between a pitcher and a position player,
we need to check for the player's primary position before we search for certain
statistics. For this, a `isPitcher` parameter of type `bool` is passed in the
callback for each player's home page. Certain statistics of interest are then
gathered and placed in the JSON object for each player.

Finally, another crawl is attempted for each player's **Biographical
Information** section on their Wiki page on Baseball-Reference. If one exists,
the text of this section is scraped and also placed in a key-value pair in the
player's JSON object.

A separate spider contains all of the starting links that we are interested in:
`mlb_2022_2023.py`. This Python file contains the links for every team's 2022
and 2023 roster, grouped by division.

In summary, the crawling process looks like the following:

1. start from a team's active roster page from 2022 or 2023 page
2. for each team's active roster page:
3. gather metadata for player
4. crawl to each player's home profile page
5. scrape statistics from 2022 or 2023 page
6. crawl to player's Wiki page (if one exists)
7. scrape "Biographical Information" from Wiki page (if one exists)

The spider scrapes about 1.3 GB of data in total and runs in just under seven
hours. About 6700 GET requests are made and just over 3200 items are stored in
the resulting JSON file. Below is a breakdown of some interesting statistics
reported by Scrapy:

```
2024-01-30 17:35:54 [scrapy.extensions.feedexport] INFO: Stored json feed (3279 items) in: json_data/mlb_data.json
2024-01-30 17:35:54 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{
    'downloader/request_bytes': 3227315,
    'downloader/request_count': 6667,
    'downloader/request_method_count/GET': 6667,
    'downloader/response_bytes': 273457667,
    'downloader/response_count': 6667,
    'elapsed_time_seconds': 24519.853224,
    'httpcompression/response_bytes': 1492804240,
    'item_scraped_count': 3279,
    'request_depth_max': 2,
}
```
