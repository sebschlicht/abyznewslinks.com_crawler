db = db.getSiblingDB('abyz_news_links');
db.createCollection('news_agencies');
db.news_agencies.createIndex({ 'url': 1 });
db.news_agencies.createIndex({ 'language': 1 });
