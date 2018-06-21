# -*- coding: utf-8 -*-
import sys
import pandas as pd

"""
Created on Wed May 16 18:26:34 2018

@author: Administrator
"""

# =============================================================================
# 2.3 选取特定的列
#     1.使用列索引值
#     2.使用列标题
# =============================================================================

#2.3.2 列标题
#当你想保留的列的标题非常容易识别
#或者在处理多个输入文件时，各个输入文件中列的位置会发生改变，但标题不变

#2. pandas
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_column_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]
data_frame_column_by_name.to_csv(output_file, index=False)

