from django.shortcuts import render
from django.http import HttpResponse
from photologue.models import *
from django.shortcuts import render_to_response
from django.conf import settings
import os
from PIL import Image
import datetime
from .models import Blog
from .models import PhotoBlogMap



def upload(request):
    return render(request,'cuigelasi/upload.html')

def allupload(request):
      try:
        f=request.FILES['tuxiang']
        if f.size > 5000000:
          return HttpResponse("it is large!")
        try:
          parser=ImageFile.Parser()
          for chunk in f.chunks():
            parser.feed(chunk)
          img=parser.close()
        except IOError:
          return HttpResponse("it is an io error!")
      
        imageName='photologue/photos/'+f.name
        name=settings.STATIC_PATH+'/'+imageName
        
        img02=Image.open(f)
        img02.save(name)
        
      except UnicodeEncodeError:
        return render_to_response('cuigelasi/upload.html',{'image_error':"please use English"})
      
      now ='00TB'+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
      photoInfo=Photo(image=imageName,title=now,slug=now,is_public=True)
      photoInfo.save()

      phototype="0000"
      
      try:
        f1=request.FILES['fengmiantuxiang']
        if f1.size > 5000000:
          return HttpResponse("it is large!")
        try:
          parser1=ImageFile.Parser()
          for chunk1 in f1.chunks():
            parser1.feed(chunk1)
          img1=parser1.close()
        except IOError:
          return HttpResponse("it is an io error!")
        imageName1='photologue/photos/'+f1.name
        name1=settings.STATIC_PATH+'/'+imageName1
        img03=Image.open(f1)
        img03.save(name1)
      except UnicodeEncodeError:
        return render_to_response('cuigelasi/upload.html',{'image_error':"please use English"})
      
      now1 ='11TB'+datetime.datetime.now().strftime("%Y%m%d%H%M%S")
      photoInfo1=Photo(image=imageName1,title=now1,slug=now1,is_public=True)
      photoInfo1.save()

      phototype1="0001"
      
      title=request.POST['biaoti']
      content=request.POST['neirong']
      photo_name=request.POST['TBbiaoti']
      st=Blog()
      st.blog_title=title
      st.blog_content=content
      st.photo_name=photo_name
      st.save()
      
      pe=PhotoBlogMap()
      pe.PhotoBlogMap_blogtitle=title
      pe.PhotoBlogMap_phototype=phototype
      pe.PhotoBlogMap_phototitle=now
      pe.save()

      pe1=PhotoBlogMap()
      pe1.PhotoBlogMap_blogtitle=title
      pe1.PhotoBlogMap_phototype=phototype1
      pe1.PhotoBlogMap_phototitle=now1
      pe1.save()
      
      return HttpResponse("it is ok!") 

def showall(request):
      photo_list= Photo.objects.all()
      blog_list=Blog.objects.all()
      photoblogmap_list=PhotoBlogMap.objects.all()
      return render_to_response('cuigelasi/showall.html',{'photo_list':photo_list,'blog_list':blog_list,'photoblogmap_list':photoblogmap_list})

def showmore(request,photoblogmapPhotoBlogMap_phototitle):
      m=photoblogmapPhotoBlogMap_phototitle
      pp=PhotoBlogMap.objects.get(PhotoBlogMap_phototitle=m)
      p=pp.PhotoBlogMap_blogtitle
      t=Blog.objects.get(blog_title=p)
      photo_list= Photo.objects.all()
      photoblogmap_list=PhotoBlogMap.objects.all()
      return render_to_response('cuigelasi/showmore.html',{'photo_list':photo_list,'photoblogmap_list':photoblogmap_list,'t':t})
  
  
  
  
  