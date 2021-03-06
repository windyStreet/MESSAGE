#!/usr/bin/env python
# !-*- coding:utf-8 -*-

from bin.logic.func import Mail_func
from bin.until import PR

MSG_CODE_TYPE = 1

class Smtp_logic(object):
    def __init__(self):
        pass

    '''
        @author:wuqiang
        @time:2017年8月7日15:26:27
        @version:V0.1.0
        @func:"发送邮件信息"
        @param:data:{
            "from":"yaogc@longrise.com.cn" （able null,发件地址）string
            "to":["yaogc@longrise.com.cn"，"wuqiang@longrise.com.cn"]（not null,收件人列表）string[]
            "tile":"邮件主题"（default  “no title”）string
            "content":"邮件内容"（default “no content”）string
            "type":"发送邮件类型"（able null [open-falcon,devops ] ）string[]
            "xxx":{
                "yy":"abc"
            }()
        } json #(not null)
        @notice:""
        @PR:{
            "code": code
            "msg":msg
            "result":None
        }
        @return:PR
    '''

    def send_msg(self,data):
        data = None
        Mail_func.getInstance().send_mail(data)
        return PR

'''
        @author:wuqiang,windyStreet
        @time:2017年8月7日10:14:09
        @version:V0.1.0
        @func:""
        @param:data:{
            "A":"a",# string 用于判定
        } json #(able null)
        @param:xxx:"xxx用于区别发信息的类型"（
                                1、xxx=1，发邮件;
                                2、xxx=2，发微信;
                                3、xxx=5，发邮件和短信
                                ）
                                string （# not null）
        @notice:""
        @return:instance
'''
def getInstance():
    return Smtp_logic()