#!/usr/bin/python
# -*- coding:utf-8 -*-

import random
import requests

def get_search_word():
    word_list = ['newdream','12306','火车票','新梦想软测教育']
    num = random.randint(0,len(word_list)-1)
    return word_list[num]

def random_int():
    randome_list = range(10,99)
    num = random.randint(0,len(randome_list)-1)
    return randome_list[num]

def random_Chinese():
    first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟", "常"]
    second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏", "峰", "磊", "雷", "文",
                   "明浩", "光", "超", "军", "达"]
    name = random.choice(first_name) + random.choice(second_name)
    return name

def s():
    print( '测试用例开始执行' )
def t():
    print('测试用例结束执行')

def s1(step_name):
    print( '测试步骤 [%s] 开始执行'%step_name )
def t1(step_name):
    print('测试步骤 [%s] 结束执行'%step_name)

def get_true():
    return None

def get_access_token():
    p_dict = {
        'grant_type': 'client_credential',
        'appid': 'wx55614004f367f8',
        'secret': '65515b46dd758dfdb09420bb7db2c67f'
    }
    try:
        response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token',
                                params=p_dict)
        token = response.json()['access_token']
    except KeyError as e:
        token = None
    return token

if __name__=='__main__':
    print( pos()  )
