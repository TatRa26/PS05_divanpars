import scrapy

class DivanLightingSpider(scrapy.Spider):
    name = "divan_lighting"
    allowed_domains = ["divan.ru"]
    # URL страницы категории освещения (или другая подходящая категория)
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # Ищем все элементы освещения на странице
        items = response.css('div._Ud0k')  # Подбираем актуальный класс-контейнер

        for item in items:
            yield {
                # Название источника освещения
                'name': item.css('div.lsooF span::text').get(),
                # Цена источника освещения
                'price': item.css('div.pY3d2 span::text').get(),
                # Ссылка на детальную страницу
                'url': item.css('a').attrib['href']
            }

