# Django搭建的网站 #

网站的html页面：
* 首页
* 详情页
* 列表页
* 查询页
* About Me单页

博客网站的数据类型：
* 标签
  * 名称
* 分类
  * 名称
  * 别名（地址栏使用的名称）
* 作者
* 文章
  * 标题
  * 发表时间
  * 修改时间
  * 标签
  * 内容
  * 作者
  * 图片

----

python 环境安装打包
```
pip freeze > requirement.txt
```
将安装模块
```
pip install -r requirement.txt
```


## 模型设置
使用markdown语法
```
pip install markdown
```
在detail函数中，对文章的内容进行
```
#使用Markdown语法进行渲染
    article.content = = markdown.markdown(article.content,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
```
## 代码高亮
安装代码高亮模块
```
pip install Pygments
```

------
2019-06-11 待办事件
* [x] 实现网页的页码
* [x] 重新进行服务器的部署
* [ ] 练习css、JavaScript

---
2019-07-15 添加的内容   
  1.  添加django-mdeditor富文本编辑器 
     具体的教程可以参考[参考教程](https://juejin.im/post/5a9d00c2f265da238e0d3a54)     
     首先需要安装`Pygments`
     ```
         pip install Pygments
     ```
     生成markdown代码高亮，在`static/`文件夹下新建`md_css`文件夹，进入文件夹后，运行
     ```
         pygmentize -S monokai -f html -a .codehilite > monokai.css
     ```
     生成语法高亮的css文件，将该css文件加入到base.html中，即可实现代码高亮

  2. 添加用户的注册和登录功能
        重置密码可以使用Django的第三方软件库
        ```
        pip install -U django-password-reset
        ```
        在根目录的`settings`中将`password-reset`进行注册        
        然后在`urls`中添加
        ```
        path('password-reset/', include('password_reset.urls')),
        ```
        然后需要将自己的邮箱发送邮件。在`settings.py`的最后加入以下的内容：
        ```
        # SMTP服务器，改为你的邮箱的smtp!
        EMAIL_HOST = 'smtp.qq.com'
        # 改为你自己的邮箱名！
        EMAIL_HOST_USER = 'your_email_account@xxx.com'
        # 你的邮箱密码
        EMAIL_HOST_PASSWORD = 'your_password'
        # 发送邮件的端口
        EMAIL_PORT = 25
        # 是否使用 TLS
        EMAIL_USE_TLS = True
        # 默认的发件人
        DEFAULT_FROM_EMAIL = 'xxx的博客 <your_email_account@xxx.com>'
        ```




  3. 增加用户的评论功能
        使用Django-mptt实现分级评论
        安装:
        ```
        pip install django-mptt
        ```
        在app注册表中进行注册
        ```
        'mptt',
        ```
        修改评论模型
        ```
        # django-mptt
        from mptt.models import MPTTModel, TreeForeignKey

        # 替换 models.Model 为 MPTTModel
        class Comment(MPTTModel):
            ...

     # 新增，mptt树形结构
        parent = TreeForeignKey(
            'self',
            on_delete=models.CASCADE,
            null=True,
            blank=True,
            related_name='children'
        )

        # 新增，记录二级评论回复给谁, str
        reply_to = models.ForeignKey(
            User,
            null=True,
            blank=True,
            on_delete=models.CASCADE,
            related_name='replyers'
        )

        # 替换 Meta 为 MPTTMeta
        # class Meta:
        #     ordering = ('created',)
        class MPTTMeta:
            order_insertion_by = ['created']
   
        ```
  4. 对博客的搜索功能进行完善


