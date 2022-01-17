import scrapy
from ..items import MyscraperItem

class bookSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/category/books/travel_2',
'https://books.toscrape.com/catalogue/category/books/mystery_3', 'https://books.toscrape.com/catalogue/category/books/historical-fiction_4', 'https://books.toscrape.com/catalogue/category/books/sequential-art_5']
    genres = ['travel', 'mystery', 'historical-fiction', 'sequential-art']
    genre_number = 2

    def parse(self, response):

        genre = response.xpath('//*[@id="default"]/div/div/div/div/div[1]/h1/text()').get()
        for book in response.css('article.product_pod'):

            items = MyscraperItem() 

            items['link'] = book.css('a').attrib["href"]
            items['title'] =  book.css('a::text').get()
            items['genre'] = genre
            items['price'] = float(book.css('p.price_color::text').get().replace('£', ''))
            yield items

        is_next_page = response.css('li.next a').attrib["href"]

        if is_next_page is not None:
            
            yield response.follow(is_next_page, callback = self.parse)

    