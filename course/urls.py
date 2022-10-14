from django.urls import path
from .views import *

urlpatterns = [
    path('', CourseListView.as_view(), name='courses'),
    path('detail/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('task_detail/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('course_comment/create/<int:pk>', comment_create, name='main_comment_create'),
    path('main_comment/create/<int:pk>', main_comment_create, name='main_comment_create'),
    path('main_comment_task/create/<int:pk>', main_comment_create_task, name='main_comment_create_task'),
    path('course_comment/delete/<int:pk>', course_comment_delete, name='course_comment_delete'),
    path('course_comment_task/delete/<int:pk>', course_comment_task_delete, name='course_comment_task_delete'),
    path('course_comment_task/create/<int:pk>', course_comment_create_task, name='course_comment_task_delete'),
]
