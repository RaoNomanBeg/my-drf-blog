from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Blog 
from .forms import Blogform
from django.contrib.auth.models import User
from .serializers import Blogserializer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
# Create your views here.

@login_required
def index(request):
    post=Blog.objects.all().order_by('-created_at')

    if request.method=='POST':
        form=Blogform(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('index')
    else:
        form=Blogform()
        return render(request, 'core/index.html',{'post':post, 'form':form})
      

def post_detail(request, pk):
    post=get_object_or_404(Blog, pk=pk)
    return render(request, 'core/list.html', {'post':post})
 
@login_required
def delete_post(request, pk):
    post=get_object_or_404(Blog, pk=pk)

    if post.author != request.user:   
        # return redirect('index')
        return HttpResponseForbidden("You are not allowed to delete this postsss.")
    
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, 'core/delete.html', {'post':post})

    


class Blogviewset(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=Blogserializer

class Bloglist(APIView):
    def get(self,request):
        Blogs=Blog.objects.all()
        serializer=Blogserializer(Blogs,many=True)
        return Response(serializer.data)