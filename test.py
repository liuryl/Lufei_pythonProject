# enter_list = []
# enter_str = ''
# while True:
#     your_input = input("please enter")
#     if your_input == 'q' or your_input == 'Q':
#         print("break")
#         break
#     enter_list.append(your_input)
# for element in enter_list:
#     print(element)
#     enter_str = '_'.join(element)
#     print(element)
# print(enter_list)
# print(enter_str)


# 如 10.3.9.12 转换规则为：
#      10            00001010
#       3             00000011
#       9             00001001
#      12            00001100
# 再将以上二进制拼接起来，然后再进行一次翻转。
#
# 最终将翻转之后的二进制转换为整型。
#
# num_int_list = [10,3,9,12]
# num_t_list = []
# t_num = ''
# re_num = ''
# for i in num_int_list:
#     i=bin(i)
#     i = i.split('b')
#     i = i[1]
#     i = i.zfill(8)
#     num_t_list.append(i)
#     print(i)
# for j in num_t_list:
#     t_num = j+t_num
# print(t_num)
# k = len(t_num)
# for k in range(len(t_num),0,-1):
#
# # re_t_num = t_num.
# print(num_t_list)



#
# car_list = ['鲁A32444', '沪B12333', '京B8989M', '京C49678', '黑C46555', '晋B25041', '沪C34567']
#
# # 根据以上代码获取各省车牌数量，例如：info = {"沪":2,"京":2 ...}
# info = dict()
# h = 0
# j = 0
# hei = 0
# l = 0
# jin = 0
# for car in car_list:
#     if car.startswith("沪"):
#         h += 1
#         info.setdefault("沪",h)
#         info['沪'] = h
#         # print(h)
#     elif car.startswith("京"):
#         j += 1
#         info.setdefault("京",j)
#         info["京"] = j
#     elif car.startswith("黑"):
#         hei += 1
#         info.setdefault("黑",hei)
#         info["黑"] = hei
#     elif car.startswith("鲁"):
#         l += 1
#         info.setdefault("鲁",l)
#         info["鲁"] = l
#     elif car.startswith("晋"):
#         jin += 1
#         info.setdefault("晋",jin)
#         info["晋"] = jin
# print(info)




text = """ id,name,age,phone,job
            1,alex,22,13651054608,IT 
            2,wusir,23,13304320533,Tearcher
            3,老男孩,18,1333235322,IT"""

# 将上述数据处理为如下格式的结果：
#    info = [{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'},.... ..]
# 提示：text的内容是根据 \n 分割（\n表示回车换行）。
# print(text)
# text = text.split()
# info = []
# user_dict = dict()
# the_dict = dict()
# # print(text)
# str_list = []
# for str_1 in text:
#     str_1 = str_1.split(',')
#     str_list.append(str_1)
#     # print(str_1)
# for i in range(1,len(str_list)):
#     name_i = str(i)
#     name = "dict_" + name_i
#     name = dict()
#     # print(name)
#     for j in range(0,4):
#
#         name.setdefault(str_list[0][j],str_list[i][j])
#         # the_dict[str_list[0][j]] = str_list[i][j]
#         # print(str_list[i][j])
#     info.append(name)
#     # print(the_dict)
# # print(str_list)
# print(info)
# print(info)


# content = input("请输入内容:") # 用户可能输入 5*9*99.... 或 5* 9 * 10 * 99 或 5 * 9 * 99...
# content = content.split('*')
# num = 1
# for i in range(len(content)):
#     num = num * int(content[i])
#
# print(num)
# 补充代码实现

# num_list = []
# str_num_1 = ''
# str_num_2 = ''
# str_num_3 = ''
# str_num_4 = ''
# str_num_5 = ''
# str_num_6 = ''
# str_num_7 = ''
# str_num_8 = ''
# str_num_9 = ''
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         message = "{}*{}".format(i,j)
#         num_list.append(message)
#         print(message)
# print(num_list)
# for j in range(len(num_list)):
#     if num_list[j].startswith('1'):
#         str_num_1 = str_num_1 + num_list[j]
#     elif num_list[j].startswith('2'):
#         str_num_2 = str_num_2 + num_list[j]
#     elif num_list[j].startswith('3'):
#         str_num_3 = str_num_3 + num_list[j]
#     elif num_list[j].startswith('4'):
#         str_num_4 = str_num_4 + num_list[j]
#     elif num_list[j].startswith('5'):
#         str_num_5 = str_num_5 + num_list[j]
#     elif num_list[j].startswith('6'):
#         str_num_6 = str_num_6 + num_list[j]
#     elif num_list[j].startswith('7'):
#         str_num_7 = str_num_7 + num_list[j]
#     elif num_list[j].startswith('8'):
#         str_num_8 = str_num_8 + num_list[j]
#     elif num_list[j].startswith('9'):
#         str_num_9 = str_num_9 + num_list[j]
# # for k in range(1,20):
# #     message_1 =
# #     print(str_num_1)
# print(str_num_3)


