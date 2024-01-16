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