from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.

""" function base view show template"""
# def indexView(request):
#   """
#   function base view for show index page
#   """
#   context= {'name': 'alir'}
#   return render(request, 'index.html', context)


class IndexView(TemplateView):
  """
  class base view for show index page
  """
  template_name = 'index.html'

  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    context["name"]= "ali"
    context['post'] = Post.objects.all()
    return context
    

class RedirectToCodena(RedirectView):
  url= 'https://codena.org'
  def get_redirect_url(self, *args, **kwargs):
    post = get_object_or_404(Post, pk=kwargs['pk'])
    print(post)
    return super().get_redirect_url(*args, **kwargs) + '?utm_source=django'


class PostListView(PermissionRequiredMixin, LoginRequiredMixin ,ListView):
  permission_required = 'blog.view_post'
  # model = Post
  # queryset = Post.objects.all()
  # ordering = '-id' when we use queryset only it will work
  context_object_name = 'posts'
  paginate_by = 2
  

  def get_queryset(self):
    posts = Post.objects.filter(status=True)
    return posts


class PostDetailView(LoginRequiredMixin ,DetailView):
  model = Post



# class PostCreateView(FormView):
#     template_name = 'contact.html'
#     form_class = PostForm
#     success_url = '/blog/post/'

#     def form_valid(self, form):
#       form.save()
#       return super().form_valid(form)

class PostCreateView(LoginRequiredMixin ,CreateView):
  model = Post
  # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
  form_class = PostForm
  success_url = '/blog/post/'
  
  def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)
  

class PostEditView(LoginRequiredMixin ,UpdateView):
  model = Post
  form_class = PostForm
  success_url = '/blog/post/'



class PostDeleteView(LoginRequiredMixin ,DeleteView):
  model = Post
  success_url = '/blog/post/'