from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
   name=models.CharField(max_length=250) 
   
   def __str__(self):
       return self.name
    
USER=get_user_model()    
    
class Post(models.Model):
    
    '''
    this is a class to create post in blog app
    '''
    author=models.ForeignKey(USER,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=250)
    content=models.TextField()
    status=models.BooleanField()
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
