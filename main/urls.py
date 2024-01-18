from django.urls import path

from .views import link_list, redirect_to_external_site, delete_link

urlpatterns = [
    path('', link_list, name='home'),
    path('link/<str:link>', redirect_to_external_site, name='user_link'),
    path('link/<str:link>/del', delete_link, name='del'),
]
