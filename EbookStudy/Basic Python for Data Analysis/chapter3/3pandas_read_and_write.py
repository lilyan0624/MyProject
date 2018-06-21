# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:23:15 2018

@author: Administrator
"""

# =============================================================================
# 3.2　处理单个工作表
# =============================================================================
#3.2.1　读写Excel文件
#pandas

import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013')

writer = pd.ExcelWriter(output_file)

data_frame.to_excel(writer, sheet_name='jan_13_output', index=False)

writer.save()