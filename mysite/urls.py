"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from threedbang import views as threedbang_views
# from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^threedbang/', include('threedbang.urls')),
    # url(r'^$' , threedbang_views.upload , name = 'root'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^accounts/login/', auth_views.login , name = 'login' ,kwargs = {'template_name': 'index-smooth-scroll.html'}),
    # url(r'^accounts/logout/', auth_views.logout , name = 'logout' ,kwargs = {'template_name': 'index-smooth-scroll.html'}),
    url(r'^account/signup$', threedbang_views.CreateUserView.as_view() , name = 'signup'),
    url(r'^account/signup/done$' , threedbang_views.RegisteredView.as_view() , name = 'create_user_done'),
    url(r'^$', threedbang_views.BootTemplateView.as_view() , name = 'bootstrap'),
    url(r'^mypage/$', threedbang_views.MypageTemplateView.as_view() , name = 'mypage' )
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
