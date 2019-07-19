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