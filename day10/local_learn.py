import os

# 打印脚本的路径
abss = os.path.abspath(__file__)
print(abss)

# 向上找一级目录
path = os.path.dirname(abss)
print(path)


# 总的地址
base_dir=os.path.dirname(os.path.abspath(__file__))
file_path=base_dir+"/my.ini"
print(file_path)

# 自动拼接
join_path=os.path.join(base_dir,'my.ini')
print(join_path)
# open('/Users/liuriyilang/PycharmProjects/Lufei_pythonProject/day10',mode='r',encoding='utf-8')
