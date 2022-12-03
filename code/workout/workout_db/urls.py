from django.urls import path
from .views import *
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register(r'user', UserViewSet, basename = 'user')
# router.register(r'userForm', UserViewSet, basename = 'user')

# urlpatterns = router.urls

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('keywordsearch/', views.keywordsearch, name='keywordsearch'),
    path('about/', views.about, name='about'),
    path('workout_type/', views.workout_type, name='workout_type'),
    path('workout_type_grid/', views.workout_type_grid, name='workout_type_grid'),
    path('workout_type_table/', views.workout_type_table, name='workout_type_table'),
    path('workout_trainer/', views.workout_trainer, name='workout_trainer'),
    path('workout_trainer_grid/', views.workout_trainer_grid, name='workout_trainer_grid'),
    path('workout_trainer_table/', views.workout_trainer_table, name='workout_trainer_table'),
    path('recipe/', views.recipe, name='recipe'),
    path('recipe_table/', views.recipe_table, name='recipe_table'),
    path('forum/', views.forum, name='forum'),
    path('forum_post/', views.forum_post, name='forum_post'),
    path('forum_edit/', views.forum_edit, name='forum_edit'),
    path('forum_add/', views.forum_add, name='forum_add'),
    path('forum_update/', views.forum_update, name='forum_update'),
    path('forum_delete/', views.forum_delete, name='forum_delete'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('visual/', views.visual, name='visual'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('user_info/', views.user_info, name='user_info'),
    path('logout/', views.logout, name='logout'),
]