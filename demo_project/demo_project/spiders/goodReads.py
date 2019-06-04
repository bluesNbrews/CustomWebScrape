import scrapy

class GoodReadsSpider(scrapy.Spider):
    #identity
    name = 'goodReads'

    #reuests
    def start_requests(self):
        urls = {
            'https://www.goodreads.com/quotes?page=1'
        }

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    #response
    def parse(self, response):
        for quote in response.selector.xpath("//div[@class='quote']"):
            yield {
                'text': quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
                'author': quote.xpath(".//div[@class='quoteText']/child::span").extract_first(),
                'tags': quote.xpath(".//div[@class='greyText smallText left']/a/text()").extract()
            }
