# -*- coding: utf-8 -*-
import sys
import pandas as pd

"""
Created on Wed May  9 14:20:02 2018

@author: Administrator
"""

input_file = sys.argv[1]
output_file = sys.argv[2]

important_dates = ['1/20/14','1/30/14']
data_frame = pd.read_csv(input_file)

data_frame_values_in_set = data_frame.loc[data_frame['Purchase Date']\
                                          .isin(important_dates), :]

data_frame_values_in_set.to_csv(output_file, index=False)