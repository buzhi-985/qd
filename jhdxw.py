# -- coding: utf-8 --
# @time : 2023/7/28 12:11
# @author : 不知
# @email : buzhi985@qq.com
# @file : 交汇点新闻.py
# @software: pycharm
# cron: 30 6 * * *
# new Env('交汇点新闻');

import time
import requests
import random
from os import environ

ck = environ.get("jhdCK") if environ.get("jhdCK") else ""
headers = {
    "Cookie": ck,
    "User-Agent": "jiao hui dian xin wen/8.0.49 (iPhone; iOS 15.0; Scale/2.00)",
    "Accept-Language": "en-CN;q=1, zh-Hans-CN;q=0.9, zh-Hant-CN;q=0.8",
}


def sigin():
    url = "https://japi.xhby.net/v4/api/have_signin?" \
          "token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC8xMjcuMC4wLjE6ODA5MVwvdjRcL2FwaVwvcXVlcnlTZW5kRGV0YWlsc1JlZ2lzdGVyIiwiaWF0IjoxNjc2MTA4NjczLCJleHAiOjEzNzcyMTA4NjczLCJuYmYiOjE2NzYxMDg2NzMsImp0aSI6InpsanB5QVM2NWlhaW41akciLCJzdWIiOiIxNzJhNGVhMmUxMmI0YTAxYjdmNTEyYjA0MTQ0ZmUzYiIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.bBMD5EAdzdHkXA3Ya-VXzRwao3NL4wJjNrqfjrlIUmQ"
    rep = requests.get(url, headers=headers).json()
    print(rep["data"]["user_score"])


def parise(aid):
    # aid = "Y2U9p8ifOXUkmQ2x"
    url = f"https://japi.xhby.net/v4/api/praise/{aid}"
    data = {
        "id": aid,
        "praise": "1",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC8xMjcuMC4wLjE6ODA5MVwvdjRcL2FwaVwvcXVlcnlTZW5kRGV0YWlsc1JlZ2lzdGVyIiwiaWF0IjoxNjc2MTA4NjczLCJleHAiOjEzNzcyMTA4NjczLCJuYmYiOjE2NzYxMDg2NzMsImp0aSI6InpsanB5QVM2NWlhaW41akciLCJzdWIiOiIxNzJhNGVhMmUxMmI0YTAxYjdmNTEyYjA0MTQ0ZmUzYiIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.bBMD5EAdzdHkXA3Ya-VXzRwao3NL4wJjNrqfjrlIUmQ",
        "type": "1"
    }
    rep = requests.post(url, data=data, headers=headers).json()
    if rep['code'] == 200:
        print(f"{aid}点赞成功")


def comment(aid):
    url = f"https://japi.xhby.net/v4/api/article/{aid}/comments"
    comment_list = ["中国共产党万岁", "人民万岁", "我将无我，不负人民", "魅力中国", "美丽中国", "牢记使命，砥砺前行", "又学到知识啦", "开拓眼界了", "意味深长，值得深思"]
    a = random.randint(0, 9)
    data = {
        "content": comment_list[a],
        # "latitude":"0.000000",
        # "location":"",
        # "longitude":"0.000000",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC8xMjcuMC4wLjE6ODA5MVwvdjRcL2FwaVwvcXVlcnlTZW5kRGV0YWlsc1JlZ2lzdGVyIiwiaWF0IjoxNjc2MTA4NjczLCJleHAiOjEzNzcyMTA4NjczLCJuYmYiOjE2NzYxMDg2NzMsImp0aSI6InpsanB5QVM2NWlhaW41akciLCJzdWIiOiIxNzJhNGVhMmUxMmI0YTAxYjdmNTEyYjA0MTQ0ZmUzYiIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.bBMD5EAdzdHkXA3Ya-VXzRwao3NL4wJjNrqfjrlIUmQ"
    }
    rep = requests.post(url, headers=headers, data=data).json()
    print(rep["msg"])
    pass


def getaid():
    i = 0
    comment_ci = 0
    for j in range(2):
        c_id = random.randint(9, 12)
        if c_id == 11:
            c_id = 12
        p_num = random.randint(1, 40)
        url = f"https://japi.xhby.net/v4/api/articles?column_id={c_id}&page={p_num}"
        rep = requests.get(url, headers=headers).json()["data"]["article"]["data"]

        for it in rep:
            parise(it["id"])
            time.sleep(1)
            if comment_ci < 6:
                comment(it["id"])
                time.sleep(1)
                share(it["id"])
                comment_ci += 1
            i += 1
            if i == 30:
                break
            time.sleep(1)


def share(aid):
    url = "https://japi.xhby.net/v3/api/share_score"
    data = {
        "id": aid,
        "shareOS": "ios",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC8xMjcuMC4wLjE6ODA5MVwvdjRcL2FwaVwvcXVlcnlTZW5kRGV0YWlsc1JlZ2lzdGVyIiwiaWF0IjoxNjc2MTA4NjczLCJleHAiOjEzNzcyMTA4NjczLCJuYmYiOjE2NzYxMDg2NzMsImp0aSI6InpsanB5QVM2NWlhaW41akciLCJzdWIiOiIxNzJhNGVhMmUxMmI0YTAxYjdmNTEyYjA0MTQ0ZmUzYiIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.bBMD5EAdzdHkXA3Ya-VXzRwao3NL4wJjNrqfjrlIUmQ"
    }
    rep = requests.post(url, headers=headers, data=data).json()
    if rep["code"] == 200:
        print("分享成功")


if __name__ == '__main__':
    if ck=="":
        pass
    else:
        sigin()
        getaid()
        sigin()
