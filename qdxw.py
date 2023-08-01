# -- coding: utf-8 --
# @time : 2023/7/28 10:22
# @author : 不知
# @email : buzhi985@qq.com
# @file : main.py
# @software: pycharm
import requests

headers = {
    # "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "appnews_deviceInfo=YTo1OntzOjEyOiJtYWNoaW5lX2NvZGUiO3M6MzY6IjIxMzA2MDY1LUEyODgtNDc1RC1BODI2LTVCMDJGREUzNUVGMiI7czo3OiJ1c2VyX2lkIjtzOjg6IjExNzY3OTY4IjtzOjk6InVzZXJfdHlwZSI7aToxO3M6OToidF91c2VyX2lkIjtzOjg6IjEzNzcxNzM0IjtzOjk6InR5cGVfdGVzdCI7czozOiJhcGkiO30%3D; sto-id-20480-appnews_pool=KODCAKAKFAAA; password=oK7EsToaMb0O%2FozNAxs81OySVXKcY5rI; token=oK7EsToaMb0O%2FozNAxs81OySVXKcY5rI; uid=11767968; username=CsyD6trt7wNwCdTH5J83KEXhEkQfGMQQ; PHPSESSID=63e9ba331733f0.66631615:",
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
    siginin()
    drawlottery()

