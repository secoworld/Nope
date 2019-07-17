from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from blog.models import Article
from .models import Comment
from .forms import CommentForm
# Create your views here.

# @login_required(login_url="/userprofile/login/")
# def post_comment(request, article_id):
#     article = get_object_or_404(Article, id=article_id)

#     # 处理POST请求
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.article = article
#             new_comment.user = request.user
#             new_comment.save()
#             return redirect("blog:detail", article_id)
#         else:
#             return HttpResponse("表单的内容有错误，请重新填写。")
#     else:
#         return HttpResponse("发表评论仅仅接收POST请求")


# @login_required(login_url='userprofile/login/')
# def  post_comment(request, article_id, parent_comment_id=None):
#     article = get_object_or_404(Article, id=article_id)

#     # 处理POST请求
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.article = article
#             new_comment.user = request.user

#             # 二级回复
#             if parent_comment_id:
#                 parent_comment = Comment.objects.get(id=parent_comment_id)
#                 # 如回复的层数超过二级，则转换为二级
#                 new_comment.parent_id = parent_comment.get_root().id
#                 # 被回复人
#                 new_comment.reply_to = parent_comment.user
#                 new_comment.save()
#                 return HttpResponse('200k ok')

#             new_comment.save()
#             return redirect("blog:detail", article_id)

#         else:
#             return HttpResponse("表单的内容有错，请重新书写！")

#     elif request.method == 'GET':
#         # 处理GET请求
#         comment_form = CommentForm()
#         context = {
#             'comment_form': comment_form,
#             'article_id': article_id,
#             'parent_comment_id': parent_comment_id
#         }
#         return render(request, 'reply.html', context)

#     # 处理其他请求
#     else :
#         return HttpResponse("仅接受GET/POST请求")

@login_required(login_url='/userprofile/login/')
# 新增参数 parent_comment_id
def post_comment(request, article_id, parent_comment_id=None):
    article = get_object_or_404(Article, id=article_id)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user

            # 二级回复
            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                # 若回复层级超过二级，则转换为二级
                new_comment.parent_id = parent_comment.get_root().id
                # 被回复人
                new_comment.reply_to = parent_comment.user
                new_comment.save()
                return HttpResponse('200 OK')

            new_comment.save()
            return redirect("blog:detail", article_id)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理 GET 请求
    elif request.method == 'GET':
        comment_form = CommentForm()
        context = {
            'comment_form': comment_form,
            'article_id': article_id,
            'parent_comment_id': parent_comment_id
        }
        return render(request, 'reply.html', context)
    # 处理其他请求
    else:
        return HttpResponse("仅接受GET/POST请求。")