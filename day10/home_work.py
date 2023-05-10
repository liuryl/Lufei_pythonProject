# # 于csv格式实现 用户的注册 & 登录认证。详细需求如下：
# #
# # - 用户注册时，新注册用户要写入文件csv文件中，输入Q或q则退出。
# # - 用户登录时，逐行读取csv文件中的用户信息并进行校验。
# # - 提示：文件路径须使用os模块构造的绝对路径的方式。
#
# # for循环和else搭配使用的时候for中有break时不会执行else中的内容
# # for i ,item in enumerate(list,num),i从num开始计数print（i）输出的是num开始加1
#
#
# import csv
# import os
#
# # 文件路径的处理
# base_dir_local=os.path.dirname(os.path.abspath(__file__))
# ab_file_path=os.path.join(base_dir_local,'db.csv')
#
# # 用户注册
# while True:
#     choice=input("是否进行注册（Y/N）")
#     choice=choice.upper()
#     if choice not in ('N','Y'):
#         print("error,your entern is error")
#         continue
#     if choice=='N':
#         break
#     with open(ab_file_path,mode='a',encoding='utf-8') as file_objecct:
#         while True:
#             user_name=input("please enter the username")
#             if user_name.upper()=='Q':
#                 break
#             user_pwd=input('please enter the userpwd')
#             file_objecct.write('{},{}\n'.format(user_name,user_pwd))
#             file_objecct.flush()
#     break
# #     用户登录
# print("welcome")
# username=input('please enter username')
# userpwd=input('please enter userpwd')
# if not os.path.exists(ab_file_path):
#     print('用户文件不存在')
# else:
#     with open(ab_file_path,mode='r',encoding='utf-8') as file_objecct:
#         for line in file_objecct:
#             user,passward=line.strip().split(',')
#             if username==user and userpwd==passward:
#                 print("success")
#                 break
#         else:
#             print('error,please check username and password')
#
#
# # import csv
# # import os
# # with open('user_data.csv', mode='a', encoding='utf-8') as user_csv:
# #     while True:
# #         user_choose = input('enter login or regist')
# #         user_name = input('enter user name')
# #         user_pwd = input('enter you password')
# #         user_list=[user_name,user_pwd]
# #         if user_choose.lower() == 'login':
# #             print('login')
# #             for user_data in user_csv:
# #                 user_name_data, user_pwd_data = user_data.split('-')
# #                 if not (user_name_data == user_name and user_pwd_data == user_pwd):
# #                     print('error')
# #                     continue
# #                 print('success')
# #         elif user_choose.lower() == 'register':
# #             print('register')
# #             write_csv = csv.writer(user_csv)
# #             # if len(user_csv.readline(1)) == 0:
# #             #     print('this is the first enter')
# #             #     write_csv.writerow('username', 'userpwd')
# #             # write_csv.writerow(user_name)
# #             write_csv.writerow(user_list)
# #
# #         else:
# #             print('error,please enter login or register')
# import os
import shutil

# # 补充代码：实现去网上获取指定地区的天气信息，并写入到Excel中。
# import os
# import requests
# from xml.etree import ElementTree as ET
# from openpyxl import workbook
#
# # 处理文件路径
# base_local = os.path.dirname(os.path.abspath(__file__))
# target_excel_file_path = os.path.join(base_local, 'weather.xlsx')
#
# # 创建excel文件
# wb = workbook.Workbook()
# del wb['Sheet']
#
# while True:
#     enter_city = input("enter city (q/Q is quit)")
#     if enter_city.upper() == 'Q':
#         break
#     url_local = "http://ws.webxml.com.cn//WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName={}".format(
#         enter_city)
#     res = requests.get(url=url_local)
#     print(res.text)
#
#     # 提取xml
#     root = ET.XML(res.text)
#
#     # 为每个城市建立一个sheet
#     sheet = wb.create_sheet(enter_city)
#
#     for row_index, node in enumerate(root, 1):
#         text = node.text
#         cell = sheet.cell(row_index, 1)
#         cell.value = text
# wb.save(target_excel_file_path)


# 从ini文件读写到excel
#
# import os
# from openpyxl import workbook
# from openpyxl.styles import Alignment, Border, Side, Font, PatternFill
# import configparser
#
# base_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(base_dir, 'my.ini')
# traget_file_path = os.path.join(base_dir, 'my.xlsx')
#
# # 创建excel并默认创建了sheet
# wb = workbook.Workbook()
# # 删除默认创建的sheet
# del wb['Sheet']
#
# # 加载ini文件
# config = configparser.ConfigParser()
# config.read(file_path, encoding='utf-8')
#
# # 循环每个节点
# for section in config.sections():
#     # 在excel中创建sheet，名称为节点名
#     sheet = wb.create_sheet(section)
#
#     # 边框和居中
#     side = Side(style='thin', color='000000')
#     border = Border(top=side, bottom=side, left=side, right=side)
#     align = Alignment(horizontal='center', vertical='center')
#
#     # 为此在sheet设置表头
#     title_dict = {'A1': '键', 'B1': '值'}
#     for position, text in title_dict.items():
#         # set the local
#         cell = sheet[position]
#         # set the value
#         cell.value = text
#         # 设置剧中
#         cell.alignment = align
#         # 背景色
#         cell.fill = PatternFill('solid', fgColor='6495ED')
#         # 设置字体颜色
#         cell.font = Font(name='微软雅黑')
#         # 设置边框
#         cell.border = border
#     row_index = 2
#     # 读取节点下的所有键值，并写入sheet
#     for group in config.items(section):
#         for col, text in enumerate(group, 1):
#             cell = sheet.cell(row_index, col)
#             cell.alignment = align
#             cell.border = border
#             cell.value = text
#         row_index += 1
# wb.save(traget_file_path)


import os
import requests
import shutil

base_dir=os.path.dirname(os.path.abspath(__file__))
down_load_path=os.path.join(base_dir,'package')
if not os.path.exists(down_load_path):
    os.makedirs(down_load_path)


# 1.下载文件
file_url = 'https://files.cnblogs.com/files/wupeiqi/HtmlStore.zip'
res = requests.get(url=file_url)
res.content

# 将下载的文件保存到指定目录
file_name=file_url.split('/')[-1]
zip_file_path=os.path.join(down_load_path,file_name)
with open(zip_file_path,mode='wb') as file_object:
    file_object.write(res.content)

# 解压
unpack_floder=os.path.join(base_dir,'html')
shutil.unpack_archive(filename=zip_file_path,extract_dir=unpack_floder,format='zip')