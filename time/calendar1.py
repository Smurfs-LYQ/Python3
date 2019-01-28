#!/usr/bin/python3

import calendar

# calendar 查询指定年份的日历
# print(calendar.calendar(2018))

# month 获取指定年月的日历
# print(calendar.month(2018,12))

# monthcalendar 获取指定年月的日历 矩阵格式
# print(calendar.monthcalendar(2018,3))

# isleap 检测指定年份是不是闰年
# print(calendar.isleap(2012))

# leapdays 检测指定年份之间的闰年个数
# print(calendar.leapdays(2000,2010))

# monthrange 获取一个月是从周几开始以及当月天数
# print(calendar.monthrange(2018,7))

# weekday 根据年月日计算周几
# print(calendar.weekday(2018,9,14))

# timegm 将时间元组转化为时间戳
tm = (1990,1,1,0,0,0,0,0,0)
print(calendar.timegm(tm))
