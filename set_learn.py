# v1 = {'alex','武sir','肖大'}
# v2 = []
#
# # 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
# judge = True
# while judge:
#     your_enter = input("please input your name")
#     if your_enter=='N'or your_enter=='n':
#         print("break")
#         break
#     elif your_enter in v1:
#         v2.append(your_enter)
#     elif your_enter not in v1:
#         v1.add(your_enter)
# print(v1)
# print(v2)

# 模拟用户信息录入程序，已录入则不再创建。
user_info = set()
while True:
    name = input("please enter name")
    age = input("please enter age")
    item = (name,age)
    if item=="":
        continue
    if item in user_info:
        print("error,the user in data")
    else:
        user_info.add(item)
