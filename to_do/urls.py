from django.contrib import admin
from django.urls import path , include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('base.urls') ),
    path('history/', include('base.urls')),
    path('add_task/', include('base.urls')),
    path('edit_task/<str:pk>/', include('base.urls')),
    path('delete_task/<str:pk>/', include('base.urls')),
    path('create_user/', include('base.urls')),
    path('login/', include('base.urls')),
    path('logout/', include('base.urls')),
    
]
