# scrapy框架: 使用了Twisted异步网络框架
# 让爬虫更快
# Scrapy的爬虫流程: https://whnoteimage.oss-cn-qingdao.aliyuncs.com/3.png

# 入门使用
# 安装:pip --default-timeout=100 install 库名称 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
# 创建scrapy项目: scrapy startproject 项目名称
# 生成一个爬虫; scrapy genspider 爬虫名称 "网址"
# scrapy crawl demo 在控制台输入命令 scrapy crawl 爬虫名称
# settings: LOG_LEVEL = "WARNING" 设置日志等级
# settings: LOG_FIEL = "路径" 保存日志到指定的文件里
# 通过yield把数据传给pipeline
# 开启pipelines 在settings 打开  ITEM_PIPELINES = {开启pipelines的路径: 300,} 可以定义多个pipelines, 数字越小优先级越高

# 翻页请求: yield scrapy.Request(next_page_url,callback=self.parse)
# scrapy.Item
# scrapy shell "url"


