'''
阿里云盘签到
功能：自动签到，使用签到奖品，支持多账号（使用#或&分割token），支持青龙
到这里获取token：https://alist.nn.ci/zh/guide/drivers/aliyundrive.html
更新：23.07
'''
# cron: 29 7 * * *
# new Env('阿里云签到');
import re
import requests
from os import environ, system, path
from sys import exit
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def load_send():
    global send, mg
    cur_path = path.abspath(path.dirname(__file__))
    if path.exists(cur_path + "/notify.py"):
        try:
            from notify import send
            print("加载通知服务成功！")
        except:
            send = False
            print("加载通知服务失败~")
    else:
        send = False
        print("加载通知服务失败~")

load_send()
send_msg = ''
def Log(cont):
    global send_msg
    print(cont)
    send_msg += f'{cont}\n'

class AliDrive_CheckIn:
    def __init__(self, refresh_token, is_reward):
        self.userAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 D/C501C6D2-FAF6-4DA8-B65B-7B8B392901EB"
        self.aliYunPanToken = ''
        self.aliYunPanRefreshToken = ''
        self.refresh_token = refresh_token
        self.msg = ''
        self.user_name = ''
        self.is_reward = is_reward
        self.headers= {
            "Content-Type": "application/json",
            "charset": "utf-8",
            "User-Agent" : self.userAgent
        }
    def getToken(self,indx):
        Log(f"\n开始执行第{indx + 1}个账号--------------->>>>>")

        url = 'https://auth.aliyundrive.com/v2/account/token'
        body = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }
        response = requests.post(url, headers=self.headers, json=body,verify = False)
        try:
            resp = response.json()
            # print(resp)
            if resp.get('code') == 'InvalidParameter.RefreshToken':
                # print('RefreshToken 有误请检查！')
                Log('\nRefreshToken 有误请检查！(可能token失效了，到这里获取https://alist.nn.ci/zh/guide/drivers/aliyundrive.html)\n')
                return self.msg
            else:
                self.aliYunPanToken = f'Bearer {resp["access_token"]}'
                # print(self.aliYunPanToken)
                self.aliYunPanRefreshToken = resp["refresh_token"]
                # print(self.aliYunPanRefreshToken)
                self.user_name = resp["user_name"]
                # print(self.aliYunPanToken)
                # print(self.aliYunPanRefreshToken)
                # print("获取token成功，开始执行签到！")
                self.headers['Authorization'] = self.aliYunPanToken
                Log(f">账号：【{self.user_name}】\n>获取token成功")
                self.CheckIn()

        except:
            # pass
            # print(response.json()["access_token"])
            print(response.text)

    def CheckIn(self):

        sign_url = 'https://member.aliyundrive.com/v1/activity/sign_in_list?_rx-s=mobile}'

        sign_body = {'isReward': False}
        sign_res = requests.post(sign_url, headers=self.headers, json=sign_body,verify = False)
        # print(sign_res.text)
        try:
            sign_resp = sign_res.json()
            # print(sign_resp)
            result = sign_resp['result']
            self.signInCount = result['signInCount']
            isReward = result['isReward']
            if isReward == True:
                Log(f'>签到成功！\n>已累计签到{self.signInCount}天！')

            else:
                Log(f'>今日已签到！\n>已累计签到{self.signInCount}天！')
            # signInLogs = sign_resp['result']['signInLogs']
            self.reward()
            self.join_team()
            self.use_signCard()
        except:
            print(sign_res)
            # self.msg+=sign_res

    def reward(self):
        reward_data = {"signInDay": self.signInCount}
        response = requests.post('https://member.aliyundrive.com/v1/activity/sign_in_reward?_rx-s=mobile',headers=self.headers, json=reward_data,verify = False)
        try:
            resp = response.json()
            if resp['result'] != 'null':
                Log(f">{resp['result']['notice']}")
        except:
            print(response.text)
    
    def join_team(self):
        check_team_data = {}
        check_team_res = requests.post('https://member.aliyundrive.com/v1/activity/sign_in_team?_rx-s=mobile',headers=self.headers, json=check_team_data,verify = False)
        try:
            resp = check_team_res.json()
            if resp['result'] != 'null':
                act_id = resp['result']['id']
                join_team_data = {"id": act_id, "team": "blue"}
                join_team_res = requests.post('https://member.aliyundrive.com/v1/activity/sign_in_team_pk?_rx-s=mobile',headers=self.headers, json=join_team_data,verify = False)
                try:
                    join_team_res = join_team_res.json()
                    if join_team_res['success']:
                        Log('>加入蓝色战队成功!')
                except:
                    print(join_team_res.text)
        except:
            print(check_team_res.text)


    def use_signCard(self):
        use_signCard_data = {}
        use_signCard_res = requests.post('https://member.aliyundrive.com/v1/activity/complement_sign_in?_rx-s=mobile',headers=self.headers, json=use_signCard_data,verify = False)
        try:
            resp = use_signCard_res.json()
            if resp['code'] != 'BadRequest':
                Log('>补签成功！')
            else:
                Log(f">补签失败！原因：{resp['message']}")
        except:
            print(use_signCard_res.text)



if __name__ == '__main__':
    refresh_token = ''
    ali_ck = environ.get("ALYP") if environ.get("ALYP") else refresh_token
    print(environ.get("ALYP"))
    if ali_ck == "":
        print("未填写 ALYP变量 青龙可在环境变量设置 ALYP 或者在本脚本文件上方将获取到的refresh_token填入refresh_token中")
        exit(0)
    ali_reward = True
    is_reward = environ.get("ali_reward") if environ.get("ali_reward") else ali_reward
    if is_reward:
        # msg += '检测到设置了自动使用奖品\n'
        print('检测到设置了自动使用奖品\n')
    else:
        # msg += '默认自动使用奖品，如需使用请定义变量：export ali_reward = False\n'
        print('默认自动使用奖品，如需使用请定义变量：export ali_reward="True"\n')
    parts = ali_ck.split('&')
    sub_strings = []
    for part in parts:
        sub_strings.extend(part.split('#'))
    print(f"\n>>>>>>>>>>共获取到{len(sub_strings)}个账号<<<<<<<<<<")
    for indx, ck in enumerate(sub_strings):
        Sign = AliDrive_CheckIn(ck, ali_reward)
        Sign.getToken(indx)
    send('阿里云盘签到通知', send_msg)
