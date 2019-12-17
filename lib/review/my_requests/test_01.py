#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading
import requests


class RequestWebContent(object):
    """批量抓取网页内容
    """

    def __init__(self, urls):
        self.urls = urls

    def get_web_content(self, url, file_name):
        """抓取单个网页内容
        Args:
            url            type(str)        需要抓取网页内容的url
            file_name      type(str)        存储网页内容的文件名
        """
        html = requests.get(url)
        with open(file_name, 'w') as f:
            f.write(html.content)

    def single_thread(self):
        """单线程抓取网页内容
        """
        start_time = time.time()
        for index, url in enumerate(self.urls):
            self.get_web_content(url, 'single_wed_%s.txt' % index)
        print 'Used time: %s' % (time.time() - start_time)

    def multi_threads(self):
        """多线程抓取网页内容
        """
        start_time = time.time()
        ths = list()
        for index, url in enumerate(self.urls):
            th = threading.Thread(target=self.get_web_content, args=(url, 'multi_wed_%s.txt' % index))
            th.start()
            ths.append(th)
        for th in ths:
            th.join()
        print 'Used time: %s' % (time.time() - start_time)


if __name__ == '__main__':
    my_urls = ['https://www.baidu.com/'] * 3
    request_web = RequestWebContent(my_urls)
    print 'single thread...'
    request_web.single_thread()
    print 'multi threads...'
    request_web.multi_threads()