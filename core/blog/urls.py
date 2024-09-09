from django.urls import path, include
from . import views
from django.views.generic import TemplateView, RedirectView


app_name= 'blog'
urlpatterns = [
  # path('fbv-index/', views.indexView, name='fvb-test'),
  # path('cbv-index/', TemplateView.as_view(template_name='index.html', extra_context={"name":"ali"})),
  path('cbv-index/', views.IndexView.as_view(), name='cbv-index'),
  # path('go-to-codena', RedirectView.as_view(url='https://codena.org'), name='go-to-codena'),
  path('go-to-index/', RedirectView.as_view(pattern_name="blog:cbv-index"), name='go-to-index'),
  path('go-to-codena/<int:pk>/', views.RedirectToCodena.as_view(), name='go-to-codena'),
  path('post/', views.PostListView.as_view(), name= 'post-list'),
  path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
  path('post/create/', views.PostCreateView.as_view(), name='post-create' ),
  path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post-edit'),
  path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
  path('api/v1/', include('blog.api.v1.urls'))
]