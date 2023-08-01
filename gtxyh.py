# -- coding: utf-8 --
# @time : 2023/8/1 16:37
# @author : 不知
# @email : buzhi985@qq.com
# @file : gtxyh.py
# @software: pycharm
# 公众号 ： 骁友会 https://qualcomm.growthideadata.com/qualcomm-app/api/user/info
# cron: 40 6 * * *
# new Env('骁友会');
import random
import time

import requests

headers = {
    "userId": "1214202",
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "sessionKey": "7l/lz5X2u+g9+fKXZbmXQQ==",
    "openId": "o2jYV5YwiTsMzcuby9hjR5Vu-j7I",
    "timestamp": "1690878767337",
    "requestId": "f98d09ba1e5f4730946687ad0bb04d28",
    "sign": "4effbe41461da5708ec1bb1f0b6143a5",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/WIFI Language/en",
    "Referer": "https://servicewechat.com/wx026c06df6adc5d06/327/page-frame.html"
}


def signin():
    url = "https://qualcomm.growthideadata.com/qualcomm-app/api/user/signIn?userId=1214202"
    rep = requests.get(url,headers=headers).json()
    print(rep)

def luckdraw():
    url = "https://qualcomm.growthideadata.com/qualcomm-app/api/luckDraw/getLuck?userId=1214202&activityId=7"
    rep = requests.get(url,headers=headers).json()
    print(rep)

def artlike():
    i = random.randint(1,10)
    url = f"https://qualcomm.growthideadata.com/qualcomm-app/api/home/articles?page={i}&size=20&userId=1214202&type=0&searchDate=&articleShowPlace=%E9%AA%81%E5%8F%8B%E8%B5%84%E8%AE%AF%E5%88%97%E8%A1%A8%E9%A1%B5"
    # req = requests.session()
    rep = requests.get(url,headers=headers).json()
    artL = rep["data"]["articleList"]
    aid = artL[i]["id"]
    url = f"https://qualcomm.growthideadata.com/qualcomm-app/api/article/like?articleId={aid}&userId=1214202"
    rep = requests.get(url,headers=headers).json()
    print(rep)

def shareart():
    url = "https://qualcomm.growthideadata.com/qualcomm-app/api/article/shareDaily"
    data = {
        "articleId":"7947",
        "userId":"1214202"
    }
    rep = requests.post(url,headers=headers,data=data).json()
    print(rep)

def rankLi():
    """每月一次"""
    url="https://qualcomm.growthideadata.com/qualcomm-app/api/rankingMonthly/rankingList"
    data = {
        "userId":"1214202"
    }
    rep = requests.post(url,headers=headers,data=data).json()
    print(rep)

def readart():
    """
    每日阅读
    """
    url = "https://qualcomm.growthideadata.com/qualcomm-app/api/article/detail?articleId=7947&userId=1214202"
    req = requests.session()
    rep = req.get(url,headers=headers)
    url = "https://qualcomm.growthideadata.com/qualcomm-app/api/article/enterReadDaily"
    data = {
        "articleId":"7947",
        "userId":"1214202"
    }
    rep = req.post(url,headers=headers,data=data).json()
    print(rep)
    time.sleep(320)
    url = "https://qualcomm.growthideadata.com/qualcomm-app/api/article/exitReadDaily"
    rep = req.post(url,headers=headers,data=data).json()
    print(rep)

def readvideo():
    """
    每日看视频
    """
    url = "https://qualcomm.growthideadata.com/qualcomm-app/api/article/detail?articleId=7884&userId=1214202"
    req = requests.session()
    rep = req.get(url, headers=headers)
    url ="https://qualcomm.growthideadata.com/qualcomm-app/api/sysConfig/detail"
    data = {
        "propertyKey":"task_switch_DAILY_PLAY_VIDEO_5_MINUTES"
    }
    rep = req.post(url,headers=headers,data=data).json()
    print(rep)
    url = "https://qualcomm.growthideadata.com/qualcomm-app/api/article/enterReadDaily"
    data = {
        "articleId": "7884",
        "userId": "1214202"
    }
    rep = req.post(url, headers=headers, data=data).json()
    print(rep)
    time.sleep(320)
    url = "https://qualcomm.growthideadata.com/qualcomm-app/api/article/exitReadDaily"
    rep = req.post(url, headers=headers, data=data).json()
    print(rep)

if __name__ == '__main__':
    signin()
    luckdraw()
    artlike()
    shareart()
    readart()
    readvideo()
