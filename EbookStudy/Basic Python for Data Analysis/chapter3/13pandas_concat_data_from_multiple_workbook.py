# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:55:35 2018

@author: Administrator
"""

# =============================================================================
# 3.5　处理多个工作簿
# =============================================================================
#3.5.2　从多个工作簿中连接数据
#pandas

import sys
import pandas as pd
import glob
import os

input_path = sys.argv[1]
output_file = sys.argv[2]

all_workbooks = glob.glob(os.path.join(input_path, '*.xlsx'))
data_frames = []

for workbook in all_workbooks:
    worksheet = pd.read_excel(workbook, sheetname='SIT更新已超期', \
                                   index_col=None)
    for data in worksheet.items():
        data_frames.append(data)
    all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)
    writer = pd.ExcelWriter(output_file)
    all_data_concatenated.to_excel(writer, sheet_name='本周SIT更新超期明细', \
                                   index=False)
    writer.save()
    