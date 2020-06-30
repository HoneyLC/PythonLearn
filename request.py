import sys

import requests
from retrying import retry
from selenium import webdriver

import pytesseract
from PIL import Image

"""
爬虫
"""

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

# 模拟登陆  请求session获得cookie
session = requests.session()
url = "http://zhibo.renren.com/"
data = {"password": "123456789", "username": "guanzhanggui"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/78.0.3904.97 Safari/537.36"}
post = session.post(url, data=data, headers=headers)

# 保存图片

response = requests.get("https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png")
# with open("baidu.png", "wb") as f:
#    f.write(response.content)

# retrying

# json数据转化(xpath)   json.load() json转为python数据类型 ;  json.dumps() python数据类型转json
# 正则表达式    re.compile()  pattern.match(从头找)  pattern.search(找一个) pattern.findall(查询所有)  pattern.sub(替换)
# xpath 处理数据:   https://whnoteimage.oss-cn-qingdao.aliyuncs.com/xpath.png
#                  https://whnoteimage.oss-cn-qingdao.aliyuncs.com/xpath2.png
#                   from lxml import etree  ;
#                   html = etree.HTML(text),etree.tostring(html).decode(),html.xpath("xpath语句")

#  csv文件  表格


# 多线程爬虫  使用队列存储每一步的结果,   threading.Thread(target=方法);


# 爬取动态HTML

# selenium(Web自动化测试工具)和phantomJS(无界面浏览器)

# w = webdriver.chrome;     创建客户端
# w.get("https://www.baidu.com");  发送请求
# w.find_element_by_id("kw").send_keys();  通过id元素定位
# w.find_elements_by_xpath("kw");  通过xml元素定位
# w.find_elements_by_link_text("kw");  通过文本元素定位
# w.find_elements_by_partial_link_text("kw");  通过文本元素定位
# w.find_elements_by_tag_name("kw");  通过标签名元素定位
# w.find_elements_by_class_name("kw");  通过class名元素定位
# w.find_elements_by_css_selector("kw");  通过css选择器名元素定位
# w.switch_to.frame();  切换iframe
# element.text 获取文本信息
# element.get_attribute("") 获得属性
# w.set_window_size(1000,200)  设置窗口大小
# w.save_screenshot("./baidu.png")
# w.get_cookies() 获得cookies
# w.delete_cookie(""); 删除指定cookie
# w.delete_all_cookies(); 删除所有的cookie
# cookies = {i["name"]:i["values"] for i in cookies}  cookie获得指定的值
# w.page_source  浏览器中的element的内容
# w.current_url  当前url地址
# w.quit()
# time.sleep; 页面等待
# WebDriverWait(w,10).until(EC.presence_of_element_located(By.ID,"myDynamicElement")); 显示等待 设置最长等待时间
# w.implicitly_wait(10)

# Tesseract图像翻译成文字的ocr库(光学文字识别)


image_open = Image.open("C:\\Users\\Administrator\\Desktop\\2.png")
string = pytesseract.image_to_string(image_open)
print(string)

