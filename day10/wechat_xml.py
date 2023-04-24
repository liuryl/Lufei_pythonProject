# 按照一定格式解析xml内容
content = """<xml>
    <ToUserName><![CDATA[gh_7f083739789a]]></ToUserName>
    <FromUserName><![CDATA[oia2TjuEGTNoeX76QEjQNrcURxG8]]></FromUserName>
    <CreateTime>1395658920</CreateTime>
    <MsgType><![CDATA[event]]></MsgType>
    <Event><![CDATA[TEMPLATESENDJOBFINISH]]></Event> 
    <MsgID>200163836</MsgID>
    <Status><![CDATA[success]]></Status>
</xml>"""

from xml.etree import ElementTree as ET
info={}
root=ET.XML(content)
for  node in root:
    info[node.tag]=node.text
print(info)