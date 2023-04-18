# li = ["alex", "WuSir", "ritian", "barry", "武沛齐"]
# data=[1,"a",3,4,"heart"]
# s = "qwert"
# print(len(li))
# li.append("seven")
# print(li)
# li.insert(0,"Tony")
# print(li)
# li[1] = "Kelly"
# print(li)
# li[2] = "妖怪"
# print(li)
# li.extend(data)
# print(li)
# str_len = len(s)
# for i in range(str_len):
#     li.append(s[i])
#     i+=1
# print(li)
# li.remove("barry")
# print(li)
# li.pop(1)
# print(li)
# list_len = len(li)
# for i in range(4,0,-1):
#     li.pop(i)
# print(li)

# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# li1 = li[0:3]
# print(li1)
# li2 = li[3:6]
# print(li2)
# li3 = li[1:6:2]
# print(li3)
# li4 = li[1::2]
# print(li4)
# li5 = li[len(li)-1:len(li)-2:-1]
# print(li5)
# li6 = li[len(li)-3::-2]
# print(li6)

#
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# print(lis)
# """- 将列表lis中的第2个索引位置的值变成大写，并打印列表。
# - 将列表中的数字3变成字符串"100"
# - 将列表中的字符串"tt"变成数字 101
# - 在 "qwe"前面插入字符串："火车头"""
# lis[2] = lis[2].upper()
# print(lis)
# print(len(lis[]))
# for i in range(len(lis)):
#     for j in range(len(lis[i])):
#         if lis[i][j]==3:
#             lis[i][j]==100
# print(lis)

# users = ["武沛齐","景女神","肖大侠"]
# for i in range(len(users)):
#     print(users[i])

# goods = ['汽车','飞机','火箭']
# choose = int(input("please enter your choose"))
# message = "用户输入{},您选择的商品是{}".format(choose,goods[choose])
# print(message)

# num = []
# for i in range(0,50):
#     if i%3==0:
#         num.append(i)
# print(num)

# num = []
# for i in range(0,50):
#     if i%3==0:
#         num.insert(0,i)
# print(num)

# li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
"""查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表"""
# li_len = len(li)
# a_list = []
# for i in range(li_len):
#     li[i] = li[i].strip()
#     if li[i].startswith("a"):
#         a_list.append(li[i])
#     i+=1
# print(li)
# print(a_list)

# data = ["京1231", "冀8899", "京166631", "晋989"]
# data_len = len(data)
# jing_data = []
# for i in range(data_len):
#     if data[i].startswith("京"):
#         jing_data.append(data[i])
# message = "京牌共有{}个，为：{}".format(len(jing_data),jing_data)
# print(message)

# text = "wupeiqi|alex|eric"
# text_list = text.split("|")
# print(text_list)
# text_tuple = tuple(text_list)
# print(text_tuple)

# 花色列表
color_list = ["红桃", "黑桃", "方片", "梅花"]

# 牌值
num_list = []
for num in range(1, 14):
    num_list.append(num)

print(num_list)
result = []
# 请根据以上的花色和牌值创建一副扑克牌（排除大小王）
# 最终result的结果格式为： [ ("红桃",1), ("红桃",2) ... ]
for i in range(len(color_list)):
    for j in range(len(num_list)):
        board = (color_list[i],num_list[j],)
        result.append(board)
print(result)