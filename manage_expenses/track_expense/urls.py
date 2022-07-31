

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add_expense,name='add'),
    path('edit/<int:pk>',views.edit_expense,name='edit'),
    path('delete/<int:pk>',views.delete_expense,name='delete'),
]