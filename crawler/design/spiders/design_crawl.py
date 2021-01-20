import scrapy
from ..items import DesignItem
#allows us to access code from the library making us not need to write much code
from scrapy.utils.response import open_in_browser
class  brightspaceSpider (scrapy.Spider):
   #name of the code we use in terminal
    name ="design_crawl"
#website that you are scraping
    start_urls = ['https://brightspace.ucc.on.ca/d2l/lms/dropbox/user/folders_list.d2l?ou=12586&isprv=0']

#tells the codes to go to the source code
    def parse(self, response):
        #gets the login information so that the program can see the source code of Brightspace
        token = response.css('from input::attr (value)').extract_first()
        return Formrequest.from_response(response,formdata={
            'csrf_token' : token,
            'email adress' : 'chas.dingle@ucc.on.ca'
            'password' #passwordhere change to input later



        },callback = self.start_scraping)

    def start_scraping(self,response):
        open_in_browser(response)
        items = DesignItem()
        # if else statement
        # tells the code to only extract the code with this tag
        test_name = response.css('title::text').extract()

        items['test_name'] = test_name

        # used to get the list. Not return because scrapy uses a generator in itself so you need yeild to co-operate with scrapys generator
        yield items