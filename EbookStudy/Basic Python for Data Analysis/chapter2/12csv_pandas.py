# -*- coding: utf-8 -*-
import sys
import pandas as pd

"""
Created on Fri May 18 14:00:57 2018

@author: Administrator
"""

# =============================================================================
# 添加标题行
# =============================================================================
#2.pandas

input_file = sys.argv[1]
output_file = sys.argv[2]

header_list = ['Supplier Name', 'Invoice Number', 'Part Number', \
               'Cost', 'Purchase Date']

#参数1：header=None，如无此参数则第一行是0,1,2,3...首行，如有此参数则首行不显示
#参数2：names=header_list，读取文件时，将header_list列表作为标题行读取
data_frame = pd.read_csv(input_file, header=None, names=header_list)

#参数：index=False，如无此参数则第一列是0,1,2,3...首列，如有此参数则首列不显示
data_frame.to_csv(output_file, index=False)

