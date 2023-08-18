import scrapy
import json
import re

class NbsSpider(scrapy.Spider):
    name = 'articles'
    start_urls = [
        'https://nbs.sk/wp-json/nbs/v1/post/list?_locale=user'
    ]

    def start_requests(self):
        request_body = {"lang":"en","limit":"20","offset":"0","filter":{"lang":"en"},"onlyData":"true"}
        yield scrapy.Request('https://nbs.sk/wp-json/nbs/v1/post/list?_locale=user',
                             method='POST',
                             body=json.dumps(request_body),
                             headers={"Content-Type":"application/json"},
                             callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        titles = re.findall('"h3">[\sa-zA-Záňť0-9(),.’–-]*<',str(data))
        titles = re.sub('"h3">|<',"",str(titles))
        print(titles)