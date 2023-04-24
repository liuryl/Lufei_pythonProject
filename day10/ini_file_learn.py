import configparser

config = configparser.ConfigParser()
config.read('my.ini',encoding='utf-8')

# # 获取所有的节点
# result = config.sections()
# print(result)
# # 获取节点下所有的值
# result = config.items('mysqld_safe')
# print(result)
# for key,value in config.items('mysqld_safe'):
#     print(key,value)

# 获取某个节点下的键对应值
# result = config.get('mysqld','collation-server')
# print(result)

#其他功能
# 判断是否存在
# v1 = config.has_section('client')
# print(v1)
# 添加节点
# config.add_section('group')
# 添加节点并设置值
# config.set('group','name','wupeiqi')
# config.write(open('my.ini',mode='w',encoding='utf-8'))

# delet
# 删除节点
config.remove_section('client')
# 删除节点中内容
config.remove_option('mysqld','datadir')
config.write(open('my.ini',mode='w',encoding='utf-8'))