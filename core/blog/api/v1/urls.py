from django.urls import path, include
from . import views
from django.views.generic import TemplateView, RedirectView


app_name= 'api-v1'
urlpatterns = [

  # path('post/', views.postList, name='post-list'),
  # path('post/<int:id>/', views.postDetail, name='post-detail'),
  path('post/', views.PostList.as_view(), name='post-list'),
  path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),

]