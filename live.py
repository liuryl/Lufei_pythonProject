# # python基础
# # if
# # while
# # for
# # int
# # ......
# list_kong = [1,2]
# dict_kong = dict()
# tuple_kong = ()
# str_kong = ''
# set_kong = set()
# print(type(set_kong))
# # python3.6除了set都有序
# # if not and or优先级
# a = 1
# b = a
# b = 2
# a = 1
# c = ab
# a = [True,'python',[[1,2,(1,2)]],{1,2}]
# # print(len(a))
# # take = a[2][0][2]
# # print(take)
# # # del a[2][0][2]
# a[2][0].pop(2)
# # print(a)
# # a.insert(1,'mysql')
# print(a)
# a[1] = "luffycity"
# print(a)

# your_num = input("enter")
# num_list = []
# sum_list = 0
# for i in your_num:
#     i = int(i)
#     i = i*i
#     sum_list = i+sum_list
# print(sum_list)
# lis = ['A', 'B', 'A', 'C', 'E', 'R', 'A', 'D', 'A', 'A']
# lis = str(lis)
# lis.replace()
# for i in range(len(lis)):
#     if lis[i] == 'A':
#         lis[i] = lis[i].lower()
# print(lis)

# 编写一个程序，在程序中通过键盘输入一个范围在50-100的整数，如果不正确则提示继续输入；
#
# 1）输出用户输入整数到50的所有整数，55，54，53，52，51，50
#
# 2）求1到用户输入整数的累加和。
# your_num = input("enter a num")
# if not your_num.isdecimal():
#     your_num = input("enter a num")
# if not your_num in range(50,100):
# is_num = True
# result = 0
# while True:
#     your_num = input("enter a num")
#     if your_num.isdecimal() and (int(your_num) in range(50,101)):
#         break
# for i in range(int(your_num),49,-1):
#     print(i,end=',')
# #     打印用逗号结尾
# for i in range(int(your_num)):
#     result += i
# print(result)
#
your_enter = input("enter")
num_alpha = 0
for i in your_enter:
    # i>"a" and i<"z"
    if i.isalpha():
        num_alpha += 1
print(num_alpha)