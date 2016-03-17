from django.db import models

# Create your models here.

class Blog(models.Model):
    blog_title = models.CharField(max_length=60)
    blog_content = models.CharField(max_length=9000)
    photo_name = models.CharField(max_length=60)
     
    def __str__(self):
        return self.blog_title
    
class PhotoBlogMap(models.Model):
    PhotoBlogMap_blogtitle=models.CharField(max_length=30)
    PhotoBlogMap_phototype = models.CharField(max_length=30)
    PhotoBlogMap_phototitle= models.CharField(max_length=30)
    
    def __str__(self):             
        return self.PhotoBlogMap_blogtitle

