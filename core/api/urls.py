from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name='api-version1'
router=DefaultRouter()
router.register('post',views.PostModelViewSet,basename='post')
router.register('category',views.CategoryModelviews,basename='category')
urlpatterns=router.urls
# urlpatterns = [
#     # path('cbv-index/', TemplateView.as_view(template_name="index.html",extra_context={"name":"ali"})),
#     path('post/',views.PostModelViewSet.as_view(),name='post-list'),
#     # path('post/<id>',views.postDetail,name='post-detail'),

# ]