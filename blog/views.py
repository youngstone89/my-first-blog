from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	posts= Post.objects.all()

	if posts:
		return render(request,'blog/post_list.html', {'posts' : posts})
	else:
		return render(request, 'blog/error.html',{})

def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html',{'post': post})

def index(request):
	return HttpResponse("Hello World, You're at the polls index.")