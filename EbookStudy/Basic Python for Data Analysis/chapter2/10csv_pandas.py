# -*- coding: utf-8 -*-
import sys
import glob
import os
import pandas as pd

"""
Created on Fri May 18 15:02:52 2018

@author: Administrator
"""

# =============================================================================
# 2.8 计算每个文件中值的总和与均值
# =============================================================================
#2. pandas

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []

for input_file in all_files:
    data_frame = pd.read_csv(input_file, index_col=None)
    
#    使用列表生成式将销售额这一列中带美元符号的字符串转换为浮点数，然后使用"数据框函数"
#    将这个对象转换为一个"DataFrame"，以便可以使用这两个函数计算列的总计和均值
    total_cost = pd.DataFrame([float(str(value).strip('$').replace(',', ''))\
                 for value in data_frame.loc[:, 'Sale Amount']]).sum()
    
    average_cost = pd.DataFrame([float(str(value).strip('$').replace(',', ''))\
                 for value in data_frame.loc[:, 'Sale Amount']]).mean()
    
#    将文件名、文件中销售额的总计和均值 这3种数据组合成一个文本框（字典）
    data = {'file_name':os.path.basename(input_file), \
            'total_sales':total_cost, \
            'average_sales':average_cost}
    
#    往空的列表中追加数据框，每个元素是一个数据框
    all_data_frames.append(pd.DataFrame(data, \
    columns=['file_name', 'total_sales', 'average_sales']))
    
#使用concat函数将这些数据框连接成为一个数据框，然后将这个数据框写入输出文件。
data_frames_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frames_concat.to_csv(output_file, index=False)