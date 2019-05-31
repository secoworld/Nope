#添加开始视图，设置为开始 页面
from django.http import HttpResponse

def hello(request):
    return HttpResponse("欢迎使用Django")