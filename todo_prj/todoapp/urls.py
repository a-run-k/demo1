
from django.contrib import admin
from django.urls import path, include

from todoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cvhome/',views.listview.as_view(),name='cvhome'),
    path('detailview/<int:pk>/',views.dv.as_view(),name='detailview'),
    path('uv/<int:pk>/',views.uv.as_view(),name='uv'),
    path('delev/<int:pk>/',views.delev.as_view(),name='delev')
]

