from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://tieba.baidu.com/p/4847606272?pn={page}'
heads = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"
}

page = 0
n = 0
# 循环爬取每一页的信息
while True:
    page += 1
    reqone = requests.get(url.format(page=page), headers=heads)
    # 创建beautifulsoup
    Html = BeautifulSoup(reqone.text, features="lxml")
    print("页面: ", url.format(page=page))
    # 利用css选择器查找
    ck1 = Html.select('#j_p_postlist')
    # 到37页后停止循环
    if page == 38:
        break
    # 通过遍历爬取所有的图片标签
    for ck2 in ck1:
        ck3 = str(ck2.select('.BDE_Image'))
        print()
        try:
            for i in [7, 17, 27, 37, 47, 57, 67, 77, 87, 97, 107, 117, 127, 137, 147, 157, 167, 187, 197, 207]:
                # 通过“切割字符串，并抓取指定下标信息
                ck4 = ck3.split('"')[int(i)]
                print(ck4)
                # 保存到本地
                res = requests.get(ck4, headers=heads)
                n = n + 1
                with open('d:\\pic\\' + str(n) + '.jpg', 'wb') as f:
                    f.write(res.content)
        except:
            pass
