# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:47:00 2018

@author: Administrator
"""

# =============================================================================
# 3.2　处理单个工作表
# =============================================================================
#3.2.1　读写Excel文件
#基础Python和xlrd、xlwt模块

#导入xlrd模块的open_workbook函数，xlwt模块的Workbook对象
import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

#实例化一个xlwt Workbook对象，可将结果写入用于"输出"的Excel文件(工作簿)
output_workbook = Workbook()
#使用xlwt的add_sheet函数为"输出"工作簿添加一个名为jan_2013_output的工作表
output_worksheet = output_workbook.add_sheet('jan_2013_output')

#使用xlrd的open_workbook函数打开用于"输入"的工作簿，并将结果赋给一个workbook对象
with open_workbook(input_file) as workbook:
    
#    使用这个workbook对象的sheet_by_name函数引用名称为january_2013的工作表
    worksheet = workbook.sheet_by_name('january_2013')
    
#    创建行与列索引值上的for循环语句，使用range函数和worksheet对象的nrows属性和
#    ncols属性，在工作表的每行和每列之间迭代。
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            
#            使用xlwt的write函数和行与列的索引将每个单元格的值写入输出文件的工作表。
            output_worksheet.write(row_index, column_index, \
                                   worksheet.cell_value(row_index, column_index))

#保存并关闭输出工作簿           
output_workbook.save(output_file)
    
