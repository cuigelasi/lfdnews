from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^upload/$',views.upload,name='upload'),
    url(r'^allupload/$',views.allupload,name='allupload'),
    url(r'^showall/$',views.showall,name='showall'),
    url(r'^showmore/$',views.showmore,name='showmore'),
    url(r'^showmore/(?P<photoblogmapPhotoBlogMap_phototitle>\w+([-+.]\w+)*\w+([-.]\w+)*\w+([-.]\w+)*)/$',views.showmore),
]
