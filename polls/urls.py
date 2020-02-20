from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),

    path('home1/', views.home1),
    path('home1/test', views.test, name='test'),

    path('home2/', views.home2),
    path('home2/tsk', views.tsk, name='tsk'),

    path('home3/', views.home3),
    path('home3/tsk_view', views.tsk_view, name='tsk_view'),

    path('home4/', views.home4),
    path('home4/tsk_cmnt', views.tsk_cmnt, name='tsk_cmnt'),

    path('home5/', views.home5),
    path('home5/user', views.user, name='user'),




    path('user_get/', views.user_get, name='user_get'),





]



