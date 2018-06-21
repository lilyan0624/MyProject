# -*- coding: utf-8 -*-
import sys
import csv
import glob
import os

"""
Created on Fri May 18 15:02:09 2018

@author: Administrator
"""

# =============================================================================
# 2.8 计算每个文件中值的总和与均值
# =============================================================================
#1.基础Python

input_path = sys.argv[1]
output_file = sys.argv[2]

#创建输出文件的列标题列表
output_header_list = ['file_name', 'total_sales', 'average_sales']
#创建文件读取对象（filewriter）
csv_out_file = open(output_file, 'a', newline='')
filewriter = csv.writer(csv_out_file)
#将标题行写入输出文件
filewriter.writerow(output_header_list)

for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    with open(input_file, 'r', newline='') as csv_in_file:
        
        filereader = csv.reader(csv_in_file)        
#       创建一个空列表（output_list），保存要写入输出文件中的每行输出。
        output_list = []
#       将输入文件的文件名作为第一个值追加到output_list中，需对每个输入文件进行计算。
        output_list.append(os.path.basename(input_file))
#       使用next函数除去每个输入文件（filereader）的标题行
        header = next(filereader)
        
        total_sales = 0.0
        number_of_sales = 0.0
        
        for row in filereader:
#           使用列表索引取出销售额这列中的值，并赋给变量sale_amount
            sales_amount = row[3]
            total_sales +=  float(str(sales_amount).strip('$').replace(',', ''))
            number_of_sales += 1
            
        average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
        
#       将总销售额作为第二个值添加到output_list中
        output_list.append(total_sales)
#       将平均销售额作为第三值添加到output_list中
        output_list.append(average_sales)
#       将output_list中的值写入输出文件
        filewriter.writerow(output_list)
        
csv_out_file.close()
        
        
