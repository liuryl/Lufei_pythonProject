# # 有一个数据结构如下所示，请编写一个函数从该结构数据中返画由指定的 字段和对应的值组成的字典。如果指定字段不存在，则跳过该字段。
# DATA = {
#     "time": "2016-08-05T13:13:05",
#     "some_id": "ID1234",
#     "grp1": {"fld1": 1, "fld2": 2, },
#     "xxx2": {"fld3": 0, "fld4": 0.4, },
#     "fld6": 11,
#     "fld7": 7,
#     "fld46": 8
# }
#
# # fields:由"|"连接的以fld开头的字符串, 如fld2|fld7|fld29
#
# def select(fields):
#     result={}
#     fields = fields.split('|')
#     for input_value in fields:
#         value=DATA.get(input_value)
#         if not value:
#             continue
#         result[fields]=value
#     print(DATA)
#     return result
#
# fields='fld2|fld7|fld29'
# fields=fields.split('|')
# for i in fields:
#     print(DATA.get(i))


# 内部维护的数据有：0123456789AB..Zab..z(10个数字+26个大写字母+26个小写字母)。
# 当执行函数：
# 	base62encode(1)，获取的返回值为1
# 	base62encode(61)，获取的返回值为z
# 	base62encode(62)，获取的返回值为10
# import itertools
# import string
#
# num_map = list(itertools.chain(string.digits, string.ascii_lowercase, string.ascii_uppercase))
# print(num_map)
#
#
def base62encode(num):
    num_map_len = len(num_map)
    result_num = []
    while num >= num_map_len:
        num, remain = divmod(num, num_map_len)
        result_num.insert(0, num_map[remain])
    result_num.insert(0, num_map[num])
    result = ''.join(result_num)
    return result
#
# print(base62encode(62))



v1=[' '.join(['{}*{}'.format(j,i) for j in range(1,i+1)]) for i in range(1,10)]
print(v1)