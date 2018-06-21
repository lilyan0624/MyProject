# -*- coding: utf-8 -*-
"""
Created on Wed May 23 09:57:14 2018

@author: Administrator
"""

# =============================================================================
# 3.1内省Excel工作簿
# 在实际开始处理工作簿中的数据之前，检查工作表的数目和每个工作表中的数据类型和数据量
# 有助于确定文件中的数据确实是你需要的，并对数据一致性和完整性做一个初步检查
# =============================================================================

import sys
from xlrd import open_workbook

input_file = sys.argv[1]

#使用xlrd的open_workbook函数打开excel文件，赋值给对象workbook
#workbook对象中包含工作簿中所有可用信息，能使用该对象从工作簿中得到单独的工作表
workbook = open_workbook(input_file)

#使用workbook对象的nsheets属性，打印所有工作表的数量
print('Number of worksheets:', workbook.nsheets)

#workbook对象的sheets方法可以识别出工作簿中所有的工作表
for worksheet in workbook.sheets():
    
#    使用worksheet对象的name属性来确定每个工作表的名称。
#    使用worksheet对象nrows和ncols属性来分别确定每个工作表中行与列的数量。
    print("Worksheet name: ", worksheet.name, \
          "\tRows: ", worksheet.nrows, \
          "\tColumns: ", worksheet.ncols)