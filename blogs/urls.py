from django.urls import path, re_path
from . import views
# from django.conf.urls import url

# app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('retrieve', views.retrieve, name="retrieve"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    # url(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete"),
    re_path(r'^delete_product/(?P<pk>[0-9]+)/$', views.delete,name="delete")
]
