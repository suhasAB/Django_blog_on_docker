from django.shortcuts import render
from django.views import  generic
from .models import Post as PostModel
# Create your views here.

class PostList(generic.ListView):
    queryset=PostModel.objects.filter(status=1).order_by('-created_on')
    template_name='index.html'

class PostDetail(generic.DetailView):
    model=PostModel
    template_name='post_detail.html'