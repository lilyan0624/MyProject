# -*- coding: utf-8 -*-
import sys
import pandas as pd

"""
Created on Wed May  9 10:53:35 2018

@author: Administrator
"""
#使用pandas的read_csv和to_csv函数进行读取和写入
#使用pandas的loc函数选择特定的行与列
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

data_frame_values_meet_condition = data_frame.loc[(data_frame['Supplier Name']\
.str.contains('Z')) | (data_frame['Cost'] > 600.0), :]

data_frame_values_meet_condition.to_csv(output_file, index=False)