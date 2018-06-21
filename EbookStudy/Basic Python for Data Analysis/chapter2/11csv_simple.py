# -*- coding: utf-8 -*-
import sys
import csv

"""
Created on Thu May 17 09:26:12 2018

@author: Administrator
"""

# =============================================================================
# 2.4 选取连续的行
# =============================================================================
#1. 基础Python
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        
        row_counter = 0
        for row in filereader:
            if row_counter >= 3 and row_counter <= 15:
                filewriter.writerow(value.strip() for value in row)
            row_counter += 1













