# def func(*args, **kwargs):
#     prev = "-".join(args)
#
#     data_list = []
#     for k, v in kwargs.items():
#         item = "{}-{}".format(k, v)
#         data_list.append(item)
#         content = "*".join(data_list)
#
#     return prev, content
#
#
# v1 = func("北京", "上海", city="深圳", count=99)
# print(v1)
#
# v2 = func(*["北京", "上海"], **{"city": "深圳", "count": 99})
# print(v2)


# 获取天气信息示例
import requests


def get_weather(code):
    """ 获取天气信息 """
    url = "http://www.weather.com.cn/data/ks/{}.html".format(code)
    res = requests.get(url=url)
    res.encoding = "utf-8"
    weather_dict = res.json()
    return weather_dict


def write_file(**kwargs):
    print(kwargs)
    weather_dict = kwargs
    """将天气信息拼接起来，并写入到文件
    格式要求：
    	1. 每个城市的天气占一行
    	2. 每行的格式为：city-北京,cityid-101010100,temp-18...
    """
    for key, value in weather_dict.items():
        message = '{}-{}'.format(key, value)
        city_weather_list.append(message)
    message = ','.join(city_weather_list)
    print(message)
    with open('city_weather.text', mode='a', encoding='utf-8') as weather_object:
        weather_object.write(message + '\n')
        weather_object.close()
    # 补充代码
    # with open('city_weather_str.text',mode='w',encoding='utf-8') as weather_file:


city_list = [
    {'code': "101020100", 'title': "上海"},
    {'code': "101010100", 'title': "北京"},
]

for city_name in city_list:
    city_weather_list = []
    print(city_name['code'])
    weather_dict = get_weather(city_name['code'])
    weather_dict = weather_dict['weatherinfo']
    # key,value=weather_dict
    # print(key)
    write_file(**weather_dict)
