import scrapy
from mySpider.items import MyspiderItem

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['guanzhanggui.com']  # 允许排重的范围
    start_urls = ['https://www.guanzhanggui.com/']  # 最开始的请求的url地址

    def parse(self, response):
        # 处理start_url的响应
        response_xpath = response.xpath("//title/text()").extract()
        print(response_xpath)
        item = MyspiderItem()
        item["name"] = {"name": "张三", "age": 19}
        yield item
