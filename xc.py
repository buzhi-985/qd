"""
小程序:喜茶GO
域名：vip.heytea.com
请求头：Authorization:XXXXXXX
export xchd='XXXXXXX'

"""
# cron: 40 7 * * *
# new Env('喜茶签到');
from os import environ
import requests
# xchd = environ.get("xchd") if environ.get("xchd") else ""
xchd = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI3ODI3ODM4NiIsInVzZXJfbWFpbl9pZCI6OTUyMzIzMDUsImNoYW5uZWwiOiJXIiwic291cmNlIjoiYXBpIiwiaXNfZ3Vlc3QiOmZhbHNlLCJsYWJlbCI6ImNsaWVudDp3ZWFwcCIsImlhdCI6MTY5MDg3NzI1MywibmJmIjoxNjkwODc3MjUzLCJleHAiOjE2OTA5NjM2NTMsImlzcyI6ImhleXRlYSJ9.qoxIizZaMxYbOvmRk2pk0abT0UGqkq0z4qNda1sOYyc"
def qd():
  url= 'https://vip.heytea.com/api/service-member/vip/task/award/114'
  headers= {
    "Host": 'vip.heytea.com',
    "Connection": 'keep-alive',
    'X-version': '4.9.4',
    'GTM-Zone': 'GMT+8:00',
    'Accept-Language': 'zh-CN',
    "Authorization": xchd,
    "Client": '1',
    'Content-Type': 'application/json',
    "Region": '1',
    "Accept": 'application/prs.heytea.v1+json',
    "xweb_xhr": '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF',
    'X-client': 'weapp',
    "version": '4.9.4',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    "Referer": 'https://servicewechat.com/wx696a42df4f2456d3/825/page-frame.html',
    'Accept-Encoding': 'gzip, deflate',
  }
  rep = requests.post(url,headers=headers).json()
  print(rep)


if __name__=="__main__":
  qd()