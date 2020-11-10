# Django 搭建完整的网站

## 实现的功能
1. 首页能够实现动态轮播图
2. 多级评论
3. 能够插入图片、视频、音乐
4. 动态背景
5. 用户注册、登录、退出、点赞
6. 二级菜单，鼠标移入时弹出菜单
7. 能够有小游戏窗口
8. 重写后台管理界面
9. 支持Markdown语法
10. 可以选择富文本或者是Markdown语法
11. 左侧菜单隐藏，移入时弹出
12. 回到顶部区域
13. 最后能够实现前后端分离
14. 数据库使用MySQL

## 参考内容
一些常见的问题都放在了doc文件夹下

## 实现的步骤
1. 配置环境
   * virtualenv 虚拟环境配置
    Python安装`virtualenv`，并生成虚拟环境
    ```
    pip install virtualenv
    python -m venv env
    ```
    启动虚拟环境
    ```
    .\env\Scripts\activate
    ```
    安装django和pillow库
    ```
    pip install django
    pip install pillow
    ```

    安装完成后，使用django进行生成项目, `seco`为将要生成的项目名称
    ```
    django-admin startproject seco
    ```
    运行django，并且在`127.0.0.1:8000`中可以看到启动成功的界面
    ```
    python manage.py runserver 
    ```
    新建项目APP`article`
    ```
    python manage.py startapp article
    ```
    将App在`seco/setting.py`中`INSTALLED_APPS`中加入
    ```python
    INSTALLED_APPS =[
        ....
        'article',
    ]
    ```
    将`seetings.py`中的语言和时区改为中文和shanghai 
    ```python
    LANGUAGE_CODE = 'zh-hans'
    TIME_ZONE = 'Asia/shanghai'
    ```

    将`templates`加入到`TEMPLATES`中
    ```python
    'DIRS': [os.path.join(BASE_DIR, 'templates'),],
    ```
    设置静态文件和媒体文件的目录
    ```python
    # 设置静态文件的根目录
     STATIC_ROOT = [
         os.path.join(BASE_DIR, 'static'),
     ]

     # 设置媒体文件的位置
     MEDIA_URL = '/media/',
     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

    将更改数据库，将Django自带的sqlite数据库换成MySQL数据库
    ```python
        import pymysql         # 一定要添加这两行！通过pip install pymysql！
        pymysql.install_as_MySQLdb()

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'mysite',
                'HOST': '192.168.1.1',
                'USER': 'root',
                'PASSWORD': 'pwd',
                'PORT': '3306',
            }
        }
    ```
    将数据库换成sqlite以外的数据库需要手动创建数据库`CREATE DATABASE database_name`,
    ```
    CREATE DATABASE mysite CHARACTER SET utf8;
    ```

2. 使用Markdown编辑器
   首先需要安装Markdown
   ```python 
   pip install markdown 
   ```
   将Markdown显示，可以使用
    ```python
    import markdown

    eassy.body = markdown.markdown(article.body, extensions=[
                                     'markdown.extensions.extra',
                                    # 语法高亮扩展
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',])
    ```

    实现代码高亮
    ```
    pip install Pygments
    ```
    进入到`static/css/`然后运行
    ```
    pygmentize -S monokai -f html -a .codehilite > monokai.css
    ```
    然后在网页中引入生成的`css`文件

    安装富文本编辑器
    ```
    pip install django-mdeditor
    ```
    然后在settings.py中进行注册
    ```
    'mdeditor',
    ```
    将下面代码放入到`urls.py`的底部，用于指定图片传送的地方
    ```python 
    from django.conf.urls.static import static
    from django.conf import settings

    if settings.DEBUG:
        # static files (images, css, javascript, etc.)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
    在Model中使用mdeditor
    ```python
    from mdeditor.fields import MDTextField

    context = MDTextField("文章内容")
    ```

3. 在Markdown中提取目录
   首先现将之前的`eassy.body`改为：
   ```python 
    md = markdown.Markdown( extensions=[
                                     'markdown.extensions.extra',
                                    # 语法高亮扩展
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',])
    eassy.context = md.convert(eassy.context)
    eassy.toc = md.toc

   ```
   > 注意`markdown.markdown` 和 `markdown.Markdown`的区别


## 环境中更改过的地方
1. 在`lib\site-packages\django\db\backends\mysql\base.py`中，将以下代码注释
   ```python
   if version < (1, 3, 3):
     raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__) 
   ```
2. 在`env\lib\site-packages\django\db\backends\mysql\operations.py`中将146行中
   ```python
   query = query.decode(errors='replace')
   ```
   改为
   ```python 
   query = query.encode(errors='replace')
   ```

## 记录我在使用Django时候遇到的坑（遇到的问题，为什么会出现这些问题， 如何解决）
1. 问题：在使用nginx时，已经申请了https链接，结果使用的时候依旧显示nginx的欢迎界面
   解决办法：  将server 80的下的内容复制一份到server 443中即可。    
   已经将成功的配置和方法复制到了nginx.conf 和 uwsgi/myblog.ini中
   

2. 出现错误
   ```
   RuntimeError: cryptography is required for sha256_password or caching_sha2_password
   ```
   解决方法：
   ```
   pip install cryptography
   ```
3. 在网页中的Markdown的列表无法正常显示，不能正常的缩进，在显示`css`文件中的`div ul`下加入
   ```css
   padding-inline-start: 1em;
   ```

4. Django的后台管理样式出现无法加载css样式的问题，
   解决方法：           
   首先在`seetings.py`中添加`STATIC_ROOT`选项
   ```python
   STATIC_ROOT = os.path.join(BASE_DIR, 'static_new')
   ```
   然后再将`nginx`服务器的配置更改`vi /etc/nginx/sites-available/mysite.conf`
   将下面的内容
   ```
   location /static {
        alias /home/www/seco/static; # your Django project's static files - amend as required
    	index index.html index.htm;
	}
   ```
   更改为
   ```
   location /static {
        alias /home/www/seco/static_new; # your Django project's static files - amend as required
    	index index.html index.htm;
	}
   ```

# 解决跨域问题
首先安装插件
```shell
pip install django-cors-headers
```

在`settings.py`中配置选项：
```python
INSTALLED_APPS = [
    ...
    'corsheaders'，
    ...
 ] 

MIDDLEWARE_CLASSES = (
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', # 注意顺序
    ...
)
#跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ()

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)
```

# 备份pip安装过的库
备份
```shell
pip freeze > requirement.txt
```

安装

```shell
pip install -r requirement.txt
```