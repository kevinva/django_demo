from django.urls import path, re_path
from . import views

app_name = 'tasks'
urlpatterns = [
    # 创建任务
    path('create/', views.task_create, name = 'task_create'),

    # 查询任务列表
    path('', views.task_list, name = 'task_list'),

    # 查询单个任务对象
    re_path(f'^(?P<pk>\d+)/$', views.task_detail, name = 'task_detail'),

    # 更新任务
    re_path(f'^(?P<pk>\d+)/update/$', views.task_update, name = 'task_update'),

    # 删除任务
    re_path(f'^(?P<pk>\d+)/delete/$', views.task_delete, name = 'task_delete'),
]