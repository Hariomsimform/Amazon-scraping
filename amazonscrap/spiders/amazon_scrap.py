import scrapy
from ..items import AmazonscrapItem

class AmazonScrapSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?bbn=3&rh=n%3A3%2Cp_n_publication_date%3A1250226011&dc&qid=1656066085&rnid=1250225011&ref=lp_3_nr_p_n_publication_date_0']

    def parse(self, response):
        items = AmazonscrapItem()
        product_name =response.css('.a-size-medium::text').extract()
        print(product_name)
        product_author = response.css('.a-color-secondary .a-size-base:nth-child(2)').css('::text').extract()
        print(product_author)
        product_price = response.css('.s-price-instructions-style .a-price-whole').css('::text').extract()
        print(product_price)
        product_img = response.css('.s-image::attr(src)').extract()
        print(product_img)
        items['product_name']=product_name
        items['product_author']=product_author
        items['product_price']=product_price
        items['product_img']=product_img

        yield items 
