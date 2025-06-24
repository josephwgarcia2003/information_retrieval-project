import scrapy
import hashlib
import re
from bs4 import BeautifulSoup
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class KsuSpider(CrawlSpider):
    name = 'ksu'
    allowed_domains = ['kennesaw.edu']
    start_urls = [
        'https://www.kennesaw.edu/',
        'https://ccse.kennesaw.edu/',
        'https://catalog.kennesaw.edu/'  # You can replace this with any other KSU page
    ]

    custom_settings = {
        'USER_AGENT': 'KSU CS4422-IRbot/0.1',
        'DOWNLOAD_DELAY': 2.0,
        'ROBOTSTXT_OBEY': True,
        'CLOSESPIDER_PAGECOUNT': 1000,
        'DEPTH_PRIORITY': 1,
        'SCHEDULER_DISK_QUEUE': 'scrapy.squeues.PickleFifoDiskQueue',
        'SCHEDULER_MEMORY_QUEUE': 'scrapy.squeues.FifoMemoryQueue',
    }

    rules = (
        Rule(LinkExtractor(allow_domains=['kennesaw.edu'], unique=True), callback='parse_items', follow=True),
    )

    def parse_items(self, response):
        entry = dict.fromkeys(['pageid', 'url', 'title', 'body', 'emails'])

        # Generate unique ID from URL
        url = response.url
        pageid = hashlib.md5(url.encode('utf-8')).hexdigest()

        # Get title
        title = response.xpath('//title/text()').get(default='')

        # Extract body text using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        body = soup.get_text(separator=' ', strip=True)

        # Extract email addresses using regex
        emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', response.text)

        # Fill the dictionary
        entry.update({
            'pageid': pageid,
            'url': url,
            'title': title,
            'body': body,
            'emails': emails
        })

        yield entry
