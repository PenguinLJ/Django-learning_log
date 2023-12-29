"""定义learning_logs的URL模式"""
from django.urls import path, include

from . import views

app_name = 'learning_logs'  # 变量 app_name 让 Django 能够将这个 urls.py 文件与项目内其他应用程序中的同名文件区分开来

urlpatterns = [
    # home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>',views.edit_entry,name='edit_entry'),

]
'''实际的 URL 模式是对 path() 函数的调用，这个函数接受三个实参（见❺）。第一个
是一个字符串，帮助 Django 正确地路由（route）请求。收到请求的 URL 后，Django
力图将请求路由给一个视图，并为此搜索所有的 URL 模式，以找到与当前请求匹配
的。Django 忽略项目的基础 URL（http://localhost:8000/），因此空字符串（''）与基
础 URL 匹配。其他 URL 都与这个模式不匹配。如果请求的 URL 与任何既有的 URL
模式都不匹配，Django 将返回一个错误页面。
path() 的第二个实参（见❻）指定了要调用 view.py 中的哪个函数。当请求的 URL
与前述正则表达式匹配时，Django 将调用 view.py 中的 index() 函数（这个视图函数
将在 18.3.2 节编写）。第三个实参将这个 URL 模式的名称指定为 index，让我们能
够在其他项目文件中轻松地引用它。每当需要提供这个主页的链接时，都将使用这个
名称，而不编写 URL。'''
