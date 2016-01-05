#!/usr/bin/env python
# coding=utf-8

import codecs
from decimal import *


def pollutant():
    fo = codecs.open("data.txt", "r", "utf-8")
    while 1:
        lines = fo.readlines(100000)
        if not lines:
            break
        i = 0
        count_one_1 = 0
        count_one_2 = 0
        count_one_3 = 0
        count_one_4 = 0
        count_one_5 = 0
        count_one_6 = 0
        count_two_1 = 0
        count_two_2 = 0
        count_two_3 = 0
        count_two_4 = 0
        count_two_5 = 0
        count_two_6 = 0
        count_three_1 = 0
        count_three_2 = 0
        count_three_3 = 0
        count_three_4 = 0
        count_three_5 = 0
        count_three_6 = 0
        while (i < 1092):
            if lines[i + 2].strip() >= "2015-07-01" and lines[i + 2].strip() < "2015-08-01":
                if lines[i + 5].strip() == u"PM2.5":
                    count_one_1 += 1
                if lines[i + 5].strip() == u"PM10":
                    count_two_1 += 1
                if lines[i + 5].strip() == u"臭氧8小时":
                    count_three_1 += 1
            if lines[i + 2].strip() >= "2015-08-01" and lines[i + 2].strip() < "2015-09-01":
                if lines[i + 5].strip() == "PM2.5":
                    count_one_2 += 1
                if lines[i + 5].strip() == u"PM10":
                    count_two_2 += 1
                if lines[i + 5].strip() == u"臭氧8小时":
                    count_three_2 += 1
            if lines[i + 2].strip() >= "2015-09-01" and lines[i + 2].strip() < "2015-10-01":
                if lines[i + 5].strip() == u"PM2.5":
                    count_one_3 += 1
                if lines[i + 5].strip() == u"PM10":
                    count_two_3 += 1
                if lines[i + 5].strip() == u"臭氧8小时":
                    count_three_3 += 1
            if lines[i + 2].strip() >= "2015-10-01" and lines[i + 2].strip() < "2015-11-01":
                if lines[i + 5].strip() == u"PM2.5":
                    count_one_4 += 1
                if lines[i + 5].strip() == u"PM10":
                    count_two_4 += 1
                if lines[i + 5].strip() == u"臭氧8小时":
                    count_three_4 += 1
            if lines[i + 2].strip() >= "2015-11-01" and lines[i + 2].strip() < "2015-12-01":
                if lines[i + 5].strip() == u"PM2.5":
                    count_one_5 += 1
                if lines[i + 5].strip() == u"PM10":
                    count_two_5 += 1
                if lines[i + 5].strip() == u"臭氧8小时":
                    count_three_5 += 1
            if lines[i + 2].strip() >= "2015-12-01" and lines[i + 2].strip() < "2016-01-01":
                if lines[i + 5].strip() == u"PM2.5":
                    count_one_6 += 1
                if lines[i + 5].strip() == u"PM10":
                    count_two_6 += 1
                if lines[i + 5].strip() == u"臭氧8小时":
                    count_three_6 += 1
            i += 6
        count_one = (count_one_1, count_one_2, count_one_3, count_one_4, count_one_5, count_one_6)
        count_two = (count_two_1, count_two_2, count_two_3, count_two_4, count_two_5, count_two_6)
        count_three = (count_three_1, count_three_2, count_three_3, count_three_4, count_three_5, count_three_6)
        return [count_one, count_two, count_three]


