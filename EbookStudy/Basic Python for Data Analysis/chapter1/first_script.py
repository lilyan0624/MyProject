#!/usr/bin/env python3
from math import exp,log,sqrt
import re
from datetime import date,time,datetime,timedelta
from operator import itemgetter
import numpy as np
import sys
import glob
import os
#shebang行：windwows忽略这行，但macOS基于Unix，会使用这行找到执行文件中代码的python版本。
# -*- coding: utf-8 -*-
# =============================================================================
# Ctrl+1：注释/撤销注释
# Ctrl+4/5：块注释/撤销块注释
# Ctrl+Alt+↓/↑ 复制一行
# Ctrl+D 删除一行
# Shift+Ctrl+Alt+← 转到上一编辑位置
# Shift+Ctrl+Enter：不缩进回车
# Tab/Shift+Table:代码缩进/撤销代码缩进
# Ctrl+L：跳转到行号
# Ctrl+G 查找函数定义
# Shift+ Ctrl+C 光标转到Console
# (Shift+)Ctrl+Tab 转到上/下一文件
# F5：运行
# F11：全屏
# F12 设置breakpoint
# =============================================================================
"""
Created on Sat Apr 21 09:01:25 2018

@author: lily
"""

print ("output #1： I'm exited to learn python")

#2两位数相加
x = 4
y = 5
z = x + y
#语法说明：{}为占位符，0为format函数传入的第一个参数，：为分割传入值和格式，d为格式化为整数
print("output #2: Four plus five equals {0:d}.".format(z))

#3两个列表相加
a = [1,2,3,4]
b = ["first","second","third","fourth"]
c = a + b
#语法说明：{0}无需指定格式化d因为是列表，分别将format函数中的变量a，b，c传入{0},{1},{2}
print("output #3: {0},{1},{2}".format(a,b,c))
      
# =============================================================================
# 1.数值
# =============================================================================
#整数     
x = 9    
print("output #4: {0}".format(x))
print("output #5: {0}".format(3**4))
print("output #6: {0}".format(int(8)/int(2.7)))
      
#浮点数
print("output #7: {0:.3f}".format(8.3/2.7))
y = 2.5*4.8
print("output #8: {0:.1f}".format(y))
r = 8/float(3)
print("output #9: {0:.2f}".format(r))
print("output #10 {0:.4f}".format(8.0/3))

#巧用type()函数进行类型判断帮助错误诊断
type(3.5)

#需要加入from math import exp,log,sqrt
print("output #11: {0:.2f}".format(exp(3)))
print("output #12: {0:.3f}".format(log(4)))
print("output #13: {0:.1f}".format(sqrt(81)))

# =============================================================================
# 2.字符串
# =============================================================================
#区分这4种引号的使用效果：‘ ’，“ ”,''' ''',""" """
print("output #14: {0:s}".format('I\'m enjoying learning english.\
      只有单引号里有单引号i\'m，需要使用反斜杠\
      虽在行尾加反斜杠可将字符串分成多行\
      但仍作为一行长文本打印到屏幕上'))

print("output #15: {0:s}".format("I\'m enjoying learning english.\
      虽在行尾加反斜杠可将字符串分成多行\
      但仍作为一行长文本打印到屏幕上"))

print("output #16: {0:s}".format('''I'm enjoying learning english.
      三个单引号不用在行尾增加反斜杠。
      也能创建多行字符串，
      且打印到屏幕上也是分行的。'''))

print("output #17: {0:s}".format("""I'm enjoying learning english.
      三个双引号不用在行尾增加反斜杠。
      也能创建多行字符串，
      且打印到屏幕上也是分行的。"""))

#字符串常用操作符：+，*，len
str1 = "She is a "
str2 = "very "
str3 = "beautiful girl"
sentence1 = str1 + str2 + str3
sentence2 = str1 + str2 * 3 + str3
length1 = len(sentence1)
length2 = len(sentence2)
print("output #19: {0:s}, the length is {1:d}.".format(sentence1,length1))
print("output #20: {0:s}, the length is {1:d}.".format(sentence2,length2))

