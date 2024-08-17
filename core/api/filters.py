from django_filters.rest_framework import FilterSet
from blog.models import Post

class PostFilter(FilterSet):

    class Meta:
        model=Post
        fields=['category']