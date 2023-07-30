# Abyz Crawler

This is a crawler for the website [Abyz News Links](http://www.abyznewslinks.com), extracting the news agencies alongside with their metadata per country.

This readme is intended for developers.

Note that some files in this repository are encrypted via [vauly](https://github.com/sebschlicht/vauly).
Check the project's setup file on how to setup a local development environment for this project and use or avoid vauly.

## Run Crawler

>Most commands need to be run from within the virtual environment, which can be activated via: `source venv/bin/activate`

First, provide the following environment variables, specifying the URI and the database name of the MongoDB you want to persist the news agencies to:

* MONGO_URI
* MONGO_DB

(e.g. via `export`)

Run the following command to crawl news agencies and store them inside the local database:

    scrapy crawl abyz-news-agencies

## Run MongoDB

Start up the container via:

    docker-compose up -d
