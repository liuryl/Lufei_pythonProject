# data_list = [
#     '1-5 编译器和解释器.mp4',
#     '1-17 今日作业.mp4',
#     '1-9 Python解释器种类.mp4',
#     '1-16 今日总结.mp4',
#     '1-2 课堂笔记的创建.mp4',
#     '1-15 Pycharm使用和破解（win系统）.mp4',
#     '1-12 python解释器的安装（mac系统）.mp4',
#     '1-13 python解释器的安装（win系统）.mp4',
#     '1-8 Python介绍.mp4', '1-7 编程语言的分类.mp4',
#     '1-3 常见计算机基本概念.mp4',
#     '1-14 Pycharm使用和破解（mac系统）.mp4',
#     '1-10 CPython解释器版本.mp4',
#     '1-1 今日概要.mp4',
#     '1-6 学习编程本质上的三件事.mp4',
#     '1-18 作业答案和讲解.mp4',
#     '1-4 编程语言.mp4',
#     '1-11 环境搭建说明.mp4'
# ]
#
# result=[item.rsplit('.',1)[0] for item in data_list]
# print(result)

# info = {
#     "name":"武沛齐",
#     "email":"xxx@live.com",
#     "gender":"男",
# }
#
#
# resule=';'.join(['{}-{}'.format(key,value) for key,value in info.items()])
# print(resule)

#
# info = {
#     'sign_type': "MD5",
#     'out_refund_no': "12323",
#     'appid': 'wx55cca0b94f723dc7',
#     'mch_id': '1526049051',
#     'out_trade_no': "ffff",
#     'nonce_str': "sdfdffd",
#     'total_fee': 9901,
#     'refund_fee': 10000
# }
#
# result = sorted(info.items(), key=lambda x: x[0])
# print(result)
# data = '&'.join(['{}-{}'.format(key, value) for key, value in result])
# print(data)


# # 请用列表推导式实现，踢出列表中的字符串，最终生成一个新的列表保存。
# data_list = [11,22,33,"alex",455,'eirc']
#
# new_data_list = [ i for i in data_list if type(i)!=str] # 请在[]中补充代码实现。
# print(new_data_list)
# # 提示：可以用type判断类型


# # 请用列表推导式实现，对data_list中的每个元素判断，如果是字符串类型，则计算长度作为元素放在新列表的元素中；
# # 如果是整型，则让其值+100 作为元素放在新的列表的元素中。
# data_list = [11, 22, 33, "alex", 455, 'eirc']
#
# new_data_list = [i + 100 if type(i) == int else len(i) for i in data_list]  # 请在[]中补充代码实现。
# print(new_data_list)
# # 提示：可以基于三元运算实现
#
#
# # 请使用字典推导式实现，将如果列表构造成指定格式字典.
# data_list = [
#     (1, 'alex', 19),
#     (2, '老男', 84),
#     (3, '老女', 73)
# ]
# data = {item[0]: item for item in data_list}
# print(data)
# # 请使用推导式将data_list构造生如下格式：
# """
# info_dict = {
#     1:(1,'alex',19),
#     2:(2,'老男',84),
#     3:(3,'老女',73)
# }
# """


# # 有4个人玩扑克牌比大小，请对比字典中每个人的牌的大小，并输入优胜者的姓名（值大的胜利，不必考虑A）。
# player = {
#     "武沛齐": ["红桃", 10],
#     "alex": ["红桃", 8],
#     'eric': ["黑桃", 3],
#     'killy': ["梅花", 12],
# }
#
# data = sorted(player.items(), key=lambda x: x[1][1])
# print(data)


def fib(max_count):
    first = 1
    second = 0
    count_inner = 0
    while count_inner < max_count:
        ndxt_count = first + second
        first = second
        second = ndxt_count
        yield ndxt_count
        count_inner += 1


count = input("请输入要生成斐波那契数列的个数：")
count = int(count)
fib_generator = fib(count)
for num in fib_generator:
    print(num)
