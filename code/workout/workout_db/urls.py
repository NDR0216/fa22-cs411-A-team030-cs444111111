from django.urls import path
from .views import *
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register(r'user', UserViewSet, basename = 'user')
# router.register(r'userForm', UserViewSet, basename = 'user')

# urlpatterns = router.urls

from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('user/', views.user, name='user'),
    path('user/add/', views.user_add, name='user_add'),
    path('user/add_post/', views.user_add_post, name='user_add_post'),
    path('user/delete/<str:user_id>', views.user_delete, name='user_delete'),
    path('user/update/<str:user_id>', views.user_update, name='user_update'),
    path('user/update_post/<str:user_id>', views.user_update_post, name='user_update_post'),
    path('video/', views.video_trainer, name='video'),
    path('adv_query_1/', views.adv_query_1, name='adv_query_1'),
    path('adv_query_2/', views.adv_query_2, name='adv_query_2'),
]