#字符串常用标准库模块:split
str1 = "My deliverable is due in May"
str1_list1 = str1.split()
str1_list2 = str1.split(" ",2)
print("output #21: {0}".format(str1_list1))
print("output #22: FIRST PIECE:{0}, SECOND PIECE:{1}, THIRD PIECE:{2}"\
      .format(str1_list2[0],str1_list2[1],str1_list2[2]))
str2 = "Your,deliverable,is,due,in,June"
str2_list = str2.split(",")
print("output #23: {0}".format(str2_list))
print("output #24: {0} {1} {2}".format(str2_list[1],str2_list[5],str2[-1]))

#字符串常用标准库模块:join
print("output #25: {0}".format(",".join(str2_list)))
print("output #25: {0}".format(" ".join(str2_list)))

#字符串常用标准库模块:lstrip(左侧),rstirp(右侧),strip(两端),strip("待删除字符")
str3= " Remove unwanted characters    from this string.\t\t    \n"
print("output #26: string3: {0:s}".format(str3))
str3_lstrip = str3.lstrip()
print("output #27: lstrip: {0:s}".format(str3_lstrip))
str3_rstrip = str3.rstrip()
print("output #28: rstrip: {0:s}".format(str3_rstrip))
str3_strip = str3.strip()
print("output #29: strip: {0:s}".format(str3_strip))

str4 = "$$Here's another string that has unwanted characters.__---++"
print("output #30: {0:s}".format(str4))
str4 = "$$The unwanted characters have been removed.__---++"
str4_strip = str4.strip("$_-+")
print("output #31: {0:s}".format(str4_strip))

#字符串常用标准库模块:replace
str5 = "Let's replace the spaces in this sentence with other characters"
str5_replace = str5.replace(" ","!@!")
print("output #32: {0:s}".format(str5))
print("output #33: {0:s}".format(str5_replace))
str5_replace = str5_replace.replace("!@!",",")
print("output #34: {0:s}".format(str5_replace))

#字符串常用标准库模块：lower()，upper()，capitalize()
str6 = "Here's WHAT Happens WHEN You Use different type"
print("output #35: LOWER: {0:s}".format(str6.lower()))
print("output #36: UPPER: {0:s}".format(str6.upper()))
print("output #37-1: CAPITALIZE: {0:s}".format(str6.capitalize()))

str6_list = str6.split()
for word in str6_list:
    print("output #37-2: {0:s}".format(word.capitalize()))

# =============================================================================
# 3.正则表达式与模式匹配
#   需要import re
# =============================================================================

#r: 原始字符串（不处理字符串中的转义字符，如\n，\t等）
#re.I: 不区分大小写
#re.compile函数：建立正则表达式的匹配条件
#search函数：使用已建立的匹配条件进行搜索
str7 = "The quick brown fox jumps over the lazy dog."
str7_list = str7.split()
pattern1 = re.compile(r"The",re.I)
pattern2 = re.compile(r"The")
count1 = 0
count2 = 0

for word in str7_list:
    if pattern1.search(word):
        count1 += 1
print("output #38: {0}".format(count1))     
for word in str7_list:
    if pattern2.search(word):
        count2 += 1
print("output #38: {0}".format(count2))

#?P<name>:出现在re.compile函数中的元字符，后面加要匹配的内容。匹配到的结果可用<name>引用
#group参数中引用<name>
pattern3 = re.compile(r"(?P<match_word>The)",re.I)
for word in str7_list:
    if pattern3.search(word):
        print("output #39: {0:s}".format(pattern3.search(word)\
              .group("match_word")))


#str_to_find：如果正则表达式过长且复杂时，可通过定义变量再传递给compile函数
#sub函数：
str_to_find = r"The"
pattern4 = re.compile(str_to_find,re.I)
print("output #40: {0:s}".format(pattern4.sub("a",str7)))

