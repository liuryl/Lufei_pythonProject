# from xml.etree import ElementTree as ET
#
# # 使用ET打开xml文件
# tree = ET.parse('xm.xml')
# # 获取跟节点
# root = tree.getroot()
# print(root)

# 读取节点数据
# 获取跟标签的孩子标签
# for child in root:
#     # child.tag获取标签
#     # child.attrib获取属性
#     print(child.tag, child.attrib)
#     for nod in child:
#         print(nod.tag, nod.attrib, nod.text)

# 使用find找到标签
# contry_object = root.find('country')
# print(contry_object.tag, contry_object.attrib)
# gdppc_object = contry_object.find('gdppc')
# print(gdppc_object.tag, gdppc_object.attrib, gdppc_object.text)

# 修改节点内容和属性
# rank=root.find('country').find('rank')
# print(rank.text)
# rank.text='999'
# rank.set('update','2020-11-11')
# print(rank.text,rank.attrib)
# # 保存文件
# tree = ET.ElementTree(root)
# tree.write('new.xml',encoding='utf-8')

# delet
# root.remove(root.find('country'))
# print(root.findall('country'))
# tree=ET.ElementTree(root)
# tree.write('newnew.xml',encoding='utf-8')
#
# import os
# from xml.etree import ElementTree as ET
#
# # 创建跟标签
# root = ET.Element("home")
#
# # 创建节点大儿子
# son1 = ET.Element('son', {'name': '儿1'})
# # 创建小儿
# son2 = ET.Element('son2', {'name': '儿2'})
#
# # 在大儿子中创建两个孙子
# grandson1 = ET.Element('grandson', {'name': 'er11'})
# grandson2 = ET.Element('grangdson', {'name': 'er12'})
# son1.append(grandson1)
# son1.append(grandson2)
#
# # 将儿子添加到跟节点中
# root.append(son1)
# root.append(son2)
#
#
# tree = ET.ElementTree(root)
#
# if not os.path.exists('files'):
#     os.makedirs('files')
# tree.write('files/ooo.xml',encoding='utf-8',short_empty_elements=False)

#
# from xml.etree import ElementTree as ET
#
# # 创建跟节点
# root = ET.Element("family")
#
# # 创建子节点
# son1 = root.makeelement('son', {'name': 'son_1'})
#
# son2 = root.makeelement('son', {'name': 'son_2'})
# # 创建孙子节点
# grandson1 = son1.makeelement('grandson', {'name': 'grand_son_1'})
# grandson2 = son1.makeelement('grandson', {'name': 'grand_son_2'})
#
# son1.append(grandson1)
# son1.append(grandson2)
#
# # 将儿子节点添加到root
# root.append(son2)
# root.append(son1)
#
# tree = ET.ElementTree(root)
# tree.write('files/oooo.xml', encoding='utf-8')


# from xml.etree import ElementTree as ET
#
# root = ET.Element('family')
#
# son1 = ET.SubElement(root, 'son', attrib={'name': 'son_1'})
# son2 = ET.SubElement(root, 'son', attrib={'name': 'son_2'})
#
# grandson = ET.SubElement(son1, 'age', attrib={'name': 'grand_son1'})
# grandson.text = 'grandsonson'
#
# et = ET.ElementTree(root)
# et.write('files/test.xml', encoding='utf-8')



from xml.etree import ElementTree as ET

root=ET.Element('user')
root.text='<![CDATA[hello]]'

et = ET.ElementTree(root)
et.write('files/tx.xml',encoding='utf-8')