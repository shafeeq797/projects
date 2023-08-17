"""
URL configuration for projectcake project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from appcake import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('createuser/',views.createuser),
    path('adduser/',views.adduser),
    path('loginuser1/',views.loginuser),
    path('admin1/',views.admin2),
    path('user1/',views.user2),
    path('addcake/',views.addcake1),
    path('addcake3/',views.addcake4),
    path('viewcake/',views.viewcak1),
    path('updatecake/<int:id>',views.updatecake2),
    path('updatecake3/<int:id>',views.update5),
    path('delete/<int:id>',views.delete1),
    path('viewuser/',views.viewuser1),
    path('deleteuser/<int:id>',views.deleteuser2),
    path('viewcakeonly/',views.cakeonly),
    path('viewprofile/',views.profile),
    path('updateprofile/<int:id>',views.updateprofile1),
    path('updateprofile2/<int:id>',views.updateprofile3),
    path('chocolatecake/',views.choco),
    path('price/',views.price1),
    path('back/',views.admin2),
    path('back1/',views.user2),


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
