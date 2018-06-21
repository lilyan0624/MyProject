# -*- coding: utf-8 -*-
import sys
import csv

"""
Created on Fri May 18 14:00:41 2018

@author: Administrator
"""

# =============================================================================
# 添加标题行
# =============================================================================
#2.基础Python
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        
        header_list = ['Supplier Name', 'Invoice Number', 'Part Number',\
                       'Cost', 'Purchase Date']
        filewriter.writerow(header_list)

#       writerow函数是追加写入，不会覆盖上面的标题行        
        for row in filereader:
            filewriter.writerow(row)
