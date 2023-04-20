"""
结合下面的两个变量 header 和 stock_dict实现注意输出股票信息，格式如下：
	SH601778，股票名称:中国晶科、当前价:6.29、涨跌额:+1.92。
    SH688566，股票名称:吉贝尔、当前价:...               。
	...
"""
# header = ['股票名称', '当前价', '涨跌额']
#
# stock_dict = {
#     'SH601778': ['中国晶科', '6.29', '+1.92'],
#     'SH688566': ['吉贝尔', '52.66', '+6.96'],
#     'SH688268': ['华特气体', '88.80', '+11.72'],
#     'SH600734': ['实达集团', '2.60', '+0.24']
# }
# for i in header:
#     print(i)
# for j in stock_dict:
#     # print("股票代码"+j)
#     message = j+","+header[0]+":"+stock_dict.get(j)[0]+","+header[1]+":"+stock_dict.get(j)[1]+","+header[2]+":"+stock_dict.get(j)[2]
#     print(message)

# for key,values in stock_dict.items():
#     # print(key,values)
#     message = []
#     for i in range(len(values)):
#         text = "{}:{}".format(header[i],values[i])
#         # print(text)
#         message.append(text)
#         # print(message)
#     # print(message)
#     data = '、'.join(message)
#     # result = key+data
#     print("{},{}".format(key,data))
# print(message)

# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}

# # 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic.setdefault("k4","v4")
# print(dic)
# # 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic["k1"]="alex"
# print(dic)
# # 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic["k3"].append(44)
# print(dic)
# # 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic["k3"].insert(0,18)
# print(dic)

# dic1 = {
#  'name':['alex',2,3,5],
#  'job':'teacher',
#  'oldboy':{'alex':['python1','python2',100]}
# }

# # 1，将name对应的列表追加⼀个元素’wusir’。
# dic1.setdefault('name').append("wusir")
# print(dic1)
# # 2，将name对应的列表中的alex全变成大写。
# dic1['name'][0] = dic1['name'][0].upper()
# print(dic1)
# # 3，oldboy对应的字典加⼀个键值对’⽼男孩’:’linux’。
# dic1['oldboy'].setdefault('老男孩','linux')
# print(dic1)
# # 4，将oldboy对应的字典中的alex对应的列表中的python2删除
# dic1['oldboy']['alex'].pop(1)
# print(dic1)


# 例如：用户输入 x1|wupeiqi ,则需要再字典中添加键值对 {'x1':"wupeiqi"}
# flag = True
# enter_dict = dict()
# while flag:
#     your_enter = input("please enter the exception is x1|wupeiqi")
#     if your_enter == 'n' or your_enter == 'N':
#         break
#     your_enter = your_enter.split('|')
#     key = your_enter[0]
#     value = your_enter[1]
#     enter_dict.setdefault(key,value)
#     # print(your_enter)
# print(enter_dict)

# key_list = []
# value_list = []
# info = {'k1':'v1','k2':'v2','k3':'v3'}
# key_list = info.keys()
# print(key_list)
# value_list = info.values()
# print(value_list)

# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# a. 请循环输出所有的key
# b. 请循环输出所有的value
# c. 请循环输出所有的key和value
# for key,value in dic.items():
#     print(key)
#     print(value)
#     print("{}:{}".format(key,value))

# info = {
#     'k1':'v1',
#     'k2':[('alex'),('wupeiqi'),('oldboy')],
# }
# value_len = len(info['k2'])
# print(value_len)
# for i in info['k2']:
#     print(i)


# str_1 = "k: 1|k1:2|k2:3  |k3 :4"
# # print(str_1)
# str_list = str_1.split('|')
# new_str_list = []
# # print(str_list)
# key_list = []
# value_list = []
# key_value = dict()
# for value in str_list:
#     value = value.split(':')
#     # print(value)
#     for value_2 in value:
#         value_2 = value_2.strip()
#         new_str_list.append(value_2)
#         # print(value_2)
#     # new_str_list = new_str_list.append(value)
# for value_3 in new_str_list:
#     if value_3.startswith('k'):
#         key_list.append(value_3)
#     else:
#         value_list.append(value_3)
# # print(key_list)
# # print(value_list)
# print(len(key_value))
# for i in range(len(key_list)):
#     key_value.setdefault(key_list[i],value_list[i])
#     # print(key_value)
# print(key_value)

"""
有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。

   result = {'k1':[],'k2':[]}
"""
# result = {'k1': [], 'k2': []}
# li= [11,22,33,44,55,66,77,88,99,90]
# for li_num in li:
#     if li_num >66:
#         result['k1'].append(li_num)
#     elif li_num < 66:
#         result['k2'].append(li_num)
# print(result)

"""
商品列表：
  goods = [
		{"name": "电脑", "price": 1999},
		{"name": "鼠标", "price": 10},
		{"name": "游艇", "price": 20},
		{"name": "美女", "price": 998}
	]
要求:
1：页面显示 序号 + 商品名称 + 商品价格，如：
      1 电脑 1999 
      2 鼠标 10
	  ...
2：用户输入选择的商品序号，然后打印商品名称及商品价格
3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4：用户输入Q或者q，退出程序。
"""
goods = [
		{"name": "电脑", "price": 1999},
		{"name": "鼠标", "price": 10},
		{"name": "游艇", "price": 20},
		{"name": "美女", "price": 998}
	]

# for i in range(len(goods)):
#     message = "{} {} {}".format(i+1,goods[i]['name'],goods[i]['price'])
#     print(message)
# while True:
# 	user_choose = input("please enter you choose")
# 	if int(user_choose) >len(goods) or int(user_choose) < 0 or user_choose.isalpha():
# 		print("error please enter again")
# 	elif user_choose == 'Q' or user_choose == 'q':
# 		print("exit")
# 		break
# 	elif int(user_choose) <len(goods) and int(user_choose) > 0:
# 		message_1 = "{}  {}".format(goods[int(user_choose)-1]['name'],goods[int(user_choose)- 1]['price'])
# 		print(message_1)