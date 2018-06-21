# -*- coding: utf-8 -*-
import sys
import csv
import glob
import os

"""
Created on Fri May 18 15:00:41 2018

@author: Administrator
"""

# =============================================================================
# 2.7 从多个文件中连接数据
# =============================================================================
#1.基础Python
#多个文件连接时，屏幕输入的是path而非file
input_path = sys.argv[1]
output_file = sys.argv[2]

#判断是否第一个文件
#如是：则处理if语句连标题行一起写入；如不是：则处理else跳过标题行
first_file = True

for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'a', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else:
                header = next(filereader, None)
                for row in filereader:
                    filewriter.writerow(row)