from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth.views import logout
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^facebook/$', views.facebook, name='facebook'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]