# -*- coding: utf-8 -*-
import sys
import csv

"""
Created on Wed May  9 11:25:13 2018

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

#2.2.2 行中的值属于某个集合
#1. 基础Python
input_file = sys.argv[1]
output_file = sys.argv[2]

important_dates = ['1/20/14','1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            a_date =row_list[4]
            if a_date in important_dates:
                filewriter.writerow(row_list)
        