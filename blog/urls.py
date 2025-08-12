from django.urls import path , include
from .views import *

urlpatterns = [
    path("", index , name='home'),
    path("post/<slug>/", post_detail, name="blog-post-detail"),


]