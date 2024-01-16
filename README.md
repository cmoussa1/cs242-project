# Scrapy Notes

## installation requirements/prerequisites

First, check to see that you have Python (>= 3.6) and Scrapy installed on your
system. To install Scrapy:

```
pip3 install scrapy
```

## instructions on how to set up a Scrapy project

Inside of the directory of your choice, run:

```console
scrapy startproject my_project_name
```

There will be a number of folders and files created.

* `scrapy.cfg`: the project configuration file.
* `projectname/`: this directory contains your project’s Python modules.
* `projectname/items.py`: define the data structure for scraped data here.
* `projectname/pipelines.py`: process the scraped data (e.g., cleaning, storing to a database).
* `projectname/settings.py`: configure settings like user agent, concurrent requests, etc.
* `projectname/spiders/`: this directory will contain your spiders.

Inside the `spiders/` director, you can create a spider file using the
`scrapy genspider` command:

```console
scrapy genspider my_new_spider www.baseball-reference.com
```