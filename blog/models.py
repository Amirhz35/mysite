from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    category = models.ManyToManyField(Category)
    #tag
    counted_veiw = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return '{} _ {}'.format(self.title,self.id)

    def snippetchar(self):
        return self.content[:100] + '...'

    def snippetwords(self):
        return Truncator(self.content).words(20)
        
