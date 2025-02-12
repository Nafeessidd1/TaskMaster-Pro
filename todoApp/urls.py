"""todoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from todos.views import login_page, register,logout_page # Import the views from your views module
import todoApp.views as views

urlpatterns = [
    path('todos/', include('todos.urls')),
    path('login/', login_page, name='login_page'), 
    path('logout/', logout_page, name='logout_page'),# 'login_page' as a string
    path('register/', register, name='register'),   # 'register' as a string
    path('admin/', admin.site.urls),
    path('', views.index, name='index')  # Provide a name for the index path
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

