# -- coding: utf-8 --
# @time : 2023/8/1 17:53
# @author : 不知
# @email : buzhi985@qq.com
# @file : hn.py 抓包：小程序:红牛能量俱乐部
# @software: pycharm
# cron: 50 6 * * *
# new Env('红牛');
import random
import requests

headers = {
    "content-type": "application/json;charset=UTF-8",
    "componentSend": "1",
    "HH-APP": "wx5549b5fa9842e321",
    "HH-VERSION": "0.1.55",

    "HH-FROM": "20230522308440",
    "appPublishType": "1",

    "HH-CI": "saas-wechat-app",
    "Authorization": "bearer ca81d101-f1c5-4bb6-b33c-1315d9dca182",

    "Accept-Encoding": "gzip,compress,br,deflate",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/WIFI Language/en",
    "Referer": "https://servicewechat.com/wx5549b5fa9842e321/25/page-frame.html"
}


def signin():
    url = "https://xiaodian.miyatech.com/api/coupon/auth/signIn"
    data = {"miniappId":197}
    rep = requests.post(url,headers=headers,json=data).json()
    print(rep)

if __name__ == '__main__':
    signin()
