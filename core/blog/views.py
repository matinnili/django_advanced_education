from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import Post

# Create your views here.
def indexview(request):
    """
    a function based view  to show index page    
    """
    context={'name':'ali'}
    return render(request,"index.html",context)

class IndexView(TemplateView):
    """
    a class based view  to show index page
    """
    template_name='index.html'
    def get_context_data(self, **kwargs: Any) :
        context=super().get_context_data(**kwargs)
        context['name']='ali'
        return context
class Redirecttomaktab(RedirectView):
    url='https://maktabkhooneh.com'
    def get_redirect_url(self, *args: Any, **kwargs: Any) :
        post=get_object_or_404(Post,pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    
    
class PostList(ListView):
    # model=Post
    # queryset=Post.objects.all()
    context_object_name='Posts'
    paginate_by=2
    ordering='id'
    def get_queryset(self) :
        Posts=Post.objects.filter(status=False)
        return Posts