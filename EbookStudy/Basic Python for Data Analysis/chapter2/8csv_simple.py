# -*- coding: utf-8 -*-
import sys
import csv
import glob
import os

"""
Created on Fri May 18 14:56:34 2018

@author: Administrator
"""

# =============================================================================
# 2.6 读取多个CSV文件
# glob模块可以定位匹配于某个特定模式的所有路径名。模式中可以包含Unixshell风格的通配符
# os模块包含了用于解析路径名的函数,返回path的基本文件名,即:
# 如path是C:\Users\my_input_file.csv，则os.path.basename(path)返回my_input_file.csv
# =============================================================================
#文件计数与文件中的行列计数

input_path = sys.argv[1]
file_counter = 0

#1. os模块中的os.path.join()函数将函数圆括号中的两部分连接在一起。
#input_path是包含输入文件的文件夹的“路径”，'sales_*'代表任何以'sales_'开头的“文件名”。
#2. glob模块中的glob.glob()函数将'sales_*'中的星号（*）转换为实际的文件名。
#在这个示例中，glob.glob()函数和os.path.join()函数创建了一个包含3个输入文件的列表
#['C:\Users\Clinton\Desktop\sales_january_2014.csv',
#'C:\Users\Clinton\Desktop\sales_february_2014.csv',
#'C:\Users\Clinton\Desktop\sales_march_2014.csv']
#3. for循环语句对于列表中3个输入文件执行下面缩进的各行代码
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    
    row_counter = 0
    
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader, None)
#        第二层for循环从header的下一行开始迭代，故第一层for循环中先定义row_counter=1
#        故第二层for循环第一次结束时为2，即第2行
        for row in filereader:
            row_counter += 1
    print('{0!s}: \t{1:d} rows \t{2:d} columns.'.format(\
          os.path.basename(input_file), row_counter, len(header)))
    
#    每结束一次外循环，file_counter自动加1，故共有3个文件
    file_counter += 1
    
print('Number of files: {0:d}'.format(file_counter))
        