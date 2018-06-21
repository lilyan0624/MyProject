# -*- coding: utf-8 -*-
import sys
import csv

"""
Created on Wed May  9 09:06:56 2018

@author: Administrator
"""

# =============================================================================
# 2.1.3 读写CSV文件
# 如将成本数量改为$6,015.00：
# 使用基础python会错误地将数据内部的逗号当做分隔符处理，拆成2个元素
# 使用Python内置的csv模块能自动处理嵌入数据的逗号问题，正确地将每一行拆分成了5个值。
# =============================================================================

#基础python，使用CSV模块

#delimiter默认是','，可以省略。此处为提示，则加上了。

#1.定义两个变量（input_file和output_file）来保存屏幕输入的文件路径和文件名
input_file = sys.argv[1]
output_file = sys.argv[2]

#2.将这两个变量打开为“文件对象”（csv_in_file和csv_out_file）
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        
#3.使用csv模块的reader函数创建一个“文件读取对象”(filereader)，使用该对象读取输入文件中的行。
#4.使用csv模块的writer函数创建一个“文件写入对象”(filewriter),使用该对象将数据写入输出文件。
#第二个参数（delimiter=','）是默认分隔符。
#如果输入文件和输出文件都是用逗号分隔的，可省略。如是‘\t’或' '等就不可省略了。
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')
        
#使用“文件写入对象”（filewriter）的writerow函数来写入输出文件
        for row_list in filereader:
            print(row_list)
            filewriter.writerow(row_list)