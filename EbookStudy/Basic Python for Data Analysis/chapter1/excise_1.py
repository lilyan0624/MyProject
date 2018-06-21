# -*- coding: utf-8 -*-
import sys
"""
Created on Tue May  8 10:26:22 2018

@author: Administrator
"""
# =============================================================================
# 练习1：创建一个新的Python脚本，在它里面创建3个不同的列表，将这3个列表相加，并使
# 用for循环和定位索引（也就是range(len())）在列表中循环，在屏幕上打印出列表的
# 索引值和元素值
# =============================================================================
new_list1 = ['1','2','3']
new_list2 = ['a','b','c']
new_list3 = ['my','name','is','lily']
long_list = new_list1 + new_list2 + new_list3
for index in range(len(long_list)):
    print("output #1: long list is: {0}:{1}".format(index, long_list[index]))

          
# =============================================================================
# 练习2：创建一个新的Python脚本，在它里面创建两个同样长度的不同列表，其中一个列表包
# 含具有唯一性的字符串。再创建一个空字典。使用for循环、定位索引和if语句检查
# 字符串列表中的每个元素是否是字典中的键。如果不是，将这个元素作为字典键，将另
# 一个列表中具有同样索引位置的元素作为字典值，把它们添加到字典中。最后在屏幕上
# 打印出字典的键和值。
# =============================================================================
#解题思路：
#1.将new_list_1的元素逐一判断是否为字典new_dict_1中的键。
#2.如不是字典键，将该元素作为键、new_list_2同样索引位元素作为值，添加到new_dict_1。

new_list_1 = ['abc','def','abc','ghi']
new_list_2 = ['123','456','123','789']
new_dict_1 = {}

#用for循环和定位索引来遍历new_list_1中的元素，new_list_1[index]
#用set函数来选出new_dict_1中的字典键，if not in则继续添加到字典中
for index in range(len(new_list_1)):
    if new_list_1[index] not in set(new_dict_1):
        new_dict_1[new_list_1[index]] = new_list_2[index]

print("output #2: keys and values of new_dict_1 are:")
for key, value in new_dict_1.items():
    print("{0}:{1}".format(key, value))



# =============================================================================
# 练习3：创建一个新的Python脚本，在它里面创建一个列表，其中的元素是具有相同长度的列
# 表。修改1.7.2节中的代码，在列表的列表中循环，将每个列表中的值以逗号隔开的字
# 符串形式打印在屏幕上，并在每个列表的最后一个值后面加上一个换行符。        
# =============================================================================
#解题思路：
#1.遍历得到another_new_list中4个元素中的列表里的值
#2.判断每个列表的最后一个值的位置
    
#直接打印在屏幕上
another_new_list = [['abc','def'],[123,456],['abc',123],['def',456]]
print("output #3: ")
for i in range(len(another_new_list)):
        for j in range(len(another_new_list[i])):
            if j < (len(another_new_list[i])-1):
                print(format(another_new_list[i][j]) + ',')
            else:
                print(format(another_new_list[i][j]) + '\n')


#写入到新建文件: 在cmd输入python excise_1.py new_file.txt
another_new_list = [['abc','def'],[123,456],['abc',123],['def',456]]
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
print("output #3: ")
for i in range(len(another_new_list)):
        for j in range(len(another_new_list[i])):
            if j < (len(another_new_list[i])-1):
                filewriter.write(str(another_new_list[i][j]) + ',')
            else:
                filewriter.write(str(another_new_list[i][j]) + '\n')
filewriter.close()
print("output has written to file.")

















