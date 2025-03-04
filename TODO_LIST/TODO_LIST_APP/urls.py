# from django.contrib import admin
# from django.urls import path
# from . import views 

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('admin/', admin.site.urls),
    

    
# ]
from django.urls import path
from TODO_LIST_APP.views import home, archived, deleted, add, update, empty_recycle_bin

urlpatterns = [
    path('', home, name='home'),
    path('archived/', archived, name='archived'), 
    path('deleted/', deleted, name='deleted'), 
    path('add/', add, name='add'),
    path('<int:pk>/update/', update, name='update'), 
    path('empty_recycle_bin/', empty_recycle_bin, name='empty_recycle_bin'),    
]