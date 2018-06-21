# -*- coding: utf-8 -*-
import sys
import pandas as pd

"""
Created on Thu May 17 09:49:36 2018

@author: Administrator
"""

input_file = sys.argv[1]
output_file = sys.argv[2]

#read_csv函数，第二个参数（header=None）如果不去掉则第一行标记为列序号
data_frame = pd.read_csv(input_file, header=None)

#使用drop函数丢弃前三行和最后三行
data_frame = data_frame.drop([0,1,2,16,17,18])

#使用iloc函数根据行索引选取一个单独行作为数据框的列索引
data_frame.columns = data_frame.iloc[0]

#使用reindex函数为数据框重新生成索引
data_frame = data_frame.reindex(data_frame.index.drop(1))

data_frame.to_csv(output_file, index=False)

