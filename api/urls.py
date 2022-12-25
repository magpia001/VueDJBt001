from django.urls import path
from . import views

app_name='api'
urlpatterns = [
    path('post/list/', views.ApiPostLV.as_view(), name='post_list'),
]