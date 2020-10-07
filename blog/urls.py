
from django.urls import path
from . import views

app_name = 'all_blog'

urlpatterns = [
    path('',views.blog ,name = 'blog'),
    path('<int:blog_id>',views.details, name= 'details')
]
