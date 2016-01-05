#!/usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import static


def draw_pollutant():
    # 计算每月首要污染物的出现天数
    print static.pollutant()

    N = 6
    oneMeans = static.pollutant()[0]

    # the x locations for the groups
    ind = np.arange(N)

    # the width of the bars
    width = 0.25

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, oneMeans, width, color='r')

    twoMeans = static.pollutant()[1]
    rects2 = ax.bar(ind + width, twoMeans, width, color='y')

    threeMeans = static.pollutant()[2]
    rects3 = ax.bar(ind + width * 2, threeMeans, width, color='b')

    # add some
    ax.set_ylabel(u'天数')
    ax.set_title(u'各月首要污染物出现天数')
    ax.set_xticks(ind + width)
    ax.set_xticklabels((u'7月', u'8月', u'9月', u'10月', u'11月', u'12月'))

    ax.legend((rects1[0], rects2[0], rects3[0]), (u'PM2.5', u'PM10', u'臭氧8小时'))

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2, 1.1 * height, '%d' % int(height), ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    plt.show()


def draw_rank(month):
    # 计算当前月或半年空气质量等级的相对比例
    print static.rank(month)

    # 创建一个图形区域 长10 宽6
    figure(1, figsize=(10, 6))

    # 坐标轴起始点为0.1,0.1从左下开始，长度占整个区域的0.6，高占0.8
    ax = axes([0.1, 0.1, 0.6, 0.8])

    # 饼图的lables
    labels = '43%', '7%', '43%', '7%'

    # 饼图所分成的区域
    fracs = [6, 1, 6, 1]

    # 按分成的区域画饼图 并加上lables
    pie(fracs, labels=labels)

    # loc=5为在右侧后面是在针对坐标轴的位置
    legend((u"在理想范围以上: 6", u"在理想范围以下: 1", u"在理想范围内:   6", u"低血糖:         1"), loc=5,
           bbox_to_anchor=(1.5, 0.5))

    # text针对坐标轴的坐标
    text(1.8, 0.5, u"结果", fontsize=12)

    title(u"空气质量等级的相对比例")

    show()


if __name__ == '__main__':
    # draw_pollutant()
    draw_rank(7)
