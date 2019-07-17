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
1、 添加django-mdeditor富文本编辑器 
   具体的教程可以参考[参考教程](https://juejin.im/post/5a9d00c2f265da238e0d3a54)
   * 安装
      ```
      pip install django-mdeditor
      ```
   * 在setting.py中INSTALL_APPS进行配置
      ```
        INSTALLED_APPS = [
        ...
        'mdeditor',
      ]
      ```


