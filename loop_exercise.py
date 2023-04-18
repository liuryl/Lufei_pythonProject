# # 猜数字
# number = 66
# flag = True
# while flag:
#     your_num = input("please enter you number")
#     your_num = int(your_num)
#     if your_num<number:
#         print("small")
#     elif your_num>number:
#         print("big")
#     else:
#         print("true")
#         flag = False

# 使用循环输出0-100
# i =0
# while i<=100:
#     print(i)
#     i=i+1

# i=0
# while i<=100:
#     if (i%2) !=0:
#         print(i)
#     i=i+1

# i=0
# while i<=100:
#     if(i%2)==0:
#         print(i)
#     i+=1


# flag = True
# i = 3
# local_name = "liuri"
# local_password = "999"
#
# while i>0:
#     username = input("please enter you user name")
#     password = input("please enter you password")
#     if username == local_name and password == local_password:
#         print("success")
#         break
#     else:
#         print("error please enter again")
#         massage = "you times is {}".format(i-1)
#         print(massage)
#         i -=1

# age = 10
# i=0
# while i<3:
#     your_age = int(input("please enter your age"))
#     if your_age == age:
#         print("successed")
#         break
#     elif i == 2:
#         again = input("do you want to play the game again?")
#         if again == "y":
#             i=0
#             continue
#         elif again =="n":
#             print("break")
#             break
#     i+=1


# your_enter = input("please enter your word")
# if your_enter.startswith("al"):
#     print("yes")
# else:
#     print("no")
#
# end_enter = input("please enter")
# if end_enter.endswith("Nb"):
#     print("yes")
# else:
#     print("no")


# your_name = input("please enter your name")
# your_name = your_name.replace("l","p")
# print(your_name)

# your_num = input("please enter you num")
# if your_num.isdecimal():
#     your_num = int(your_num)
#     print("yes")
#     print(your_num)
# else:
#     print("error")

# your_num = input("please enter")
# your_num = your_num.split("+")
# print(type(your_num))
# print(len(your_num))
# i = len(your_num)
# j=0
# while j<i:
#     if your_num[j].isdigit():
#         print(str(j)+"is digital")
#     elif your_num[j].isalpha():
#         print("is letter")
#     j+=1


# the_num = input("please enter a equal")
# the_num = the_num.split("+")
# i = len(the_num)
# j =0
# sum = 0
# while j<i:
#     the_num[j] = the_num[j].strip()
#     print(the_num[j])
#     sum = sum+int(the_num[j])
#     j+=1
# print(sum)


# import random
# print("i")
# random_code = random.randrange(1,9999999)
# print(random_code)
# msg = "欢迎登陆系统你的验证码为:{},你的手机号为:{}".format(random_code,"13303059500")
# print(msg)

# data_list = []
# while True:
#     hobby = input("please your hobby , q is break")
#     if hobby=="q":
#         print("break")
#         break
#     data_list.append(hobby)
# i = len(data_list)
# j=0
#
# list_str = ",".join(data_list)
# # print(list_str)
# print(list_str)

# v1 = 675
# v1 = bin(v1)
# print(v1)
# v2 = "0b11000101" # 请将二进制v2转换为十进制（整型）
# v2 = int(v2,base=2)
# print(v2)
# v3 = "11000101"   # 请将二进制v3转换为十进制（整型）
# v3 = int(v3,base=2)
# print(v3)

# v1 =123
# v2 = 456
# v1 = bin(v1)
# v2 = bin(v2)
# print(v1+v2)
# v1 = v1.rsplit('b')
# v1 = v1[1]
# v2 = v2.rsplit('b')
# v2 = v2[1]
# print(v1)
# print(v2)
# sum = v1+v2
# print(sum)
# print(type(sum))
# # bin(sum)
# sum = int(sum,base = 2)
# print(sum)

# v1 = 123
# v2 = 456
# v1 = bin(v1)
# v2 = bin(v2)
# v1 = v1.split('b')
# v2 = v2.split('b')
# v1 = v1[1]
# v2 = v2[1]
# v1 = v1.zfill(16)
# v2 = v2.zfill(16)
# sum = v1+ v2
# sum = int(sum,base = 2)
# print(sum)

# your_str = input("please enter")
# your_str = your_str.replace("苍老师","***")
# print(your_str)

# name = "aleX leNb "
# name = name.strip()
# print(name)
# if name.startswith('al'):
#     print("yes")
# if name.endswith('Nb'):
#     print("yes")
# name1 = name.replace('l','p')
# print(name1)
# name2 = name.split('l')
# print(name2)
# name3 = name.rsplit('l',1)
# print(name3)
# name4 = name.upper()
# print(name4)

# s = "123a4b5c"
# s1 = s[0:3]
# print(s1)
# s2 = s[3:6]
# print(s2)
# s3 = s[-1]
# print(s3)
# s4 = s[5::-2]
# print(s4)

# message = "伤情最是晚凉天，憔悴厮人不堪言"
# i = 0
# while i<len(message):
#     print(message[i])
#     i+=1

# message = "伤情最是晚凉天，憔悴厮人不堪言"
# i=0
# for i in range(0,len(message)):
#     print(message[i])
#     i+=1
# message = "伤情最是晚凉天，憔悴厮人不堪言"
# i=len(message)-1
# print(message[i])
# print("*****************")
# # print(len(message))
# # print(message[i])
# for i in range(len(message)):
#     print(i)
#     print(message[i])
#     i+=1
#     print(i)
"""
要求：
	将num1中的的所有数字找到并拼接起来：1232312
	将num1中的的所有数字找到并拼接起来：1218323
	然后将两个数字进行相加。
"""
num1 = input("请输入：") # asdfd123sf2312
num2 = input("请输入：") # a12dfd183sf23
# 请补充代码
len_num1 = len(num1)
len_num2 = len(num2)
char = 0
str_num1 = ""
str_num2 = ""
for char in range(len_num1):
    if num1[char].isdecimal():
        str_num1=str_num1+num1[char]
        # print(str_num1)
    char+=1
print(str_num1)
for char in range(len_num2):
    if num2[char].isdecimal():
        str_num2=str_num2+num2[char]
        # print(str_num1)
    char+=1
print(str_num2)
int_num1 = int(str_num1)
int_num2 = int(str_num2)
print(int_num1+int_num2)