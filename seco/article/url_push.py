import os
import django
import time

#设置环境
import sys
pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,pathname)
sys.path.insert(0,os.path.abspath(os.path.join(pathname,'..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE","seco.settings")

#注册django
django.setup()

# 引入requests
import requests

#引入Article 模块
from article.models import Article

url = 'http://data.zz.baidu.com/urls?site=https://www.liulongtao.com&token=kHA6zh1nAq4xtHkW'

# 提交的基本链接
base_url = 'https://www.liulongtao.com/article/'

# 设置headers
header = {
    'User-Agent': 'curl/7.12.1' ,
    'Host': 'data.zz.baidu.com' ,
    'Content-Type': 'text/plain' ,
    'Content-Length': '83',
}

# 读取Article的所有页面，并将数据返回
def get_article():
    articles = Article.objects.all()
    return articles

def  urls_push(url, base_url, articles):
    data =[]
    for art in articles:
        data.append(base_url+str(art.id))

    # 将data数据转换为文本样式
    data = '\n'.join(data)
    # 使用requests发送post请求
    req  = requests.post(url, data = data, headers = header)
    return req.json()

if __name__ == "__main__":
    articles = get_article()
    req = urls_push(url, base_url, articles)
    print(time.asctime(time.localtime()), end=' ')
    print(req)

    print(req)