# 1。对文件的操作，主要的方式

# with open('local',mode='',encoding='utf-8') as file_object:
# 2.函数，def 函数名(name)  defhanshuming ()
# def a(*args,**kwargs):
#     print('l')
# a('l','k')
# # @函数名装饰器
# lambda x:for i in x
# [i for i in range() ]
# 'abf' if x>y else'def'
# from test import base62encode
# base62encode()
# def a ():
#     print('abd')
#     yield 1
#     print('123')
#
# abc=a().send()
# print(abc)
# with open()
#     flush
#

# def a(mane='ll'):
#     b=mane
#     print('l')
# a('ksk')


# def func(x,y):
#     return x+y
# v1=lambda x,y:x+y
# print(v1(1,2))
# ls = [{"id": 1, "name": 'alex', "age": 18},
# {"id": 2, "name": 'wusir', "age": 16},
# {"id": 3, "name": 'taibai', "age": 17}]
#
# a=sorted(ls,key=lambda x:x['age'])
# print(a)
# ls.sort(key=lambda x:x['age'])
#
# map是映射***
# zip是一一对应
# filter--

# def outer(orgini):
#     def inner(*arg,**kwargs):
#         print('a')
#         func=orgini(*arg,**kwargs)
#         print('b')
#         return func
#     return inner
#
# @outer
# a = '123'
# def outer1():
#     a += '5'
# outer1()
# print(a)
# a = [1, 2, 3, 4, 5]
# b = [i if i % 2 != 0 else 0 for i in a ]
# print(b)


# 一个歌唱比赛的歌手打分，我们设计一个程序帮助现场去掉一个最低分和一个最高分，再计算一个平均分。
#
# 范例：
#
#   在程序中定义列表表示分数，values = [8,9,5,10,8,6,8,7,9,9.5]。
#
# 输出：
#
#   最小值的位置是 2 , 最小值是 5
#
#   最大值的位置是 3 , 最大值是 10
#
# 平均分是8.3125,有效评分有8个
# values = [8, 9, 5, 10, 8, 6, 8, 7, 9, 9.5]
# def soc_func(*values):
#     max_num = max(values)
#     min_num = min(values)
#
#     max_loc = values.index(max_num)
#     min_local = values.index(min_num)
#
#     message = " 最小值的位置是 {min_local} , 最小值是 {min_num}.\n最大值的位置是 {max_loc}, 最大值是{max_num}.".format(
#         min_local=min_local, min_num=min_num, max_loc=max_loc, max_num=max_num)
#
#     num_total=sum(values)
#     num_total=num_total-max_num-min_num
#
#     socer=num_total/8
#
#     message_soc='平均分是{},有效评分有8个'.format(socer)
#     print(message+'\n'+message_soc)
# soc_func(*values)
import random
a=set()
# while
for i in range(0,20):
    num_a=random.randint(1,100)
    while num_a in a:
        num_a = random.randint(1, 100)
    a.add(num_a)
print(len(a))