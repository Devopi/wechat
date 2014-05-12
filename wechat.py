#-*- coding:utf-8 -*-

import hashlib
import time
from xml.dom import minidom


def kpass():
    return " "

def checksign(*arg1):
    if len(arg1) != 4:
        return False
    t=[arg1[0], arg1[1], arg1[2]]
    t.sort()
    if hashlib.new("sha1", (''.join(t))).hexdigest()==arg1[3]:
        return True
    else:
        return False

class wechat():
    def __init__(self, xmlstr):
        dom = minidom.parseString(xmlstr)
        root = dom.documentElement
        self.ToUserName=root.getElementsByTagName('ToUserName')[0].firstChild.data
        self.FromUserName=root.getElementsByTagName('FromUserName')[0].firstChild.data
        self.CreateTime=int(root.getElementsByTagName('CreateTime')[0].firstChild.data)
        self.MsgType=root.getElementsByTagName('MsgType')[0].firstChild.data
        if self.MsgType=='text' :
            self.Content=root.getElementsByTagName('Content')[0].firstChild.data
        elif elf.MsgType=='event' :
            self.Event=root.getElementsByTagName('Event')[0].firstChild.data
        self.MsgId=int(root.getElementsByTagName('MsgId')[0].firstChild.data)

    def text(self, text):
        return '''<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%d</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
<FuncFlag>0</FuncFlag>
</xml>'''%(self.FromUserName, self.ToUserName, int(time.time()), text)


