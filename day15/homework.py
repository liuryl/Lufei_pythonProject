# 自己去网上搜索如何基于Python计算mp4视频的时长，最终实现用代码统计某个文件夹下所有mp4的时长。
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
def get_file_path():
    file_path_list = []
    abs_path = os.path.abspath(__file__)
    the_path = os.path.dirname(abs_path)
    mp4_path = '{the_path}/{file_name}'.format(the_path=the_path, file_name='mp4_files')

    # print(mp4_path)
    data = os.walk(mp4_path)
    for path, floder_list, file_list in data:
        # print(path)
        # print(floder_list)
        # print(file_list)
        for file_name in file_list:
            file_path = path + '/' + file_name
            file_path_list.append(file_path)
    return file_path_list
    # for file_name in file_list:
    #     print(file_name)
    #     print("path"+path)
    # print(data)


def get_video_time(videopath):
    video_path = videopath

    video = VideoFileClip(video_path)

    video_duration = video.duration

    video.close()

    return video_duration


if __name__ == '__main__':
    file_path_list = get_file_path()
    for file_path in file_path_list:
        print(get_video_time(str(file_path)))
