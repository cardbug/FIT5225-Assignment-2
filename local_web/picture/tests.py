# from django.test import TestCase
# # 一、准备一个带有重复数据的列表
# list_1 = [1,2,3,1,5,6,2]
#
# # 二、使用 set() 方法进行去重处理
# #【注：仅用 set() 方法处理后的数据类型并不是 list 】
# result = set(list_1)
# print("仅用 set() 方法处理后的数据及数据类型：",list(result),type(result))
s=",".join(["car", "traffic light", "person", "person", "car", "car", "person"])
print(s)