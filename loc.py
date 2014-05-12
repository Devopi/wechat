#-*- coding:utf-8 -*-

import web
import time
import wechat
import gettitle

#import bingq

import simple

from settings import token
from settings import apiurl

urls = (
    apiurl, 'api',
    '/(.*)', 'index'
)

class api:

    def POST(self):
        hove=wechat.wechat(web.data())
        if hove.MsgType=='text':
            if hove.Content=='time':
                return hove.text(time.asctime())
            elif hove.Content[:6]=='title ':
                return hove.text(gettitle.gettitle(hove.Content[6:]))
#            elif hove.Content[:7]=='search ' :
#                return bingq.search(hove.Content[7:])
            return hove.text(simple.resp(hove.Content))
        elif hove.MsgType=='event' and hove.Event=='subscribe' :
            return hove.text('hello!')
        

    def GET(self):
        args=web.input()
        try:
            if wechat.checksign(args.timestamp, args.nonce, token ,args.signature)==True:
                return args.echostr
        except :
                raise web.seeother('/')

class index:
    def GET(self ,name):
        return wechat.kpass()

app = web.application(urls, globals()).wsgifunc()

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)

