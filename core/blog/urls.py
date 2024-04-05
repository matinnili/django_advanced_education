from django.urls import path
from .views import indexview,IndexView
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name='blog'
urlpatterns = [
    # path('cbv-index/', TemplateView.as_view(template_name="index.html",extra_context={"name":"ali"})),
    path('cbv-index/',IndexView.as_view(),name='cbv-index'),
    path('go-to-index',RedirectView.as_view(pattern_name='blog:cbv-index'))
]