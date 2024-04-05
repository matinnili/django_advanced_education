from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
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