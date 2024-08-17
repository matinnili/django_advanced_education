from rest_framework import serializers
from blog.models import Post,Category

class PostSerializer(serializers.ModelSerializer):
    
    snippet=serializers.ReadOnlyField(source='get_snippet')
    
    category=serializers.SlugRelatedField(slug_field='id',queryset=Category.objects.all())
    class Meta :
      model=Post
      fields=['title','content','status','author','created_date','id','snippet','category']

    def get_absolute_url(self,obj):
       request=self.context.get('request')
       return request.build_absolute_uri(obj)
    def to_representation(self, instance):
       rep=super().to_representation(instance)
       request=self.context.get('request')
       
       if request.__dict__['parser_context']['kwargs']:
          rep.pop('snippet')
       else:
          rep.pop('content')
       
       rep['category']=CategorySerializer(instance.category).data
       
       return rep
      

      

class CategorySerializer(serializers.ModelSerializer):
   
   class Meta :
      model=Category
      fields=['name','id']
      