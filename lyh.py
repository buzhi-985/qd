# -- coding: utf-8 --
# @time : 2023/8/2 10:59
# @author : 不知
# @email : buzhi985@qq.com
# @file : lyh.py辽友会
# @software: pycharm
# cron: 30 8 * * *
# new Env('辽友会');
import datetime
from os import environ

import requests
from tools.tool import timestamp
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
req = requests.session()
"""
换acesstoken和cookies，中间以@隔开
"""
CK = environ.get("lyhCK") if environ.get("lyhCK") else ""
headers = {
    'Accept': "*/*",
    'Accept-Encoding': 'gzip, deflate, br',
    "Content-Type": "application/json",  # 需要
    'accesstoken': str(CK.split("@")[0]),
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/4G Language/zh_CN miniProgram/wx7b8d2f8c69ac139e',
    'Cookie': str(CK.split("@")[1])
}


# 每周会员中心
def week():
    url = "https://lyh.lncmcc.com/zt-portal/lnlyh/portal/app/api/v1/member1018/13378e9d313c35247235d239a0cd10ef/89bef18245155c4c180f212222178881"
    data = {"meta": {"time": datetime.datetime.utcnow().strftime("%Y-%m-%dT%T.002Z"),
                     "devid": "89bef18245155c4c180f212222178881", "cliver": "ios@1.0.0@ios",
                     "reqsn": "89bef18245155c4c180f212222178881", "lang": "zh_CN"}, "data": {"chanId": "xcx"}}
    res = req.post(url, headers=headers, json=data).json()
    print(res)


