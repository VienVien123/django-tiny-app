from django.urls import path
from TODO_LIST_APP.views import home, archived, deleted, add, update, empty_recycle_bin
from django.contrib.auth import views as auth_views
from .views import manage_users, reset_password, user_login
from . import views
# from .views import user_register, user_login

urlpatterns = [
    path('', home, name='home'),
    path('archived/', archived, name='archived'), 
    path('deleted/', deleted, name='deleted'), 
    path('add/', add, name='add'),
    path('<int:pk>/update/', update, name='update'), 
    path('empty_recycle_bin/', empty_recycle_bin, name='empty_recycle_bin'),   
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login') ,
    path('admin-custome/manage-users/', views.manage_users, name='manage_users'),
    path('admin-custome/manage-users/block/<int:user_id>/', views.toggle_block_user, name='toggle_block_user'),
    path('admin-custome/manage-users/reset-password/<int:user_id>/', views.reset_password, name='reset_password'),
]