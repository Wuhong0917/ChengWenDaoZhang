from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post, Blog_Category, TK_Video, TK_Category
from .forms import PostForm
from django.utils import timezone
from datetime import timedelta

def blogs(request):
	post_list = Post.objects.filter(is_published=True)
	paginator = Paginator(post_list, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
    
	context = {
		'page_obj': page_obj,
		'blog_categories': Blog_Category.objects.all(),
		'tk_categories' :  TK_Category.objects.all(),
		'recent_posts': Post.objects.filter(is_published=True)[:5],
	}
	return render(request, 'blogs.html', context)

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk, is_published=True)
	post.increase_views()

	context = {
		'post': post,
		'blog_categories': Blog_Category.objects.all(),
		'tk_categories' :  TK_Category.objects.all(),
		'recent_posts': Post.objects.filter(is_published=True)[:5],
	}
	return render(request, 'blogpost_detail.html', context)


def category_posts(request, category_name):
	category = get_object_or_404(Blog_Category, name=category_name)
	post_list = Post.objects.filter(category=category, is_published=True)

	paginator = Paginator(post_list, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {
		'category': category,
		'page_obj': page_obj,
		'blog_categories': Blog_Category.objects.all(),
		'tk_categories' : TK_Category.objects.all(),
		'recent_posts': Post.objects.filter(is_published=True)[:5],
	}
	return render(request, 'blogcategory.html', context)


def all_videos(request):
    video_list = TK_Video.objects.all()
    paginator = Paginator(video_list, 6)  # 6 videos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = get_common_context()
    context.update({
        'page_obj': page_obj,
        'video_count': video_list.count(),
        'tk_categories' :  TK_Category.objects.all(),
        'blog_categories': Blog_Category.objects.all(),
    })
    return render(request, 'all_videos.html', context)


def category_videos(request, category_name):
    category = get_object_or_404(TK_Category, name=category_name)
    video_list = TK_Video.objects.filter(category=category)
    
    paginator = Paginator(video_list, 6)  # 6 videos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = get_common_context()
    context.update({
        'category': category,
        'page_obj': page_obj,
        'video_count': video_list.count(),
        'tk_categories' :  TK_Category.objects.all(),
        'blog_categories': Blog_Category.objects.all(),
    })
    return render(request, 'category_videos.html', context)




@login_required
def create_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
    
	context = {
		'form': form,
		'blog_categories': Blog_Category.objects.all(),
		'tk_categories' :  TK_Category.objects.all(),
		'recent_posts': Post.objects.filter(is_published=True)[:5],
	}
	return render(request, 'create_post.html', context)



def home(request):
	context = get_common_context()
	return render(request, 'home.html', context)


def shijie(request):
	context = get_common_context()
	return render(request, 'shijie.html', context)


def service(request):
	context = get_common_context()
	return render(request, 'service.html', context)

def contactus(request):
	context = get_common_context()
	return render(request, 'contactus.html', context)



# def get_common_context():
#     """获取公共上下文数据"""
#     return {
        
#     }


def get_common_context():
	latest_post = Post.objects.filter(is_published=True).order_by('-created_at').first()
	latest_video = TK_Video.objects.all().order_by('-created_at').first()
    
	return {
		'latest_post': latest_post,
		'latest_video': latest_video,
		'blog_categories': Blog_Category.objects.all(),
		'tk_categories' : TK_Category.objects.all(),
    }