# -*- coding: utf-8 -*-
"""
Created on Wed May 23 18:14:10 2018

@author: Administrator
"""

# =============================================================================
# 自动将本周内SIT和UAT超期的记录整合成一份excel
# 更新记录
# 20180620：
# =============================================================================

import sys
import pandas as pd
import glob
import os,xlrd,xlwt

input_path = sys.argv[1]
output_file = sys.argv[2]

def input1 = pd.read_excel(input_path)












































#input_path = sys.argv[1]
#output_file = sys.argv[2]


#def read_excel(all_workbooks):
#    for workbook in all_workbooks:
#        workbook_tmp=xlrd.open_workbook(workbook)
#        #print(workbook_tmp)
#        print(workbook_tmp.sheet_names())
#        sheet_n=workbook_tmp.sheet_by_index(2)
#        print(sheet_n)
#        print(sheet_n.row_values(0))
#    return sheet_n.row_values(0)
#def write_excel(row_names):
#    f=xlwt.Workbook()
#    sheet1=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
#    row0=row_names
#    for i in range(len(row0)):
#        sheet1.write(0,i,row0[i])
#    f.save('test.xls