# 需求：
#
# - 生成一副扑克牌（自己设计扑克牌的结构，小王和大王可以分别用14、15表示 ）
#
# - 3个玩家
# user_list = ["alex","武沛齐","李路飞"]
# - 发牌规则
#
#   - 默认先给用户发一张牌，其中 J、Q、K、小王、大王代表的值为0.5，其他就是则就是当前的牌面值。
#   - 用户根据自己的情况判断是否继续要牌。
#     - 要，则再给他发一张。
#     - 不要，则开始给下个玩家发牌。
#   - 如果用户手中的所有牌相加大于11，则表示爆了，此人的分数为0，并且自动开始给下个人发牌。
#
# - 最终计算并获得每个玩家的分值，例如：
# result = {
#       "alex":8,
#       "武沛齐":9,
#       "李路飞":0
#   }
# 必备技术点：随机抽排

# import random
#
# total_poke_list = [("红桃", 1), ("黑桃", 2), ("大王", 15), ("小王", 14)]
#
# # 随机生成一个数，当做索引。
# index = random.randint(0, len(total_poke_list) - 1)
# # 获取牌
# print("抽到的牌为：", total_poke_list[index])
# # 踢除这张牌
# total_poke_list.pop(index)
#
# print("抽完之后，剩下的牌为：", total_poke_list)


import random

# 代码示例：（请补充实现）
total_poke_list = []
card = []
result = {}
user_list = ["alex","武沛齐","李路飞"]
color_list = ["红桃", "黑桃", "方片", "梅花"]
big_king = ('大王', 15*0.5)
small_king = ('小王', 14*0.5)

for color in color_list:
    for i in range(1,14):
        card.append(color)
        if i>10:
            i = i*0.5
        card.append(i)
        card_tuple = tuple(card)
        # print(card_tuple)
        total_poke_list.append(card_tuple)
        card.clear()
# 补充代码
total_poke_list.append(big_king)
total_poke_list.append(small_king)
print(total_poke_list)
for name in user_list:
    first_num = random.randint(0,len(total_poke_list)+1)
    first_card = total_poke_list[first_num]
    result.setdefault(name,first_card[1])
    total_poke_list.pop(first_num)
print(result)
while True:
    alex_choose = input("please alex enter y or n")
    if alex_choose == 'n':
        print("alex choose skip")
        pass
    elif alex_choose == 'y':
        alex_new_num = random.randint(0,len(total_poke_list)-1)
        alex_new_card = total_poke_list[alex_new_num][1]
        # print(alex_new_card)
        new_num = int(alex_new_card) + int(result['alex'])
        # print(new_num)
        if new_num > 11:
            print("alex boom")
            new_num = 0
        result.update({'alex': new_num})
        # print(alex_new_card)
        print(result['alex'])
        total_poke_list.pop(alex_new_num)
    # wupeiq_choose = input("please enter y or n")
    # if wupeiq_choose == 'n':
    #     print("wupeiqi choose skip")
    #     pass

    wu_choose = input("please wu_choose enter y or n")
    if wu_choose == 'n':
        print("wu_choose choose skip")
        pass
    elif wu_choose == 'y':
        wu_new_num = random.randint(0,len(total_poke_list)-1)
        wu_new_card = total_poke_list[wu_new_num][1]
        # print(wu_new_card)
        new_num = int(wu_new_card) + int(result['武沛齐'])
        # print("wu"+str(new_num))
        if new_num > 11:
            print("wu boom")
            new_num = 0
        result.update({'武沛齐': new_num})
        # print(wu_new_card)
        print(result['武沛齐'])
    total_poke_list.pop(wu_new_num)



    li_choose = input("please wu_choose enter y or n")
    if li_choose == 'n':
        print("li_choose choose skip")
        pass
    elif li_choose == 'y':
        li_new_num = random.randint(0, len(total_poke_list)-1)
        li_new_card = total_poke_list[li_new_num][1]
        # print(li_new_card)
        new_num = int(li_new_card) + int(result['李路飞'])
        # print("li" + str(new_num))
        if new_num > 11:
            print("li boom")
            new_num = 0
        result.update({'李路飞': new_num})
        # print(li_new_card)
        print(result['李路飞'])
    total_poke_list.pop(li_new_num)

    if len(total_poke_list) == 0:
        print("end")
        break
    print("len : "+str(len(total_poke_list)))