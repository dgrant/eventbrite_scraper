# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "eventbrite"
    allowed_domains = ['eventbrite.ca']
    start_urls = ['https://www.eventbrite.ca/e/raina-telgemeier-tickets-68295733377']

#    def start_requests(self):
#        urls = [
#            'https://www.eventbrite.ca/e/raina-telgemeier-tickets-68295733377',
#        ]
#        for url in urls:
#            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log("Got body:" + response.body.decode())
        sold_out_text = response.xpath('//div[@data-automation = "micro-ticket-box-status"]/text()').get().strip()
        if sold_out_text != "Sold Out":
            self.log("Tickets available!")
        else:
            self.log("Sold out!")
