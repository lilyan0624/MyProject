# -*- coding: utf-8 -*-
import sys
import csv

"""
Created on Wed May 16 15:25:10 2018

@author: Administrator
"""

# =============================================================================
# 2.3 选取特定的列
#     1.使用列索引值
#     2.使用列标题
# =============================================================================

#2.3.2 列标题
#当你想保留的列的标题非常容易识别
#或者在处理多个输入文件时，各个输入文件中列的位置会发生改变，但标题不变

#1. 基础python
input_file = sys.argv[1]
output_file = sys.argv[2]

my_column = ['Invoice Number', 'Purchase Date']
my_column_index = []

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)

#       在文件读取对象filereader上使用next函数将首行保存在列表变量header中
        header = next(filereader, None)
        
#       在列表变量header中迭代识别标题列对应的索引值，保存在列表变量my_column_index
        for index_header in range(len(header)):
            if header[index_header] in my_column:
                my_column_index.append(index_header)
        filewriter.writerow(my_column)
        
#       将文件读取对象filereader中的每一行进行迭代循环
        for row_list in filereader:           
            row_list_output = []
            
#           如row_list在my_column_index中存在，则将值保存在列表变量row_list_output
            for index in my_column_index:
                row_list_output.append(row_list[index])
            filewriter.writerow(row_list_output)
                












