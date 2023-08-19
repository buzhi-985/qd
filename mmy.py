# -- coding: utf-8 --
# @time : 2023/8/17 15:31
# @author : 不知
# @email : buzhi985@qq.com
# @file : mmy.py
# @software: pycharm
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

if __name__ == '__main__':
    # test()
    qd()
