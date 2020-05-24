"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
import BlogApp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogApp.views.home,name='home'),
    path('BlogApp/<int:blog_id>', BlogApp.views.detail,name='detail'),
    path('BlogApp/new', BlogApp.views.new,name='new'),
    path('BlogApp/create', BlogApp.views.create,name='create'),
    path('BlogApp/edit/<int:blog_id>', BlogApp.views.edit,name='edit'),
    path('BlogApp/update/<int:blog_id>', BlogApp.views.update,name='update'),
    path('BlogApp/delete/<int:blog_id>', BlogApp.views.delete,name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
