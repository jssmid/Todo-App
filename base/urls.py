from django.urls import path
from . import views


urlpatterns = [

    path('', views.home,  name='home'),
    path('history/', views.history, name='history'),
    path('add_task/', views.add, name='add_task'),
    path('edit_task/<str:pk>/', views.edit, name='edit_task'),
    path('delete_task/<str:pk>/', views.delete, name='delete_task'),
    path('create_user/', views.create_user, name='create_user'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logout_page, name='logout'),

]