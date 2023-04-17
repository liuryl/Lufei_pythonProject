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

