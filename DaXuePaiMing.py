'''
author : Liujian
data : 2017-05-14

中国大学排名定向爬虫

'''

__author__ = "LiuJian"

import requests
import bs4
from bs4 import BeautifulSoup

# 获取网页内容
def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("ERROR!")
        return ""

# 提取网页当中的内容
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:  # 先找到tbody标签，children是tr标签
        if isinstance(tr,bs4.element.Tag): # 过滤非tag类型
            tds = tr('td')  # 查询tr标签当中所有的td标签
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
            # 将前三个td标签当中的内容提取出来

    # print(ulist)

#  将内容按格式打印
def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288))) # 采用中文字符的空格填充
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)

main()