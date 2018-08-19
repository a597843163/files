# -*- coding: utf-8 -*-

from selenium import webdriver
# 超时错误
from selenium.common.exceptions import TimeoutException
# 不知道
from selenium.webdriver.common.by import By
# 显式等待使WebdDriver 等待某个条件成立时继续执行，否则在达到最大时长时抛弃超时异常
from selenium.webdriver.support.ui import WebDriverWait
# 不知道
from selenium.webdriver.support import expected_conditions as EC
# 不知道
from scrapy.http import HtmlResponse
# 输出日志信息
from logging import getLogger


class SeleniumMiddleware():
    def __init__(self, timeout=None, service_args=[]):
        # 当前模块日志
        self.logger = getLogger(__name__)
        # 设置超时时间
        self.timeout = timeout
        # 生成webdriver的对象
        self.browser = webdriver.PhantomJS(service_args=service_args,executable_path=r'F:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        # 控制浏览器窗口大小 几乎全屏
        self.browser.set_window_size(1400, 700)
        # 超时设置/等待时间过长自动停止
        self.browser.set_page_load_timeout(self.timeout)
        # 设置时间内，默认每隔一段时间检测一次当前页面元素是否存
        # 在，如果超过设置时间检测不到则抛出异常。
        self.wait = WebDriverWait(self.browser, self.timeout)
    
    def __del__(self):
        self.browser.close()
    
    def process_request(self, request, spider):
        """
        用PhantomJS抓取页面
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        # 输出debug日志信息
        self.logger.debug('PhantomJS is Starting')
        print(request.meta)
        page = request.meta.get('page', 1)
        print(page)
        try:
            # 打开请求的url
            self.browser.get(request.url)
            # 如果page大于1
            if page > 1:
                # 找到底部跳转页面的输入框input
                input = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
                # 找到跳转页面的"确定"按钮
                submit = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
                # 清除输入框内容
                input.clear()
                # 然后输入内容
                input.send_keys(page)
                # 点击确认按钮
                submit.click()
            # '''判断指定的元素中是否包含了预期的字符串，返回布尔值'''
            self.wait.until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
            # '''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))
