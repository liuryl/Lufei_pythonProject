import re

text = '你好wupeiqi，阿烤豆腐北京啊的wupeiqi拉峻粉丝弄v哦时；阿vi；；oanvosnvwupeiqi'
data_list = re.findall('wupeiqi', text)
print(data_list)
