import datetime
import requests
import time
import os
import csv
from datetime import *


def check_the_file_local():
    base_local = os.path.dirname(os.path.abspath(__file__))
    mp4_local = '{}/{}'.format(base_local, 'mp4_files')
    print(mp4_local)
    if not os.path.exists(mp4_local):
        os.mkdir(mp4_local)
    return mp4_local


def get_mp4_name(id):
    time_mp4 = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    mp4_name = '{}-{}.mp4'.format(id, time_mp4)
    return mp4_name


def get_file_local():
    '''
    获取文件地址
    :return: 返回video的地址
    '''
    base_local = os.path.dirname(os.path.abspath(__file__))
    csv_path = '{}/{}/{}'.format(base_local, 'csv_data', 'video.csv')
    return csv_path


def download_video(id, targe_url):
    '''
    下载视频
    :param targe_url: 视频网址
    :return:
    '''
    res = requests.get(
        url=targe_url
    )
    # 视频总大小（字节）
    file_size = int(res.headers['Content-Length'])

    download_size = 0

    file_local = check_the_file_local()
    mp4_file_name = file_local + '/' + get_mp4_name(id)

    with open(mp4_file_name, mode='wb') as file_object:
        # 分块读取下载的视频文件（最多一次读128字节），并逐一写入到文件中。 len(chunk)表示实际读取到每块的视频文件大小。
        for chunk in res.iter_content(128):
            download_size += len(chunk)
            file_object.write(chunk)
            file_object.flush()
            message = "视频总大小为：{}字节，已下载{}字节。".format(file_size, download_size)
            message_percent = int(download_size / file_size * 100)
            print('\r{}%'.format(message_percent), end="")
        file_object.close()

    res.close()


def output_percent():
    print("正在下载中...")
    for i in range(101):
        text = "\r{}%".format(i)
        print(text, end="")
        time.sleep(0.2)

    print("\n下载完成")


def open_csv_file():
    csv_path = get_file_local()
    with open(csv_path, mode='r', encoding='utf-8') as csv_object:
        # csv_object.readline()
        csv_value = csv.reader(csv_object)

        csv_list = list(csv_value)
        # print(csv_list)
    return csv_list


def read_csv_page():
    '''
    读取指定页面的新闻
    :param the_page: 传入选择的页面
    :return: 无
    '''
    while True:
        the_page = input('分页看新闻每页显示10条新闻 (q/Q退出)')

        if the_page.isalpha() and the_page.upper() != 'Q':
            print('error')
        if the_page.upper() == 'Q':
            return
        if int(the_page) > 10:
            the_page = 1
        csv_list = open_csv_file()
        for i in range((int(the_page) - 1) * 10, int(the_page) * 10):
            message = '{} {}'.format(i + 1, csv_list[i][1])
            print(message)


def search_news():
    '''
    根据关键字查看新闻
    :param args: 输入的关键字，代码或者字符
    :return:
    '''
    csv_list = open_csv_file()
    id_list = []
    name_list = []
    while True:
        id = input('搜索新闻，使用id或者关键字，id=1715046，key=北京 (q/Q退出)')

        if id.isalpha() and id.upper()!='Q':
            print('error')
        if id.upper() == 'Q':
            return
        for item in csv_list:
            id_list.append(item[0])
            name_list.append(item[1])
            '''
            根据代码查找新闻
            '''
        if (id.isdecimal()) and (id in id_list):
            id_local = id_list.index(id)
            name_value = name_list[id_local]
            message = '{num} {name_value}'.format(num=round(1), name_value=name_value)
            print(message)
        '''根据关键字查找新闻'''
        if not id.isdecimal():

            message_list = [name_str for name_str in name_list if id in name_str]

            for num, value in enumerate(message_list, 1):
                message = '{} {}'.format(num, value)
                print(message)


def download_target():
    while True:
        id=input('\n下载新闻，输入视频id，id=1715046(q/Q是退出)')

        if id.isalpha() and id.upper()!='Q':
            print('error')
            continue
        if id.upper()=='Q':
            return
        csv_list = open_csv_file()
        # print(csv_list)
        id_list = []
        url_list = []
        for item in csv_list:
            id_list.append(item[0])
            url_list.append(item[-1])
        # print(id_list)
        # print(url_list)
        id_index = id_list.index(id)
        target_url = url_list[id_index]
        print(target_url)
        # print(target_url)
        download_video(id, target_url)


def menu():
    while True:
        menu_list = ['1.分页看新闻', '2.搜索专区', '3.下载专区']
        function_list = [read_csv_page, search_news, download_target]
        menu_str = ';'.join(menu_list)
        print(menu_str)
        user_choose = input('请输入序号，q为退出')
        if user_choose.isalpha() and user_choose.lower() != 'q':
            print('error')
            continue
        if (user_choose.isalpha()) and (user_choose.lower() == 'q'):
            return 'q'
        if (int(user_choose) <= 3 and int(user_choose) > 0):
            use_function = function_list[int(user_choose)-1]
            use_function()


if __name__ == '__main__':
    print('i')
    while True:
        result = menu()
        if result == 'q':
            break