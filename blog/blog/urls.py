
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/',include('articles.urls')),
    url(r'^about/$',views.about),
    url(r'^$',views.homepage),
    url(r'^accounts/',include('accounts.urls')),
]
