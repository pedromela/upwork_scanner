import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess, Crawler
from spiders.homepage_spider import UpworkHomeSpider
from spiders.profile_settings_spider import UpworkProfileSettingsSpider
from upwork_controller import UpworkController

process = CrawlerProcess({
                'FEED_FORMAT': 'json',
                'FEED_URI': 'result.json'
                })

def home_spider_ended(spider, reason):
    process.stop()
    run_profile_spider(spider.upwork_controller)

def run_home_spider(controller):
    process.settings.set('FEED_URI', 'home.json')
    process.crawl(UpworkHomeSpider, upwork_controller=controller)

    for crawler in process.crawlers:
        crawler.signals.connect(home_spider_ended, signal=scrapy.signals.spider_closed)

    process.start()


def run_profile_spider(controller):
    process.settings.set('FEED_URI', 'profile.json')
    process.crawl(UpworkProfileSettingsSpider, upwork_controller=controller)
    process.start()
    

if __name__ == "__main__":
    controller = UpworkController()
    run_home_spider(controller)