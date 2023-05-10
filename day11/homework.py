# # 请定义一个函数，用于计算一个字符串中字符`a`出现的次数并通过return返回。
# #
# # - 参数，字符串。
# # - 返回值，字符串中 a 出现的次数。
#
# def a_num(a_str):
#     i = 0
#     for a_alph in a_str:
#         if a_alph == 'a':
#             i += 1
#     return i
#
#
# a_enter = input("enter")
# num_a = a_num(a_enter)
# print(num_a)
import os


# 写函数，判断用户传入的一个值（字符串或列表或元组任意）长度是否大于5，并返回真假。
# def more_five(the_str):
#     if len(the_str)>5:
#         return True
#     return False
# your_enter=input('enter')
# print(more_five(your_enter))


# 写函数，接收两个数字参数，返回比较大的那个数字（等于时返回两个中的任意一个都可以）。
# def compare_the_size(a,b):
#     if a>b:
#         return a
#     return b
#
# aa=input("enter a")
# bb=input('enter b')
# print(compare_the_size(a=aa,b=bb))

# 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历，然后将这四个值通过"*"拼接起来并追加到一个student_msg.txt文件中。

# def the_joint(name,sex,age,education):
#     with open('user_data.text',mode='a',encoding='utf-8') as user_file:
#         message='{}*{}*{}*{}'.format(name,sex,age,education)
#         user_file.write(message)
#         user_file.flush()
#     return
# # user_data_dict={'name':None,'sex':None,'age':None,'EDUCATION':None}
# # print(len(user_data_dict))
# your_name=input('enter')
# your_sex=input('enter')
# your_age=input('enter')
# your_education=input('enter')
# the_joint(name=your_name,sex=your_sex,age=your_age,education=your_education)



# - 【位置1】读取文件中的每一行数据，将包含特定关键的数据筛选出来，并以列表的形式返回。
# - 【位置1】文件不存在，则返回None
# - 【位置2】文件不存在，输出 "文件不存在"，否则循环输出匹配成功的每一行数据。


# def select_content(file_path,key):
#     # 补充代码【位置1】
#     if not os.path.exists(file_path):
#         return None
#     data_list=[]
#     with open(file_path,mode='r',encoding='utf-8') as stock_data_file:
#         for line in stock_data_file:
#             if key in line:
#                 data_list.append(line)
#     return data_list
#
#
# result = select_content("files/xxx.txt","股票")
# # 补充代码【位置2】
# if result==None:
#     print("none")
# else:
#     print(result)


# def change_string(origin):
#     # 补充代码，将字符串origin中中的敏感词替换为 **，最后将替换好的值返回。
#     data_list = ["苍老师","波多老师","大桥"]
#     for name in data_list:
#         origin=origin.replace(name,'**')
#     return origin
#
# text = input("请输入内容：")
# result = change_string(text)
# print(result)


from openpyxl import load_workbook
import hashlib

def user_data_dict():
    get_user_dict={}
    wb=load_workbook('user.xlsx')
    sheet=wb.worksheets[0]
    for row in sheet.rows:
        get_user_dict[row[1].value]=row[2].value
    return get_user_dict


def encrypt(origin):
    encrypt_byte=origin.encode('utf-8')
    md5_object=hashlib.md5()
    md5_object.update(encrypt_byte)
    return md5_object.hexdigest()

use=input("enter")
pwd=input('enter')
encrypt_ped=encrypt(pwd)


useer_name=user_data_dict()
user_pwd=useer_name.get(use)
if encrypt_ped==user_pwd:
    print('sucess')
else:
    print('erro')