def rank(month):
    fo = codecs.open("data.txt", "r", "utf-8")
    while 1:
        lines = fo.readlines(100000)
        if not lines:
            break
        i = 0
        count_1_1 = 0
        count_1_2 = 0
        count_1_3 = 0
        count_1_4 = 0
        count_1_5 = 0
        count_1_6 = 0
        count_2_1 = 0
        count_2_2 = 0
        count_2_3 = 0
        count_2_4 = 0
        count_2_5 = 0
        count_2_6 = 0
        count_3_1 = 0
        count_3_2 = 0
        count_3_3 = 0
        count_3_4 = 0
        count_3_5 = 0
        count_3_6 = 0
        count_4_1 = 0
        count_4_2 = 0
        count_4_3 = 0
        count_4_4 = 0
        count_4_5 = 0
        count_4_6 = 0
        count_5_1 = 0
        count_5_2 = 0
        count_5_3 = 0
        count_5_4 = 0
        count_5_5 = 0
        count_5_6 = 0
        count_6_1 = 0
        count_6_2 = 0
        count_6_3 = 0
        count_6_4 = 0
        count_6_5 = 0
        count_6_6 = 0
        while (i < 1092):
            if lines[i + 2].strip() >= "2015-07-01" and lines[i + 2].strip() < "2015-08-01":
                if lines[i + 4].strip() == u"优":
                    count_1_1 += 1
                if lines[i + 4].strip() == u"良":
                    count_2_1 += 1
                if lines[i + 4].strip() == u"轻度污染":
                    count_3_1 += 1
                if lines[i + 4].strip() == u"中度污染":
                    count_4_1 += 1
                if lines[i + 4].strip() == u"重度污染":
                    count_5_1 += 1
                if lines[i + 4].strip() == u"严重污染":
                    count_6_1 += 1
            if lines[i + 2].strip() >= "2015-08-01" and lines[i + 2].strip() < "2015-09-01":
                if lines[i + 4].strip() == u"优":
                    count_1_2 += 1
                if lines[i + 4].strip() == u"良":
                    count_2_2 += 1
                if lines[i + 4].strip() == u"轻度污染":
                    count_3_2 += 1
                if lines[i + 4].strip() == u"中度污染":
                    count_4_2 += 1
                if lines[i + 4].strip() == u"重度污染":
                    count_5_2 += 1
                if lines[i + 4].strip() == u"严重污染":
                    count_6_2 += 1
            if lines[i + 2].strip() >= "2015-09-01" and lines[i + 2].strip() < "2015-10-01":
                if lines[i + 4].strip() == u"优":
                    count_1_3 += 1
                if lines[i + 4].strip() == u"良":
                    count_2_3 += 1
                if lines[i + 4].strip() == u"轻度污染":
                    count_3_3 += 1
                if lines[i + 4].strip() == u"中度污染":
                    count_4_3 += 1
                if lines[i + 4].strip() == u"重度污染":
                    count_5_3 += 1
                if lines[i + 4].strip() == u"严重污染":
                    count_6_3 += 1
            if lines[i + 2].strip() >= "2015-10-01" and lines[i + 2].strip() < "2015-11-01":
                if lines[i + 4].strip() == u"优":
                    count_1_4 += 1
                if lines[i + 4].strip() == u"良":
                    count_2_4 += 1
                if lines[i + 4].strip() == u"轻度污染":
                    count_3_4 += 1
                if lines[i + 4].strip() == u"中度污染":
                    count_4_4 += 1
                if lines[i + 4].strip() == u"重度污染":
                    count_5_4 += 1
                if lines[i + 4].strip() == u"严重污染":
                    count_6_4 += 1
            if lines[i + 2].strip() >= "2015-11-01" and lines[i + 2].strip() < "2015-12-01":
                if lines[i + 4].strip() == u"优":
                    count_1_5 += 1
                if lines[i + 4].strip() == u"良":
                    count_2_5 += 1
                if lines[i + 4].strip() == u"轻度污染":
                    count_3_5 += 1
                if lines[i + 4].strip() == u"中度污染":
                    count_4_5 += 1
                if lines[i + 4].strip() == u"重度污染":
                    count_5_5 += 1
                if lines[i + 4].strip() == u"严重污染":
                    count_6_5 += 1
            if lines[i + 2].strip() >= "2015-12-01" and lines[i + 2].strip() < "2016-01-01":
                if lines[i + 4].strip() == u"优":
                    count_1_6 += 1
                if lines[i + 4].strip() == u"良":
                    count_2_6 += 1
                if lines[i + 4].strip() == u"轻度污染":
                    count_3_6 += 1
                if lines[i + 4].strip() == u"中度污染":
                    count_4_6 += 1
                if lines[i + 4].strip() == u"重度污染":
                    count_5_6 += 1
                if lines[i + 4].strip() == u"严重污染":
                    count_6_6 += 1
            i += 6
        getcontext().prec = 1
        if month == 7:
            count_all_month = count_1_1 + count_2_1 + count_3_1 + count_4_1 + count_5_1 + count_6_1
            return [float(Decimal(count_1_1) / Decimal(count_all_month)),
                    float(Decimal(count_2_1) / Decimal(count_all_month)),
                    float(Decimal(count_3_1) / Decimal(count_all_month)),
                    float(Decimal(count_4_1) / Decimal(count_all_month)),
                    float(Decimal(count_5_1) / Decimal(count_all_month)),
                    float(Decimal(count_6_1) / Decimal(count_all_month))]
        elif month == 8:
            count_all_month = count_1_2 + count_2_2 + count_3_2 + count_4_2 + count_5_2 + count_6_2
            return [float(Decimal(count_1_2) / Decimal(count_all_month)),
                    float(Decimal(count_2_2) / Decimal(count_all_month)),
                    float(Decimal(count_3_2) / Decimal(count_all_month)),
                    float(Decimal(count_4_2) / Decimal(count_all_month)),
                    float(Decimal(count_5_2) / Decimal(count_all_month)),
                    float(Decimal(count_6_2) / Decimal(count_all_month))]
        elif month == 9:
            count_all_month = count_1_3 + count_2_3 + count_3_3 + count_4_3 + count_5_3 + count_6_3
            return [float(Decimal(count_1_3) / Decimal(count_all_month)),
                    float(Decimal(count_2_3) / Decimal(count_all_month)),
                    float(Decimal(count_3_3) / Decimal(count_all_month)),
                    float(Decimal(count_4_3) / Decimal(count_all_month)),
                    float(Decimal(count_5_3) / Decimal(count_all_month)),
                    float(Decimal(count_6_3) / Decimal(count_all_month))]
        elif month == 10:
            count_all_month = count_1_4 + count_2_4 + count_3_4 + count_4_4 + count_5_4 + count_6_4
            return [float(Decimal(count_1_4) / Decimal(count_all_month)),
                    float(Decimal(count_2_4) / Decimal(count_all_month)),
                    float(Decimal(count_3_4) / Decimal(count_all_month)),
                    float(Decimal(count_4_4) / Decimal(count_all_month)),
                    float(Decimal(count_5_4) / Decimal(count_all_month)),
                    float(Decimal(count_6_4) / Decimal(count_all_month))]
        elif month == 11:
            count_all_month = count_1_5 + count_2_5 + count_3_5 + count_4_5 + count_5_5 + count_6_5
            return [float(Decimal(count_1_5) / Decimal(count_all_month)),
                    float(Decimal(count_2_5) / Decimal(count_all_month)),
                    float(Decimal(count_3_5) / Decimal(count_all_month)),
                    float(Decimal(count_4_5) / Decimal(count_all_month)),
                    float(Decimal(count_5_5) / Decimal(count_all_month)),
                    float(Decimal(count_6_5) / Decimal(count_all_month))]
        elif month == 12:
            count_all_month = count_1_6 + count_2_6 + count_3_6 + count_4_6 + count_5_6 + count_6_6
            return [float(Decimal(count_1_6) / Decimal(count_all_month)),
                    float(Decimal(count_2_6) / Decimal(count_all_month)),
                    float(Decimal(count_3_6) / Decimal(count_all_month)),
                    float(Decimal(count_4_6) / Decimal(count_all_month)),
                    float(Decimal(count_5_6) / Decimal(count_all_month)),
                    float(Decimal(count_6_6) / Decimal(count_all_month))]
        else:
            count_half_year = count_1_1 + count_2_1 + count_3_1 + count_4_1 + count_5_1 + count_6_1 + count_1_2 + count_2_2 + count_3_2 + count_4_2 + count_5_2 + count_6_2 + count_1_3 + count_2_3 + count_3_3 + count_4_3 + count_5_3 + count_6_3 + count_1_4 + count_2_4 + count_3_4 + count_4_4 + count_5_4 + count_6_4 + count_1_5 + count_2_5 + count_3_5 + count_4_5 + count_5_5 + count_6_5 + count_1_6 + count_2_6 + count_3_6 + count_4_6 + count_5_6 + count_6_6
            return [float(Decimal(count_1_1 + count_1_2 + count_1_3 + count_1_4 + count_1_5 + count_1_6) / Decimal(
                    count_half_year)),
                    float(Decimal(count_2_1 + count_2_2 + count_2_3 + count_2_4 + count_2_5 + count_2_6) / Decimal(
                            count_half_year)),
                    float(Decimal(count_3_1 + count_3_2 + count_3_3 + count_3_4 + count_3_5 + count_3_6) / Decimal(
                            count_half_year)),
                    float(Decimal(count_4_1 + count_4_2 + count_4_3 + count_4_4 + count_4_5 + count_4_6) / Decimal(
                            count_half_year)),
                    float(Decimal(count_5_1 + count_5_2 + count_5_3 + count_5_4 + count_5_5 + count_5_6) / Decimal(
                            count_half_year)),
                    float(Decimal(count_6_1 + count_6_2 + count_6_3 + count_6_4 + count_6_5 + count_6_6) / Decimal(
                            count_half_year))]


def num():
    fo = codecs.open("data.txt", "r", "utf-8")
    while 1:
        lines = fo.readlines(100000)
        if not lines:
            break
        i = 0
        aqi_list = []
        while (i < 1092):
            aqi_list += [int(lines[i + 3])]
            i += 6
        # print list
        j = 0
        ave_list = []
        while (j < 180):
            ave_num = reduce(add, aqi_list[j:j + 6]) / len(aqi_list[j:j + 6])
            ave_list += [ave_num]
            j += 7
        return ave_list


def add(x, y):
    return x + y
