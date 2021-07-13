from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog
#models.py에 Blog를 import 받기
from django.utils import timezone
from .models import Blog
from .forms import BlogForm

#paginator
from django.core.paginator import Paginator

def home(request):
    #blogs=Blog.objects.all()
    #blog 테이블에 있는 객체들 싹다 가져오기

    blogs=Blog.objects.order_by('-pub_date')#최신순 (cf. pub_date: 오래된순)
    search = request.GET.get('search')
    if search=='true':
        author=request.GET.get('writer')
        blogs=Blog.objects.filter(writer=author)  #<->Blog.objects.exclude: author꺼 빼고 보기
        return render(request,'home.html',{'blogs':blogs})

    #글쓴이 검색기능

    paginator=Paginator(blogs,3)
    page=request.GET.get('page')
    blogs=paginator.get_page(page)
    return render(request,'home.html',{'blogs':blogs})

def detail(request,id):
    blog=get_object_or_404(Blog, pk=id)
    #id 값이 있는 blog의 값을 가져오거나 404에러를 띄워라
    #pk : primary key - row 하나하나의 값 구분
    #(row의 id와 같은 개념)
    return render(request,'detail.html.',{'blog':blog})
    #query set이 아닌 object 가져오게 된다

def new(request):
    form = BlogForm()
    return render(request,'new.html',{'form':form})

def create(request):
    form=BlogForm(request.POST,request.FILES)
    if form.is_valid():
        new_blog=form.save(commit=False)
        new_blog.pub_date=timezone.now()
        new_blog.save()
        return redirect('detail',new_blog.id)
    return redirect('home')
    # new_blog=Blog()
    # new_blog.title= request.POST['title']
    # new_blog.writer= request.POST['writer']
    # new_blog.body= request.POST['body']
    # new_blog.pub_date=timezone.now() #django 제공모듈    
    # new_blog.image=request.FILES['image']
    # new_blog.save() 
    # #return + 어떤 화면으로 이동할건데? ↓
    #원래 있던 페이지로 돌아갈 것임 = redirect
    #html새로 만들어서 가는거여 = render
    # return redirect('detail',new_blog.id)

def edit(request,id): #edit.html을 띄우는 함수지만, id를 받아와야함
    edit_blog=Blog.objects.get(id=id)
    return render(request,'edit.html',{'blog':edit_blog})

def update(request,id):
    update_blog=Blog.objects.get(id=id)
    update_blog.title=request.POST['title']
    update_blog.writer= request.POST['writer']
    update_blog.body= request.POST['body']
    update_blog.pub_date=timezone.now() 
    update_blog.save() 
    return redirect('detail',update_blog.id)

def delete(request,id):
    delete_blog=Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')
