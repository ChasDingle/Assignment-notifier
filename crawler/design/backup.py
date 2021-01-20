import scrapy
from ..items import DesignItem
#allows us to access code from the library making us not need to write much code
class  brightspaceSpider (scrapy.Spider):
   #name of the code we use in terminal
    name ="design_crawl"
#website that you are scraping
    start_urls = ['https://brightspace.ucc.on.ca/d2l/lms/dropbox/user/folders_list.d2l?ou=12586&isprv=0']

#tells the codes to go to the source code
    def parse(self, response):
        items = DesignItem()
        #if else statement
        #tells the code to only extract the code with this tag
        test_name = response.css('title::text').extract()

        items['test_name'] = test_name

        #used to get the list. Not return because scrapy uses a generator in itself so you need yeild to co-operate with scrapys generator
        yield items
