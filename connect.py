#!/usr/bin/env python
# coding=utf-8

import MySQLdb

# 建立和mysql数据库的连接
conn = MySQLdb.connect(host='localhost', user='root', passwd='root')

# 获取游标
curs = conn.cursor()

# 执行SQL,创建一个数据库
curs.execute("CREATE DATABASE aqi")

# 选择连接哪个数据库
conn.select_db('aqi')

# 执行SQL,创建一个表
curs.execute("CREATE TABLE `aqi_data` (`id` int(11) NOT NULL,`city` int(11) NOT NULL,`datetime` date NOT NULL,`num` int(11) NOT NULL,`rank` int(11) NOT NULL,`pollutant` int(11) NOT NULL)")

# 插入一条记录
value = [1, "武汉市", "2015-12-31", 159, 4, 1]
curs.execute("INSERT INTO `aqi_data` VALUES (%s,%s,%s,%s,%s,%s)", value)

# # 插入多条记录
# values = []
# for i in range(20):
#     values.append((i, 'hello mysqldb' + str(i)))
# curs.executemany("insert into test values(%s,%s)", values)

# 提交修改
conn.commit()

# 关闭游标连接,释放资源
curs.close()

# 关闭连接
conn.close()
