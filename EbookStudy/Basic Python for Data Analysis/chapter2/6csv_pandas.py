# -*- coding: utf-8 -*-
import sys
import pandas as pd

"""
Created on Wed May 16 14:54:29 2018

@author: Administrator
"""

# =============================================================================
# 2.3 选取特定的列
#     1.使用列索引值
#     2.使用列标题
# =============================================================================

#2.3.1 列索引值
#当你想保留的列的索引值非常容易识别
#或者在处理多个输入文件时，各个输入文件中列的位置一致（也就是不会发生改变）

#2. pandas

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

#使用iloc函数来根据索引位置选取列
data_frame_column_by_index = data_frame.iloc[:, [1, 3, -1]]

data_frame_column_by_index.to_csv(output_file, index=False)