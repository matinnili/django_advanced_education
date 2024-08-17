from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from blog.models import Post,Category
from .serializer import PostSerializer,CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import PostPagination
from .filters import PostFilter

class PostList(APIView):


    permission_classes=[IsAuthenticated]
    serializer_class=PostSerializer

    
    def get(self,request):
        post=Post.objects.all()
        serializer=PostSerializer(post,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
class PostModelViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    # filterset_fields=['category','author']
    # search_fields=['title']
    # ordering_fields=['title']
    filterset_class=PostFilter
    pagination_class=PostPagination
    @action(["GET"],detail=False)
    def get_ok(request):
        return Response('get_ok')

class CategoryModelviews(ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    
@api_view(['GET','POST'])
def postList(request):
    if request.method=='GET':
        post=Post.objects.all()
        serializer=PostSerializer(post,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        


@api_view(['GET','PUT','DELETE'])
def postDetail(request,id):    

    post=get_object_or_404(klass=Post,pk=id)    
    if request.method=='GET':
        serial=PostSerializer(post)
        return Response(serial.data)
    elif request.method=='PUT':
        serializer=PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method=='DELETE':
        post.delete()
        return Response({"detail":"post is deleted successfully"})
