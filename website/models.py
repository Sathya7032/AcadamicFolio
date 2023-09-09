from django.db import models
from django.utils.html import format_html


class Contact(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    service = models.TextField(max_length=100)
    message1 = models.TextField(max_length=100)

    def __str__(self):
        return self.username
    

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    discription = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;"/>'.format(self.image))
    
    def __str__(self):
        return self.title


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')
    content = models.TextField()
    url = models.CharField(max_length=100)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)   

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;"/>'.format(self.image))
    
    def __str__(self):
        return self.title
    

    

