#!/usr/bin/python3

import zipfile

# 压缩文件
'''
# 打开新建压缩文件
zip = zipfile.ZipFile('../func.zip','a')

# 将文件或文件夹添加到压缩文件当中
zp.write('../func/zidian.py','zip_zidian.py')
zp.write('../func/list.py','dir/zip_list.py') #这里可以写路径

# 关闭压缩文件
zip.close()
'''

# 解压操作
'''
# 打开压缩文件
zip = zipfile.ZipFile('../func.zip','r')

# 解压整个压缩文件
zip.extractall('../one')
# 解压压缩文件中的单个文件
zip.extract('func/zidian.py','../one')

# 关闭压缩文件
zip.close()
'''

# 查看压缩文件信息
zip = zipfile.ZipFile('../func.zip','a')

# getinfo 查看压缩包中某个文件的信息
# print(zip.getinfo('func/zidian.py'))

# infolist 获取所有文件的信息
# print(zip.infolist())

# namelist 获取名称列表
print(zip.namelist())

zip.close()
