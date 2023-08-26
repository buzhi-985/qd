# -- coding: utf-8 --
# @time : 2023/8/17 15:31
# @author : 不知
# @email : buzhi985@qq.com
# @file : mmy.py
# @software: pycharm
# cron: 20 8 * * *
# new Env('慢慢游社区');
import requests
"""
慢慢游社区签到，待明天测试CK有效期 8.17
"""
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": "lz6l_2132_saltkey=wb4gH27w; lz6l_2132_lastvisit=1689733915; lz6l_2132_smile=2D1; lz6l_2132_nofavfid=1; lz6l_2132_auth=5da911ghUN%2B7NBto3Q5vMoCRWvVKIbhFn4Qdm8%2FOrAExJ2WN4j6TjOIq2JdcLNQopor5ZrETfZIuskNXqOI7h3xDjDVQ; lz6l_2132_lastcheckfeed=1037262%7C1691304158; lz6l_2132_atarget=1; lz6l_2132_visitedfid=41D45D79D78D74D2; lz6l_2132_sid=cC4IQA; lz6l_2132_ulastactivity=ae457YIMSDZMBn%2BFYC04Zq65F9FWR%2FNAeREglizCG7a%2Ba2OjdQj2; Hm_lvt_c24fddfc5cb6035d5c7fb62c14b7cd22=1692002822,1692082452,1692148998,1692256896; lz6l_2132_home_diymode=1; Hm_lpvt_c24fddfc5cb6035d5c7fb62c14b7cd22=1692257640; lz6l_2132_sendmail=1; lz6l_2132_lastact=1692257641%09misc.php%09patch",
    "Referer": "https://www.mmybt.com/forum.php",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}


def qd():
    url = "https://www.mmybt.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1"
    data = {
        "formhash": "cded6fae",
        "qdmode": "3",
        "todaysay": "",
        "fastreply": "0",
        "qdxq": "kx"
    }

    rep = requests.post(url, headers=headers,
                        data=data).text
    print(rep)

def test():
    # 4K社区签到没有返回信息
    url = "http://www.4ktt.com/home.php?mod=spacecp&ac=pm&op=checknewpm&rand=1692411632"
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Accept': '*/*',
        'Referer': 'http://www.4ktt.com/forum.php?mod=viewthread&tid=456088&extra=&highlight=%C9%DB%CA%CF%B5%E7%D3%B0&page=2',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'RUyq_2132_saltkey=q4D33DDW; RUyq_2132_lastvisit=1691064234; RUyq_2132_nofavfid=1; RUyq_2132_smile=1D1; RUyq_2132_auth=0ad7HaO0zjdZdjmHqoLezTESKkwn85qRhQPeY2VGmapLX9vgawMeZI7anN0oHduTFlF9J4nfUn%2FZdQ0xR8oaehS9Ew; RUyq_2132_lastcheckfeed=88781%7C1691304991; RUyq_2132_visitedfid=44D40D47D2D42; Hm_lvt_71e76c2a73edd432ce9856a2048f28b9=1692002763,1692082444,1692149059,1692258814; RUyq_2132_widthauto=1; RUyq_2132_sid=Xq6IEU; RUyq_2132_lip=171.22.130.88%2C1692258808; RUyq_2132_creditnotice=0D0D3D5D0D0D0D0D0D88781; RUyq_2132_creditbase=0D1D29D64D0D0D0D0D0; RUyq_2132_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; RUyq_2132_lastact=1692411632%09forum.php%09viewthread; RUyq_2132_st_p=88781%7C1692411632%7Cce2ce54748dd6d60060841444dfb1a07; RUyq_2132_viewid=tid_456088; RUyq_2132_ulastactivity=e1da0fdwExxyVwvrdmr2I4UWP29PTdrfRiFlvF7ujfsDSdy7Ymme'
    }
    text = requests.get(url, headers=head).text
    print(text)

def kk():
    # https://www.4khdr.cn/ 没有返回信息
    url = 'https://www.4khdr.cn/plugin.php?id=k_misign:sign&operation=qiandao&formhash=c05e07a0&format=empty&inajax=1&ajaxtarget='
    head = {
        "accept-encoding": "gzip, deflate, br",
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'hvLw_2132_saltkey=dGd1iD8x; hvLw_2132_lastvisit=1692952888; hvLw_2132_visitedfid=2; _clck=11r8e9m|2|feg|0|1332; PPA_CI=3c63cfc6eeda54a960707df142950f8f; hvLw_2132_st_t=0%7C1692956726%7C3323ef858ee8bc98d988a608ce68d81a; hvLw_2132_forum_lastvisit=D_2_1692956726; hvLw_2132_sendmail=1; hvLw_2132_seccodecS=5446.f228d5d7c054106ddb; hvLw_2132_ulastactivity=1692972531%7C0; hvLw_2132_auth=1e74bz6M%2FEPYUVX5Jg7xBJz6NI6JF4thjEQ0CegdbmqcWTMwQCLAgOrGsyBa1ZdqRGl6f5ooF8knaa9VL3eufSDhtfY; hvLw_2132_sid=0; hvLw_2132_checkpm=1; hvLw_2132_noticeTitle=1; hvLw_2132_lastact=1692972535%09plugin.php%09; _clsk=xhy88e|1692972538747|5|1|w.clarity.ms/collect',
        'referer': 'https://www.4khdr.cn/k_misign-sign.html',
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    text = requests.get(url, headers=head).text
    print(text)

def yy():
    url = "https://www.yingyinwu.net/sg_sign.htm"
    headers={
        "accept": "text/plain, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-length": "0",
        "cookie": "bbs_sid=p2emal3cq6bmm524cnfa1qdo5b; Hm_lvt_89f24e9c1dd236ab5ca51664aaff55d2=1692955284; _ga=GA1.1.852138999.1692955285; PPA_CI=a03b646336a986cc08317ded084d9252; bbs_token=Vz1wOFGFFPIMDtNG_2Br0DNjfFPw8ibmrr9WRb2I6H6YNGqpyAcPqGNcG_2BMopgy6cePYrpFjv7pET_2BPGQhauEHuEA91O8_3D; _ga_TFZGBP72RB=GS1.1.1692970980.2.1.1692972948.0.0.0; Hm_lpvt_89f24e9c1dd236ab5ca51664aaff55d2=1692972948",
        "origin": "https://www.yingyinwu.net",
        "referer": "https://www.yingyinwu.net/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    rep = requests.post(url, headers=headers).text
    print(rep)

if __name__ == '__main__':
    test()
    qd()
    yy()
    kk()
