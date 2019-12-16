import json
import requests

def run(url):

    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    #verify参数是为了ssl验证
    respones = requests.get(url,verify=False,headers=head)

    jsstr = respones.content.decode()


    jsdata = json.loads(jsstr)

    for i in jsdata:
        #电影名字
        print(i["title"])
        #url
        print(i["url"])
        #评分
        print(i["score"])

if __name__ == '__main__':
    for num in range(0,35):
        url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start='+str(num*20)+'&limit=20'
        info = run(url)
