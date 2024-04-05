from django.urls import path
from .views import indexview,IndexView
from django.views.generic import TemplateView
urlpatterns = [
    path('cbv-index/', TemplateView.as_view(template_name="index.html",extra_context={"name":"ali"})),
    path('fbv-index/',IndexView.as_view()
         ),
]