# 每月信息中心
def month():
    url = "https://lyh.lncmcc.com/zt-portal/lnlyh/portal/app/api/v1/marketplate1001/13378e9d313c35247235d239a0cd10ef/3d85d603f11c7f10a22dda5afcec817b"
    data = {"meta": {"time": datetime.datetime.utcnow().strftime("%Y-%m-%dT%T.002Z"),
                     "devid": "3d85d603f11c7f10a22dda5afcec817b",
                     "cliver": "ios@1.0.0@ios", "reqsn": "3d85d603f11c7f10a22dda5afcec817b", "lang": "zh_CN"},
            "data": {"taskCode": "EVERY_MONTH_LOOK_MESSAGE", "chanId": "xcx"}}
    res = req.post(url, headers=headers, json=data).json()
    print(res)
    # 每月礼券
    url = "https://h5pro.lncmcc.com/ln_giftcard/index/ling_one"
    data = {
        "islogin": "047c24cb6a34aecac5661640e6919b5116ecd66399097f0ffad8ec15f21572127126c67150758e9d833b9f46e4a4bb611a02a022ae7ab10c925efc97cef3a6ee240f543237780fe5c5f4c9696ccdf21ee97feecd12c8bfd280a37473ddc9836a9266a6fe388527e23a0981fcabed855669997bfa8b8dbda2"
    }
    headers1 = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        # X-Requested-With: XMLHttpRequest
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://h5pro.lncmcc.com",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/WIFI Language/en miniProgram/wx7b8d2f8c69ac139e",
        # Connection: keep-alive
        "Referer": "https://h5pro.lncmcc.com/ln_giftcard/%20%20?pc=nf1GCzV3%2FHc4LIFO%2F2sVryDG%2BWB6zLrY27EhOX0%2FD04dgeY3htDsMY5kMAkMcrZIlsCSifIZdvma%0AKdkGRBuIdx6bH8DwrRquybO1dT3uJvm64Chv5FNbsyuBKkRP0tJeTV8At%2Bz7SlqCW9w0HK6d%2Fo77%0A%2F%2FXTTuy93IBrOIlzZJBPo2mwzEbn5O1LwZRCA5K0nzLDA5qhZrMvC%2FWmZV%2BE3o7rYo5yuxB35B7f%0APKbpJIYmi%2FXAvQWZtuzwuFq0lrins8QD0N0Vlt3WLmbCkGl4k%2F0apTSC20jzScL1JPlJBmkerxJ6%0A0nC44O41FF%2BwXPtp%2B28m6VhFAgcN9q%2BdpTINhjlWULxznEe%2BrcS%2FID4brdgdzWBLhRNni084XCEi%0Ad7MJkFL6Jm87wLpJekHvrjSuI74S1y7u8Pey%2BxH9pKwdQOIzLfY73vhwIjY4gXMu%2FhyJBlYFy9L9%0AusdQY3w%2BMZNxlICPmfsM7N%2BvIA7897iLBOp%2FoVojmSpA7w2jC%2FBRIkUyJuaaYGfuEC0HJ10rx06O%0AMwnjc5esx2E0yAale%2FCKH6ehcoN9oc4Rs%2FuJgqcaGzUWyrTVyOWxgdfscgjbhHizvMyjec0oADHX%0A8yaHXMxA0gEDnGoTF7NSwVCyxmJZPKclmIFcrRxVST6wZ5Xl%2BggIlZpwDyZeqJ8hk7bp%2BhV90YU3%0AtjsWhry%2FhkUm8LthoDCcv5p0QF2iQOzNycFeVeKkZjs3pGF04WUGoDOUgmcdLNSZSBweRKLrTK1k%0AMPU8rVIxLr98lnd73VHNDkLrwV%2FukcZ%2Fngjr6DVHl1FygNOwc2bws0XXKC1fpM3RlBUyWm4Wrse2%0AEyyc5b8Xbd%2Bpj5QA8s62HvrNp8Feqn8Kxi1AyEjzZLurPEB7VaijumZ1%2BRmJ5sJMenTFWMSF1W4l%0ABhRlBysMnODW53kXplOQj9RM0yWXHe2OlZQIgvtY0yKc%2FGFhh0CsFb9vfFIngVQ9jaUcvtMb2dV6%0AQ%2F298x6lYI1eVJ%2BgHycheNBmxzM%2B8Y5fHP3WvzE6y0KmlR%2BvWz25FQT6SQ%3D%3D&pk=6ED53382CD378751CFD0868698FA728E632C517A594A97BDF6CACD61EF8B8C4E8637376C98B9690B955060C7F73AE6032ABA7B790B16CE8F43CCCCFF55E4F052F01D21206B064B5BE4093E8817B3B6803E305CE4E0BAABB006805114C6C87F0491918156CC809C37B689C10F2D6DFDD71751A87E49BBDAADDD9AEF82FD7049C9&_sid_=5e4f6282-4dbe-4e5b-a533-72ce8ac15c62",
        # Content-Length: 248
        "Cookie": "LN_STATIS_HAOHAN_0_USER_COOKIE_ID=79b26df1-99a6-4b8b-b159-388c6d42f783; LN_STATIS_HAOHAN_105018_USER_COOKIE_ID=5aba629d-4da7-4c36-9b91-71238386cdb9; K_LN_GIFTCARD_OCH_LOGINREQUEST=DerYrxubwTg2dBjdx761wYd6qbC%2FJJwvsnw6wvX6cUDpb1Zw0TYxsi6zt1MyPXraJy1y1%2FZxUHJnUSfkzhZz3wZiM6QjzJlHEXBdStoAP3VPQ%2BjRcuFy6kzLsFZyuwZ3qOByd6Ut1bAJr5oehg9ikXVSN36hFirNnxB9C1bm7UdIH9%2FMrh1bWMW%2FoTQpbamR%2BzBvwXU3p5tqdjknxNbVV0zmD1KJeY923w3kOpfRFTy0Dz3eSxBQ4HBbbRlQ1WFASZjbfg2r6%2BMkpVObc8KzZDlueimQsKGyDF8tz8HieuoctF3pIqLlNW83XNsiw7rhFQeZzF%2B5j4L742Lc56cDX77FgrkLViPv7uHG2rk4IoSExcwAp%2FSe%2BEwnXVQpACyJDqSfiWDiSMbUskJAid0chNNNjOpVqNbzPZecNA%2B89coODN2shiAEZ1nVr%2FKgAd%2FZ6qO5JDlKNKfLSWKNXlLNuf2e2UGxDVYWFvMzWAocSbTq1sH6SZXnmDDxyugciMjdywOxmieGpbLtKoA%2B%2BqXGbuknVTIlTO9WvR4sOvZV2pu1F%2BjPS6BuVLXXCNNg%2BiEIpPpIC97SnHES2bNMPZyToVzvSimcmzgj%2BvprfuZw3AepQYa3RTo%2FUktVkyzgE8i2xrlWGRzSxZrjeKxF3koOJizrlQwMi4H0Ca25l18Ke3L0iKwYmXESZ03%2BzzZI7e9obRh5qCzdapbiJK1ZuJoTLq1VtzS%2BipQEP%2FLyd2Hb2iyVkKR9%2B0ts3PzCFrGPi0fuPH29%2BMRSiUmY1ogwibkhHa15B%2Bt1GraeczO9lkmWfAWiJPM9iEOB5dlzYDTHWcQoPQ%2BPBJH3aMgS93usk4UnvQ%3D%3D; K_LN_GIFTCARD_OCH_SID=GH0B4txsnwpcy2MqrEOwUBbnzRopljU0Aw8cYQecIGB8kOSdVd%2F8rfFAz8S02u06"
    }
    res = req.post(url, headers=headers1, data=data).json()
    print(res)
    # 每月流量嗨翻天
    url = "https://lyh.lncmcc.com/huodong-portal/lnlyh/lljfAct/dotask?actNo=lljf0419&wechatParams=AsPVTE1iK8WAQQk0MiTxn5togifBJHkCQmidBf1qq0LbdKOXhpRxejihE51yOW0O8I3Lnn-TkjsGrtcy0YQkEbMH8-HZLsClP7oMixcKU8jFXpBGgdHGINybW_Zv11kCCvTZJ5oWIe8_PcjXLAckSiCCIe6LVLUQNUEAFl7cZXnvMNgRIT_vZ7_bm8A2muekBZtBGoq-Eq-n3jDQWrDJnJH2Ziv0XKzRO0EMSMyTeUWN67CYn-Pq4sxnDrzWYNzlR_xKWTCyr-BrZ9YXNtMUyDgr08UUgkWw88gjRN32ZId3zycqf2PP0OdBfjsHysw4EUxQtCDbDOQ-t1kMwIPFpeHLb6z3DccaOAppo_OWR5Wk8qf1_2NBkkIZYjHocw3W6heL00QpjzQ&_=1690946906775"
    headers1 = {
        "Cookie": "HDJSESSION=ZjJlYmEzYmYtMDFiOC00MDlkLWEyMjEtNjZiZjI5Zjk2Yjg4; LYH_HD_ORTAL=237_5015|ZMnNX|ZMnNP; LYH_PORTAL=227_5031|ZMnNO|ZMnL7; LYH_EDGE=236_5023|ZMm9V|ZMm9V",
        "Referer": "https://lyh.lncmcc.com/huodong-portal/lnlyh/static/html/newlljf/llhft/schedule.html?actNo=lljf0419&wechatParams=AsPVTE1iK8WAQQk0MiTxn5togifBJHkCQmidBf1qq0LbdKOXhpRxejihE51yOW0O8I3Lnn-TkjsGrtcy0YQkEbMH8-HZLsClP7oMixcKU8jFXpBGgdHGINybW_Zv11kCCvTZJ5oWIe8_PcjXLAckSiCCIe6LVLUQNUEAFl7cZXnvMNgRIT_vZ7_bm8A2muekBZtBGoq-Eq-n3jDQWrDJnJH2Ziv0XKzRO0EMSMyTeUWN67CYn-Pq4sxnDrzWYNzlR_xKWTCyr-BrZ9YXNtMUyDgr08UUgkWw88gjRN32ZId3zycqf2PP0OdBfjsHysw4EUxQtCDbDOQ-t1kMwIPFpeHLb6z3DccaOAppo_OWR5Wk8qf1_2NBkkIZYjHocw3W6heL00QpjzQ",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/WIFI Language/en miniProgram/wx7b8d2f8c69ac139e",
    }
    res = req.get(url, headers=headers1).json()
    print(res)
    # 每月浏览成长值
    url = "https://lyh.lncmcc.com/zt-portal/lnlyh/portal/app/api/v1/marketplate1001/13378e9d313c35247235d239a0cd10ef/03ac1965acf3e57d0b8b5f6b4de25120"
    data = {"meta": {"time": datetime.datetime.utcnow().strftime("%Y-%m-%dT%T.002Z"),
                     "devid": "03ac1965acf3e57d0b8b5f6b4de25120", "cliver": "ios@1.0.0@ios",
                     "reqsn": "03ac1965acf3e57d0b8b5f6b4de25120", "lang": "zh_CN"},
            "data": {"taskCode": "EVERY_MONTH_LOOK_GROW", "chanId": "xcx"}}
    res = req.post(url, headers=headers, json=data).json()
    print(res)
    # 每月浏览辽豆
    url = "https://lyh.lncmcc.com/zt-portal/lnlyh/portal/app/api/v1/marketplate1001/13378e9d313c35247235d239a0cd10ef/78ca21e75856844a7ac7073dd17c1bd5"
    data = {"meta": {"time": datetime.datetime.utcnow().strftime("%Y-%m-%dT%T.002Z"),
                     "devid": "78ca21e75856844a7ac7073dd17c1bd5", "cliver": "ios@1.0.0@ios",
                     "reqsn": "78ca21e75856844a7ac7073dd17c1bd5", "lang": "zh_CN"},
            "data": {"taskCode": "EVERY_MONTH_LOOK_BEAN", "chanId": "xcx"}}
    res = req.post(url, headers=headers, json=data).json()
    print(res)


