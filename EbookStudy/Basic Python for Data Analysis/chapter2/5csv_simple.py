# -*- coding: utf-8 -*-
import sys
import csv
import re

"""
Created on Wed May  9 15:05:39 2018

@author: Administrator
"""

# =============================================================================
# 2.2 筛选特定的行
# for row in filereader:
#     if value in row meets some business rule orset of rules:
#         do something
#     else:
#         do something else
# =============================================================================

#2.2.3 行中的值匹配于某个模式/正则表达式
#任务要求：保留发票编号由“001-”开头的行，并将结果写入一个输出文件

#1. 基础Python
input_file = sys.argv[1]
output_file = sys.argv[2]

#r'' 表示将单引号之间的模式当做原始字符串来处理（不处理字符串中的转义字符，如\n，\t等）
#（元字符）?P<name> 捕获了名为<name>的组中匹配了的子字符串
#^ 表示只在字符串开头搜索的模式
#. 表示可以匹配任何字符（除了换行符）
#* 表示重复前面的字符0次或多次
#.* 组合使用表示在‘001-’后可以包含任意值（除了换行符）
pattern = re.compile(r'(?P<pattern_1>^001-.*)', re.I)

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader:
            invoice_number = row_list[1]
            if pattern.search(invoice_number):
                filewriter.writerow(row_list)
        