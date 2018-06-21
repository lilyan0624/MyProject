# -*- coding: utf-8 -*-
import sys
import glob
import os
import pandas as pd

"""
Created on Fri May 18 15:01:37 2018

@author: Administrator
"""

# =============================================================================
# 从多个文件中连接数据
# =============================================================================
#1.Pandas:可直接从多个文件中连接数据。

#基本过程:
#1.将每个输入文件读取到pandas数据框中，将所有"数据框"追加到一个"数据框列表".
#2.使用concat函数将所有数据框连接成一个数据框,使用axis参数设置连接数据框的方式
#axis=0表示从头到尾垂直堆叠，axis=1表示并排地平行堆叠.
input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frames = []

for file in all_files:
    data_frame = pd.read_csv(file, index_col=None)
    all_data_frames.append(data_frame)

data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index=False)