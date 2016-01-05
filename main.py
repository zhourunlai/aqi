#!/usr/bin/env python
# coding=utf-8

import urllib2
import threading
from time import ctime
from bs4 import BeautifulSoup


# 爬虫
def spider(i):
    url = 'http://datacenter.mep.gov.cn/report/air_daily/air_dairy.jsp?city=%E6%AD%A6%E6%B1%89%E5%B8%82&startdate=2015-07-01&enddate=2015-12-31&page=' + i
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    all = soup.find_all('td', 'report1_2')
    for one in all:
        print one.text


# 单线程
def single_thread():
    print '单线程开始: ' + ctime() + '\n'
    spider('1')
    spider('2')
    spider('3')
    spider('4')
    spider('5')
    spider('6')
    spider('7')


# 多线程
def multi_thread():
    print '多线程开始: ' + ctime() + '\n'
    threads = []
    t1 = threading.Thread(target=spider, args=('1',))
    threads.append(t1)
    t2 = threading.Thread(target=spider, args=('2',))
    threads.append(t2)
    t3 = threading.Thread(target=spider, args=('3',))
    threads.append(t3)
    t4 = threading.Thread(target=spider, args=('4',))
    threads.append(t4)
    t5 = threading.Thread(target=spider, args=('5',))
    threads.append(t5)
    t6 = threading.Thread(target=spider, args=('6',))
    threads.append(t6)
    t7 = threading.Thread(target=spider, args=('7',))
    threads.append(t7)
    for t in threads:
        t.start()


if __name__ == '__main__':
    single_thread()
    # multi_thread()
