# -*- coding: utf-8 -*-
import sys
import pandas as pd

"""
Created on Wed May  9 16:27:08 2018

@author: Administrator
"""

# =============================================================================
# 2.2 筛选特定的行
# for row in filereader:
#     if value in row meets some business rule orset of rules:
#         do something
#     else:
#         do something else
# =============================================================================

#2.2.3 行中的值匹配于某个模式/正则表达式
#任务要求：保留发票编号由“001-”开头的行，并将结果写入一个输出文件

#2. pandas
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame_match_pattern = data_frame.loc[data_frame['Invoice Number']\
                                          .str.startswith('001-'), :]

data_frame_match_pattern.to_csv(output_file, index=True)