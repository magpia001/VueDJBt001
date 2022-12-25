from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [

    # /blog/post/99/
    path('post/<int:pk>/', views.PostDV.as_view(), name='post_detail'),
    # /blog/post/여행/
    path('category/<str:slug>/', views.category_page, name='category_page'),
    # /blog/post/행복/
    path('tag/<str:slug>/', views.tag_page, name='tag_page'),
]
