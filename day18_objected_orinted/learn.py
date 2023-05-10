# class user_info:
#     def __init__(self, name, pwd, age):
#         self.name = name
#         self.pwd = pwd
#         self.age = age
#
#
# def get_user_info():
#     user_list = []
#     while True:
#         user_name = input('enter user name')
#         if user_name.upper() == 'Q':
#             break
#         user_pwd = input('enter user pwd')
#         user_object=user_info(user_name,user_pwd,19)
#         user_list.append(user_object)
#     for user in user_list:
#         username=user.name
#         userpwd=user.pwd
#         print(username)
#         print(userpwd)
# get_user_info()

#
# class get_user_in_page:
#     def __init__(self,page_num,every_page=10):
#         self.every_page=every_page
#
#         if not page_num.isdecimal():
#             self.page_num=1
#             return
#         page_num=int(page_num)
#         if page_num<1:
#             self.page_num=1
#             return
#         self.page_num=page_num
#
#     def start_num(self):
#         return (self.page_num-1)*self.every_page
#     def end_num(self):
#         return self.page_num*self.every_page
#
# user_list=['user-{}'.format(i) for i in range(1,3000)]
# while True:
#     page=input('enter the page')
#     page_num=get_user_in_page(page,20)
#     page_data_list=user_list[page_num.start_num():page_num.end_num()]
#     for item in page_data_list:
#         print(item)


import requests
import os


class DouYin:
    def __init__(self, floder_path):
        self.fold_path = floder_path

        if not os.path.exists(floder_path):
            os.mkdir(floder_path)

    def download(self, file_name, url):
        res = requests.get(url=url,
                           headers={
                               "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
                           })
        file_path = os.path.join(self.fold_path, file_name)
        with open(file_path, mode='wb') as file_object:
            file_object.write(res.content)
            file_object.flush()

    def multi_download(self, video_list):
        for item in video_list:
            self.download(item[0], item[1])


if __name__ == '__main__':
    douyin_object = DouYin('videos')
    douyin_object.download('luosi.mp4',
                           "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
    video_list = [
        ("a1.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg"),
        ("a2.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag"),
        ("a3.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
    ]
    douyin_object.multi_download(video_list)