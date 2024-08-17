from django.urls import path,include
from .views import indexview,IndexView,Redirecttomaktab,PostList
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name='blog'
urlpatterns = [
    # path('cbv-index/', TemplateView.as_view(template_name="index.html",extra_context={"name":"ali"})),
    path('cbv-index/',IndexView.as_view(),name='cbv-index'),
    path('post/',PostList.as_view(),name='post-list'),
    path('go-to-index/<int:pk>',Redirecttomaktab.as_view()),
    path('api/v1/',include('api.urls'))
]