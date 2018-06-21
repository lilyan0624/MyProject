# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:06:06 2018

@author: Administrator
"""

# =============================================================================
# 3.2　处理单个工作表
# =============================================================================
#3.2.1　读写Excel文件
#格式化日期数据

# =============================================================================
# 1.函数xldate_as_tuple可以将Excel中代表日期、时间或日期时间的数值转换为元组。
# 只要将数值转换成了元组，就可以提取出具体时间元素（例如：年、月、日）
# 并将时间元素格式化成不同的时间格式（例如：1/1/2010或January 1, 2010）。
# 2.从datetime模块导入date函数，以使我们可以将数值转换成日期并对日期进行格式化。
# =============================================================================
import sys
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for col_index in range(worksheet.ncols):
            
#            创建if-else语句检验每个单元格类型，如为‘3’表示该单元格中包含日期数据。
            if worksheet.cell_type(row_index, col_index) == 3:                
# =============================================================================
# 1. 使用worksheet对象的cell_value函数和行列索引来引用单元格中的值，
# 作为xldate_as_tuple函数中的第一个参数，会被转换成元组中的一个代表日期的浮点数。
# 2. 第二个参数workbook.datemode是必需的，它可使函数确定日期是基于1900年还是1904年，
# 并据此将数值转换成正确的元组（在Mac上的某些Excel版本从1904年1月1日开始计算日期。）
# 3. xldate_as_tuple函数的结果被赋给一个"元组变量"date_cell。
# =============================================================================
                date_cell = xldate_as_tuple(worksheet.cell_value\
                            (row_index, col_index), workbook.datemode)
#                print(date_cell)
#print output:
#(2013, 1, 1, 0, 0, 0)
#(2013, 1, 6, 0, 0, 0)
#(2013, 1, 11, 0, 0, 0)
#(2013, 1, 18, 0, 0, 0)
#(2013, 1, 24, 0, 0, 0)
#(2013, 1, 31, 0, 0, 0)
                
# =============================================================================
# 1. 使用元组索引来引用元组date_cell中的前3个元素（也就是年、月、日）
# 并将它们作为参数传给date函数，该函数可以将这些值转换成一个date对象，
# 2. strftime函数将date对象转换为一个具有特定格式的字符串。
# 格式'%m/%d/%Y'表示像2014年3月15日这样的日期应该显示为03/15/2014。
# 3. 格式化后的日期字符串被重新赋给"元组变量"date_cell。
# =============================================================================
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
#                print(date_cell)
#rpint output:
#01/01/2013
#01/06/2013
#01/11/2013
#01/18/2013
#01/24/2013
#01/31/2013                     
#                使用列表的append函数将date_cell中的值追加给输出列表row_list_output
                row_list_output.append(date_cell)
                output_worksheet.write(row_index, col_index, date_cell)
            else:
#                使用worksheet对象的cell_value函数和行列索引引用单元格中的值，
#                并将其赋给变量non_date_cell
                non_date_cell = worksheet.cell_value(row_index, col_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index, col_index, non_date_cell)
output_workbook.save(output_file)


















