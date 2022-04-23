"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from main.views import *
from django.views.static import serve
from mysite import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexHandler),
    path('blank/', blankHandler),
    path('checkout/', cartHandler),
    path('store/<int:product_id>', productHandler),
    path('order/<int:order_id>', order_itemHandler),
    path('store/', storeHandler),
    path('about/', aboutHandler),
    path('order/', orderHandler),
    path('contact_us/', contact_usHandler),

    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    })
]

