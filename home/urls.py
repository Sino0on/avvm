from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

app_name = 'home'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('news_detail/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('event_detail/<int:pk>', EventDetailView.as_view(), name='event_detail'),
    path('page_detail/<int:pk>', PageDetailView.as_view(), name='page_detail'),
    path('galery/', GaleryListView.as_view()),
    path('register/', register, name='register'),
    path('login/', loginview, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('create_news/', NewsCreateView.as_view(), name='create_news'),
    path('update_news/<int:pk>', NewsUpdateView.as_view(), name='update_news'),
    path('update_event/<int:pk>', EventUpdateView.as_view(), name='update_event'),
    path('events/', EventsListView.as_view(), name='events')
]