def test():
    # 每日签到
    url = "https://lyh.lncmcc.com/huodong-portal/lnlyh/familysignin/sign?actNo=sign01" \
          "&wechatParams=AsPVTE1iK8WAQQk0MiTxn5togifBJHkCQmidBf1qq0LbdKOXhpRxejihE51yOW0O8I3Lnn-TkjsGrtcy0YQkEbMH8-HZLsClP7oMixcKU8jFXpBGgdHGINybW_Zv11kCCvTZJ5oWIe8_PcjXLAckSiCCIe6LVLUQNUEAFl7cZXnvMNgRIT_vZ7_bm8A2muekBZtBGoq-Eq-n3jDQWrDJnJH2Ziv0XKzRO0EMSMyTeUWN67CYn-Pq4sxnDrzWYNzlR_xKWTCyr-BrZ9YXNtMUyDgr08UUgkWw88gjRN32ZId3zycqf2PP0OdBfjsHysw4EUxQtCDbDOQ-t1kMwIPFpeHLb6z3DccaOAppo_OWR5Wk8qf1_2NBkkIZYjHocw3W6heL00QpjzQ" \
          "&shopId=" \
          f"&_={timestamp()}"
    h1 = {
        "Cookie": "HDJSESSION=ZDM3MGM0ZmYtNWUyZi00ODUxLTllZjgtNmZmMDY4Mzg5NGVh; LYH_HD_ORTAL=230_5012|ZMnz0|ZMnzy; LYH_EDGE=229_5024|ZMnzz|ZMnzx; LYH_PORTAL=226_5033|ZMnzq|ZMnzT",
        "Referer": "https://lyh.lncmcc.com/huodong-portal/lnlyh/static/html/familySign/signIn.html?actNo=sign01&pSource=JGG%2C2%2C2-3&sourceAdvertPosAr=xcx_index&_s=xcx&wechatParams=AsPVTE1iK8WAQQk0MiTxn5togifBJHkCQmidBf1qq0LbdKOXhpRxejihE51yOW0O8I3Lnn-TkjsGrtcy0YQkEbMH8-HZLsClP7oMixcKU8jFXpBGgdHGINybW_Zv11kCCvTZJ5oWIe8_PcjXLAckSiCCIe6LVLUQNUEAFl7cZXnvMNgRIT_vZ7_bm8A2muekBZtBGoq-Eq-n3jDQWrDJnJH2Ziv0XKzRO0EMSMyTeUWN67CYn-Pq4sxnDrzWYNzlR_xKWTCyr-BrZ9YXNtMUyDgr08UUgkWw88gjRN32ZId3zycqf2PP0OdBfjsHysw4EUxQtCDbDOQ-t1kMwIPFpeHLb6z3DccaOAppo_OWR5Wk8qf1_2NBkkIZYjHocw3W6heL00QpjzQ&uid=13378e9d313c35247235d239a0cd10ef&oid=86cdd5cc99a3692e1fa8c19a6a8cb906a278904974c987359aa9903590b3493d&cmSessionId=258afe69cca39a0466d1a8023303d2ad",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.29(0x18001d38) NetType/WIFI Language/en miniProgram/wx7b8d2f8c69ac139e",
    }

    res = req.get(url, headers=h1).json()
    print(res)


if __name__ == '__main__':
    test()# 每日签到
    # 获取当前日期
    now = datetime.datetime.now()
    # 判断是否是每月第一天
    if now.day == 1:
        # 执行每月第一天的操作
        print("执行每月第一天的操作")
        month()
    # 判断是否是每周一
    if now.weekday() == 0:
        # 执行每周一的操作
        print("执行每周一的操作")
        week()