# =============================================================================
# 4.日期
# from datetime import date,time,datetime,timedelta
# =============================================================================
today = date.today()
print("output #41: today: {0!s}".format(today))
print("output #42: today: {0!s}".format(today.year))
print("output #43: today: {0!s}".format(today.month))
print("output #44: today: {0!s}".format(today.day))
current_time = datetime.today()
print("output #45: today: {0!s}".format(current_time))

one_day = timedelta(days=-1)
yesterday = today + one_day
print("output #46: yesterday: {0!s}".format(yesterday))

#eight_hours.seconds: 3600秒*24小时-3600秒*8小时=57600秒
eight_hours = timedelta(hours=-8)
print("output #47: {0!s} {1!s}".format(eight_hours.days,eight_hours.seconds))

#两个date对象相减，是一个datetime.timedelat对象
#如只需要天数，将该datetime.timedelat对象转换成str类型，用split函数提取列表第一个元素[0]  
date_diff = today - yesterday
print("output #48: {0!s}".format(date_diff))
date_diff_list = str(date_diff).split()
print("output #49: {0!s}".format(date_diff_list[0]))
      
#由日期格式转化为字符串格式的函数:strftime
print("output #50: {:s}".format(today.strftime("%m%d%Y")))
print("output #50: {:s}".format(today.strftime("%b%d,%Y")))
print("output #50: {:s}".format(today.strftime("%Y-%m-%d")))
print("output #50: {:s}".format(today.strftime("%B%d,%Y")))

#由字符串格式转化为日期格式的函数:strptime
date1 = today.strftime("%m/%d/%Y")
date2 = today.strftime("%b%d,%Y")
date3 = today.strftime("%Y-%m-%d")
date4 = today.strftime("%B%d,%Y")
print("output # 54: {!s}".format(datetime.strptime(date1,"%m/%d/%Y")))
print("output # 55: {!s}".format(datetime.strptime(date2,"%b%d,%Y")))
print("output # 56: {!s}".format(datetime.date(datetime.strptime\
      (date3,"%Y-%m-%d"))))
print("output # 57: {!s}".format(datetime.date(datetime.strptime\
      (date4,"%B%d,%Y"))))

# =============================================================================
# 5.列表
# =============================================================================
#使用[]创建列表 max,min,len,count
a_list = [1,2,3]
b_list = ['printer',5,['star','sky',5]]

