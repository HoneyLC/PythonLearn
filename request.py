import sys

import requests

# 爬虫

# 请求示例
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/78.0.3904.97 Safari/537.36"}

response = requests.get("http://www.baidu.com", headers=headers)
print(response.status_code);
print(response.headers)
print(response.request.url)
print(response.url)
print(response.content.decode("utf-8"));

# format
print("阿{}拉丁".format("哈哈哈"))
print("阿{}拉{}丁".format([1, 2, 3], {"key": "value"}));


# 贴吧爬虫
class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name;
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/78.0.3904.97 Safari/537.36"}

    def get_url_list(self):
        url_list = [];
        for i in range(5):
            url_list.append(self.url_temp.format(i * 50))
        return url_list;

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, pagenum):
        file_path = "{}--第{}页.html".format(self.tieba_name, pagenum + 1);
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        # 1.构建url列表
        url_list = self.get_url_list()
        # 2.发送请求
        for url in url_list:
            html_str = self.parse_url(url)
            index = url_list.index(url);
            self.save_html(html_str, index);
        # 3. 保存


if __name__ == '__main__':
    spider = TiebaSpider("李毅")
    # spider.run()

# 翻译工具

query_string = sys.argv[0];  # 获取外部的的数据  例如:test.py what  获得 test
print(query_string)

# 使用代理:  在requests.get()加上proxies参数
proxies = {"http": "http://123.57.76.102:80"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/78.0.3904.97 Safari/537.36"}
# response = requests.get("http://www.baidu.com", proxies=proxies, headers=headers)
# print(response.content)

# 模拟登陆
session = requests.session()
url = "https://www.guanzhanggui.com/systemadmin"
data = {"password": "123456789", "username": "guanzhanggui"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/78.0.3904.97 Safari/537.36"}
post = session.post(url, data=data, headers=headers)




