from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('home',blog,name='home'),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category)
]
