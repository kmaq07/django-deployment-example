"""myshop URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from garments.views import base,aboutus,contactus,formalshirts,casualshirt,search_list,thankyou,cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',base),
    path('aboutus',aboutus),
    path('contactus',contactus),
    path('formalshirts',formalshirts),
    path('casualshirt',casualshirt),
    path('search_list',search_list),
    path('thankyou',thankyou),
    path('cart<int:x>',cart),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
