# -*- coding: utf-8 -*-
import sys
import csv
"""
Created on Wed May  9 18:49:11 2018

@author: Administrator
"""

# =============================================================================
# 2.3 选取特定的列
#     1.使用列索引值
#     2.使用列标题
# =============================================================================

#2.3.1 列索引值
#当你想保留的列的索引值非常容易识别
#或者在处理多个输入文件时，各个输入文件中列的位置一致（也就是不会发生改变）

#1. 基础python

input_file = sys.argv[1]
output_file = sys.argv[2]

#需创建一个变量保存索引值，如有修改，则只需要改此变量即可
my_columns = [1,3,-1]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        
#       对文本读取对象filereader所有行都进行迭代（以下所有缩进的语句）
        for row_list in filereader:
            
#           创建一个空列表变量（row_list_output），保存每一行中要保留的值
            row_list_output = []
            
#            在my_columns中的各个索引值进行迭代（仅包含以下一条语句）
            for index_value in my_columns:
                
#                使用append函数将索引值位置的值作为列表（row_list_output）的追加元素
                row_list_output.append(row_list[index_value])
#            在文本写入对象filewriter中，写入index_value迭代后的row_list_output值
#            因为row_list_output在外循环中定义，故外循环每次迭代后用writerow函数写入
            filewriter.writerow(row_list_output)