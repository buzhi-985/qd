# -- coding: utf-8 --
# @time : 2023/7/28 10:22
# @author : 不知
# @email : buzhi985@qq.com
# @file : main.py
# @software: pycharm
# cron: 29 6 * * *
# new Env('青岛新闻');
import requests
from os import environ

ck = environ.get("qdxwCK") if environ.get("qdxwCK") else ""
headers = {
    # "Accept-Encoding": "gzip, deflate, br",
    "Cookie": ck,
    # "vtoken": "nXCCUL3uTSryiIVw1n7GdIX5maUkCNUEzFPEvUSXUPhtW6RLXre-3NzbK0iY7f5Q_hsTcKgjlTHDJOVgF0UE56cT8jdVmo8QEdcsxPrUYMJ5VpkHv7nnZCAB7l4MVFKyjq27QZnd60uUNhAHpZXq6O-c8Yl95VHFUuQQEUWcOcsayEueNKK1HriUgx3YSYAphxmhzEEJZD4bkfwxI6ARYjywvtn9DT-rK0eyS7u1o0AgGk9wqUgHxcEDFMEUrp8FJvtjoZj-bHHR8Qhox3rzBu--RjwsaiduskWzwpqnpwi1cUZRHRiZw8rhnxK_2GIAGP8sba3dXDC2bLWP9_bFzg",
    "User-Agent": "iPhone12,1(iOS/15.0) AliApp(qdnews/6.10.9) Weex/0.24.0 828x1792"
}

def siginin():
    url = "https://appnews.qingdaonews.com/api/user_signinday/thing"
    data={
        "sign":"XwyWtUryA3tK0-qnN30usCnabAPzhfNFov4pG5KP7zd38RdpYrF8JFRuCFA8lvh4qLgLucXDxU8ZUm6QDH2JtN1W2uLellbCP3MOaTch7d7VY_sAwEyLECM42rWTQ3MIyzpmJia2WIZ8smptat93ZxgR9WA-fQe89FdLuRu7fqQ-er-sBgK3yhIUtPPl_U5GixU-PhwhfJ0UjDSYAv_TTaHkEmZca1FLD7pa0WuaFVOCzpgk70Na4FnEm5XRhsA-rEl6cUmdqlKy_DkYUstA_Vd_hZjE-ainp6w8lC8kqulwHbFpg-3VFIVr_Mv7HaCeKdatUSOx8iz0mm81ysNXRw"
    }
    rep = requests.post(url,headers=headers,data=data).json()
    print(rep)

def drawlottery():
    detail_url = "https://appnews.qingdaonews.com/api/signin/detail?weexVersion=0.4.3"
    rep = requests.get(detail_url,headers=headers).json()["result"]["prize"]
    prize_list ={}
    for it in rep:
        prize_list[it["id"]]=it["name"]
    url = "https://appnews.qingdaonews.com/api/signin/lottery?weexVersion=0.4.3"
    for i in range(3):
        data = {
            "is_gold": "0",# 0为免费次数，1为花币抽奖，每天3次
        }
        rep = requests.post(url, headers=headers, data=data).json()
        print(prize_list[rep['result']["id"]])


if __name__ == '__main__':
    if ck=="":
        pass
    else:
        siginin()
        drawlottery()

