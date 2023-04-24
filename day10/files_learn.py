# your_name = input("enter your name")
# passward = input("enter your passward")
#
# data = '{}-{}'.format(your_name,passward)
#
# file_object = open('/Users/liuriyilang/PycharmProjects/Lufei_pythonProject/learn_file.text',mode='wt',encoding='utf-8')
# file_object.write(data)
# file_object.close()
import requests

# file_object = open("learn_file.text", mode='wt', encoding='utf-8')
#
# while True:
#     your_name = input("enter your name")
#     if your_name.upper()=='Q':
#         print("break")
#         break
#     passward = input("enter your passward")
#     data = "{}-{}\n".format(your_name,passward)
#     file_object.write(data)
# file_object.close()


# 案例1：去网上下载一点文本，文本信息写入文件。

# import requests
# res_url = requests.get(url='https://unity.cn',
#                        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
#     })
#
# # 网络传输的原始二进制信息（bytes）
# # res.content
#
# file_object = open('learn_file.text', mode='wb')
# file_object.write(res_url.content)
# file_object.close()

# 案例2：去网上下载一张图片，图片写入本地文件。
# import requests
#
# res = requests.get(
#     url="https://hbimg.huabanimg.com/c7e1461e4b15735fbe625c4dc85bd19904d96daf6de9fb-tosv1r_fw1200",
#     headers={
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
#     }
# )
#
# # 网络传输的原始二进制信息（bytes）
# # res.content
#
# file_object = open('test_pythob.png', mode='wb')
# file_object.write(res.content)
# file_object.close()

#
# while True:
#     user_name = input("enter usser name")
#     if user_name.upper()=='Q':
#         print("break")
#         break
#     passward = input("enter your passward")
#
#     data = "{}--{}\n".format(user_name,passward)
#
#     file_s = open('learn_file.text',mode='a')
#     file_s.write(data)
# file_s.close()


# import requests
#
# res = requests.get(url='https://f.video.weibocdn.com/000pTZJLgx07IQgaH7HW010412066BJV0E030.mp4?label=mp4_720p&template=1280x720.25.0&trans_finger=1f0da16358befad33323e3a1b7f95fc9&media_id=4583105541898354&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=2&ot=h&ps=3lckmu&uid=3ZoTIp&ab=3915-g1,966-g1,3370-g1,3601-g0,3601-g0,3601-g0,1493-g0,1192-g0,1191-g0,1258-g0&Expires=1608204895&ssig=NdYpDIEXSS&KID=unistore,video',
#                   headers={ "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
#                   )
#
# with open('nba.mp4',mode='wb') as file_object:
#     file_object.write(res.content)


# 2日志计数
#
# ip = '223.73.89.192'
# total_count = 0
# with open('access.log',mode='r',encoding='utf-8') as file_object:
#     for line in file_object:
#         if not line.startswith(ip):
#             continue
#         total_count += 1
# print(total_count)

# # 计算每一个用户的访问次数
# user_dict = dict()
# print(type(user_dict))
# with open('access.log',mode='r',encoding='utf-8') as file_object:
#     for line in file_object:
#         user_ip = line.split(' ')[0]
#         if user_ip in user_dict:
#             user_dict[user_ip] += 1
#         else:
#             user_dict[user_ip] = 1
# print(user_dict)


# # 筛选出股票价格大于20
# with open('stock.text',mode='r',encoding='utf-8') as file_object:
#     # 跳过首航
#     file_object.readline()
#     #继续向下读
#     for line in file_object:
#         price = line.split(',')[2]
#         price = float(price)
#         if price > 20:
#             print(line.strip())


# 修改文件
# '''思路一：读到内存，使用replace（适用于小文件）
#     思路二：读文件内容，有luffcity时替换为pythonav不推荐
#     思路三：同时打开两个文件，一个读一个写
#     '''
# import shutil
# with open('ha.conf', mode='r', encoding='utf-8') as read_file, open('new_ha.conf', mode='w',
#                                                                     encoding='utf-8') as new_wirte_file:
#     for read_line in read_file:
#         new_line = read_line.replace("luffycity", 'pythonav')
#         new_wirte_file.write(new_line)
# shutil.move('new_ha.conf','ha.conf')



import os
import requests
with open('csv_learn.csv', mode='r', encoding='utf-8') as file_object:
    file_object.readline()
    for line in file_object:
        print(line)
        user_id, user_name, url = line.strip().split(',')
        print(user_name, url)
        #         根据url下载图片
        res = requests.get(url=url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        })
        # res.content
        # write the pic
        # 检查目录
        if not os.path.exists('images'):
            os.makedirs('images')
        with open('images/{}.png'.format(user_name),mode='wb') as img_object:
            img_object.write(res.content)