from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.AppIndex.as_view(), name='app_index'),
    path('<slug:slug>/', views.AppShow, name='app_show'),
    path('category/<slug:url>/', views.categoryView, name='category'),
    path('contact', views.ContactView.as_view(), name='contact'),
]