print("output #58: {}".format(a_list))
print("output #59: a_list has {} elements.".format(len(a_list)))
print("output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("output #61: the minimum value in a_list is {}.".format(min(a_list)))
print("output #62: {}".format(b_list))
print("output #63: b_list has {} elements".format(len(b_list)))
#列表B作为列表A一个元素时，列表B中的元素不纳入列表A的元素count统计，比如5只统计到1次。
print("output #64: 5 is in b_list for {} times".format(b_list.count(5)))

#索引值
#[0]: 第一个元素，[-1]：最后一个元素
print("output #65: {}".format(a_list[0]))
print("output #66: {}".format(b_list[-1]))

#列表切片
#切片引用从第一个索引值到第二个索引值的前一个元素
#切片从列表头开始，第一个索引值可省略；切片到列表末尾，第二个索引值可省略
print("output #67: {}".format(a_list[0:2]))
print("output #68: {}".format(a_list[:2]))
print("output #69: {}".format(b_list[1:]))

#列表复制
a_new_list = a_list[:]
print("output #70: {}".format(a_new_list))

#列表连接
a_long_list = a_list + b_list
print("output #71: {}".format(a_long_list))

#检查列表中是否有特定函数：in、not in
a = 2 in a_list
b = 5 not in b_list
print("output #72: {}".format(a))
print("output #73: {}".format(b))

#追加元素：append()在列表末尾追加一个新元素
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("output #74: {}".format(a_list))
#删除元素：remove()在列表中删除一个特定元素
a_list.remove(5)
print("output #75: {}".format(a_list))
#弹出元素：pop()从列表末尾删除一个元素
a_list.pop()
a_list.pop()
print("output #76: {}".format(a_list))

#列表反转
a_list.reverse()
print("output #77: {}".format(a_list))    
a_list.reverse()
print("output #78: {}".format(a_list))

   
#sort列表排序：改变原列表的排序
unordered_list = [1,3,2,4]
print("output #79: {}".format(unordered_list))
list_copy = unordered_list[:]
list_copy.sort()
print("output #80: {}".format(list_copy))
print("output #81: {}".format(unordered_list))
      
#sorted排序:不改变原列表的排序，注意函数使用方法sorted(),key=lambda?
#lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是匿名函数。
my_lists = [[1,2,3,4],[4,3,2,1],[2,4,1,3]]   
my_lists_sorted_by_index3 = sorted(my_lists,key=lambda index_value:index_value[3])   
print("output #82: {}".format(my_lists_sorted_by_index3))  
print("output #83: {}".format(my_lists))  
      
#itemgetter函数，可使用多个元素先后进行两重排序    
my_lists = [[1,2,3,4,5],[2,3,4,5,1],[4,3,5,1,2],[3,2,5,1,4]]
my_lists_sorted_by_index3_and_0 = sorted(my_lists,key=itemgetter(3,0))
print("output #84: {}".format(my_lists_sorted_by_index3_and_0))
      
      
# =============================================================================
# 6.元组
# 元组除了不能被修改外，其余特点与列表相似，可作为字典键值。
# =============================================================================
#使用圆括号创建元组 
my_tuple = ('x','y','z')     
print("output #85: {}".format(my_tuple))     
print("output #86: my_tuple has {} elements.".format(len(my_tuple)))     
print("output #87: {}".format(my_tuple[1]))     
longer_tuple = my_tuple + my_tuple
print("output #88: {}".format(longer_tuple))         

#元组解包
one,two,three = my_tuple
print("output #89: {0}{1}{2}".format(one,two,three))
var1 = 'red'
var2 = 'robin'
print("output #90: {0} {1}".format(var1,var2))
var1,var2 = var2,var1
print("output #91: {0} {1}".format(var1,var2))
      
#元组转换成列表（及列表转换成元组）
my_tuple = ('x','y','z')
my_list = [1,2,3]
print("output #92: I am a list: {}".format(list(my_tuple))) 
print("output #93: I am a tuple: {}".format(tuple(my_list))) 

# =============================================================================
# 7.字典：
# 字典：在python中，字典本质上是包含各种带有唯一标识符的成对信息的列表。
# 字典键：使用整数、字符串或其他python对象来引用一个字典值，称为字典键。
# 字典没有内置排序，因为索引不仅仅只是数值。而列表是隐式排序，因为索引是连续整数。
# 字典中可以在必要的时候创建新的位置（键），而列表为一个不存在的位置（索引）赋值是非法的。
# 字典没有排序，故搜索或添加新值时响应时间更快（计算机无需重新分配索引值）
# =============================================================================
#1. 使用花括号创建字典、用冒号分隔键-值对
empty_dict = {}
a_dict = {'one':1,'two':2,'three':3}
print("output #94: {}".format(a_dict))
print("output #95: a_dict has {} elements.".format(len(a_dict)))
another_dict = {'x':'printer','y':5,'z':['star','sky',9]}
print("output #96: {}".format(another_dict))
print("output #97: another_dict has {} elements.".format(len(another_dict)))

#2. 使用键来引用字典中的值
print("output #98: {}".format(another_dict['z']))

#3. 复制
new_dict = a_dict.copy()
print("output #99: {}".format(new_dict))

#4. 键keys()、值values()、项目itmes()
print("output #100: {}".format(a_dict.keys()))
print("output #101: {}".format(a_dict.values()))
print("output #102: {}".format(a_dict.items()))

#5.1 检查字典中是否有特定键值：in、not in
if 'y' in another_dict:
    print("output #103: y is a key in another_dict: {}"\
          .format(another_dict.keys()))

if 'c' not in another_dict:
    print("output #104: c is not a key in another_dict: {}"\
          .format(another_dict.keys()))

#5.2 检查字典中是否有特定键值：get函数(参数1,参数2)参数2非必需，不返回None，返回参数2
print("output #105: {!s}".format(a_dict.get('three')))
print("output #106: {!s}".format(a_dict.get('four')))
print("output #107: {!s}".format(a_dict.get('four','Not in a_dict')))

#6. 排序：使用sorted函数
#如不想修改原字典，则先使用copy函数进行复制
print("output #108: {}".format(a_dict.items()))
dict_copy = a_dict.copy()
ordered_dict1 = sorted(dict_copy.items(), key=lambda item:item[0])
print("output #109: order by keys {}".format(ordered_dict1))
ordered_dict2 = sorted(dict_copy.items(), key=lambda item:item[1])
print("output #110: order by values {}".format(ordered_dict2))
ordered_dict3 = sorted(dict_copy.items(), key=lambda x:x[1], reverse=True)
print("output #111: order by values, descending {}".format(ordered_dict3))
ordered_dict4 = sorted(dict_copy.items(), key=lambda x:x[1], reverse=False)
print("output #112: order by values, ascending {}".format(ordered_dict4))

# =============================================================================
# 8.控制流
# =============================================================================
#1. if-else
x = 5
if x > 4 or x != 9:
    print("output #113: x is: {}".format(x))
else:
    print("output #113: x is not greater than 4: {}".format(x))
          
#2. if-elif-else
if x > 6:
    print("output #114: x is greater than 6")
elif x > 4 and x == 5:
    print("output #114: x is: {}".format(x))
else:
    print("output #114: x is not greater than 5")

#3. for variable in sequence
#variable是一个临时占位符，表示序列中的每个值，仅在for循环中有意义
y = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
z = ['Annie','Betty','Clarie','Daphne','Ellie','Franchesca','Greta',\
     'Holly','Isabel','Jenny']

print("output #115: ")
for month in y:
    print("{!s}".format(month))

#使用range和len函数来组合生成一个可在for循环中使用的索引值序列
print("output #116: (index value: name in list)")
for i in range(len(z)):
    print("{0!s}:{1:s}".format(i,z[i]))
 
#使用一个序列生成的索引值来引用另一个序列中具有同样索引值的元素，在这里j：0-9
print("output #117: (access elements in y with z's index values)")
for j in range(len(z)):
    if y[j].startswith('J'):
        print("{!s}".format(y[j]))

#字典的键和值之间进行迭代和引用
print("output #118:")
for key, value in another_dict.items():
    print("{0:s},{1}".format(key, value))

#4. 简化for循环（列表、集合与字典生成式）：适用于不太确定内部语句需要执行多少次的情况
#列表生成式:出现在方括号内。使用列表生成特定的行。
my_data = [[1,2,3],[4,5,6],[7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print("output #119: (list comprehension): {}".format(rows_to_keep))

#集合生成式：出现在花括号内
#tuples1使用循环生成集合：在列表中选择出一组唯一的元组。
my_data = [(1,2,3),(4,5,6),(7,8,9),(7,8,9)]
set_of_tuples1 = {x for x in my_data}
print("output #120 : (set comprehension): {}".format(set_of_tuples1))
#tuples2使用内置的set函数生成集合：在列表中选择出一组唯一的元组。
set_of_tuples2 = set(my_data)
print("output #121 : (set comprehension): {}".format(set_of_tuples2))

#字典生成式：出现在花括号内
my_dictionary = {'customer1':7,'customer2':9,'customer3':11}
my_results = {key : value for key, value in my_dictionary.items() if\
              value > 10}
print("output #122: (dictionary comprehension): {}".format(my_results))

#5. while循环:适用于知道内部语句会被执行多少次的情况
print("output #123:")
x = 0
while x < 11:
    print("{!s}".format(x))
    x += 1

#6. 函数
#计算一系列数值的平均值:def自创函数getMean
def getMean(numericValues):
    return sum(numericValues)/len(numericValues) if len(numericValues) > 0\
    else float('nan')
my_list = [2,2,4,4,6,6,8,8]
print("output #124: (mean): {}".format(getMean(my_list)))

#计算一系列数值的平均值:使用Numpy包中的mean函数
my_list = [2,2,4,4,6,6,8,8]
print("output #125: (mean): {}".format(np.mean(my_list)))

#7. 异常处理
def getMean(numericValues):
    return sum(numericValues)/len(numericValues)
my_list2 = []

#try-except
try:
    print("output #126: ".format(getMean(my_list2)))
except ZeroDivisionError as detail:
    print("output #126 (Error): {}".format(float('nan')))
    print("output #126 (Error): {}".format(detail))

#try-except-else-finally
try:
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print("output #127: (Error): {}".format(float('nan')))
    print("output #127: (Error): {}".format(detail))
else:
    print("output #127: (The mean is): ".format(result))
finally:
    print("output #127 (Finally): The Finally block is excuted every time")
      
      
# =============================================================================
# 读取文本文件
# =============================================================================
##1. 读取单个文本文件：imort sys 
##使用sys.argv列表捕获传递给python脚本的命令行参数列表（文件路径名），赋值给变量input_file
#input_file = sys.argv[1]
#print("output #128: ")
##使用open函数只读模式r打开input_file文件中的各行，并赋值给变量filereader
#filereader = open(input_file, 'r', newline='')
#for row in filereader:
#    print(row.strip())
#filereader.close()
#
#input_file = sys.argv[1]
#print("output #129: ")
##使用with语句来创建文件对象,无需使用close函数关闭文件对象
#with open(input_file, 'r', newline='') as filereader:
#    for row in filereader:
#        print("{}".format(row.strip()))
#
#
##2. 读取多个文本文件：import glob；import os
##正确运行以下语句段需先将上面读取单个文件的语句段注释，让argv[1]接受目录的路径名
##os.path.join函数：将文件夹路径和该文件夹中所有符合特定模式（用*.txt匹配）的文件名连接起来
##glob.glob函数：使用glob函数处理目录，将上述函数的特定模式（用*.txt匹配）进行扩展，
#print("output #130: ")
#inputPath = sys.argv[1]
#for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
#    with open(input_file, 'r', newline='') as filereader:
#        for row in filereader:
#            print("{}".format(row.strip()))

      
# =============================================================================
# 写入文本文件    
# =============================================================================
##写入TXT
#my_letters = ['a','b','c','d','e','f','g','h','i','j']
#max_index = len(my_letters)
#output_file = sys.argv[1]
#filewriter = open(output_file, 'w')
#for index_value in range(len(my_letters)):
#    if index_value < (max_index-1):
#        filewriter.write(my_letters[index_value]+'\t')
#    else:
#        filewriter.write(my_letters[index_value]+'\n')
#filewriter.close()
#print("output #131: output written to file")
#
##写入CSV('\t'修改为','，改用'w'改为'a'追加模式)
#my_letters = ['1','2','3','4','5','6','7','8','9','0']
#max_index = len(my_letters)
#output_file = sys.argv[1]
#filewriter = open(output_file, 'a')
#for index_value in range(len(my_letters)):
#    if index_value < (max_index-1):
#        filewriter.write(my_letters[index_value]+',')
#    else:
#        filewriter.write(my_letters[index_value]+'\n')
#filewriter.close()
#print("output #131: output written to file")     


