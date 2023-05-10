# # 请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先执行func函数内部代码，再输出 "after"
# def dec(origin):
#     def inner(*args,**kwargs):
#         res=origin(*args,**kwargs)
#         print('after')
#         return res
#     return inner
# @dec
# def func(a1):
#     return a1 + "傻叉"
# @dec
# def base(a1,a2):
#     return a1 + a2 + '傻缺'
#
# @dec
# def foo(a1,a2,a3,a4):
#     return a1 + a2 + a3 + a4 + '傻蛋'
# func('a')

# 请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：将被装饰的函数执行5次，讲每次执行函数的结果按照顺序放到列表中，最终返回列表。
#
# import random
# import functools
#
#
# def outer(origin):
#     @functools.wraps(origin)
#     def inner(*args, **kwargs):
#         result_list = []
#         for i in range(5):
#             res = origin(*args, **kwargs)
#             result_list.append(res)
#         return result_list
#
#     return inner
#
#
# @outer
# def func():
#     return random.randint(1, 4)
#
#
# result = func()  # 内部自动执行5次，并将每次执行的结果追加到列表最终返回给result
# print(result)


# 请为以下函数编写一个装饰器，添加上装饰器后可以实现： 检查文件所在路径（文件件）是否存在，如果不存在自动创建文件夹（保证写入文件不报错）。

# import os
# import functools
#
#
# def check_file(function_name):
#     @functools.wraps(function_name)
#     def inner_check_file(file_path):
#         # get the upper path
#         last_path = file_path.rsplit('/', 1)[0]
#         if not os.path.exists(last_path):
#             os.makedirs(file_path)
#         res = function_name(file_path)
#         return res
#
#     return inner_check_file
#
#
# def write_user_info(path):
#     file_obj = open(path, mode='w', encoding='utf-8')
#     file_obj.write("武沛齐")
#     file_obj.close()
#
#
# write_user_info('/Users/liuriyilang/PycharmProjects/Lufei_pythonProject/day13/homework.text')




 