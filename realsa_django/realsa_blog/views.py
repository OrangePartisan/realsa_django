from django.shortcuts import render
#from django.http import HttpResponse

from .models import RealsaBlog

# Create your views here.
def blog(request):
    #return HttpResponse('Hello from realsa_blog app!')

    realsa_blog_posts = RealsaBlog.objects.all()[:10]

    context = {
        'title': 'Comments',
        'realsa_blogs': realsa_blog_posts
    }

    return render(request, 'realsa_blog/blog.html', context)

def details(request, id):
    post_detail = RealsaBlog.objects.get(id=id)

    context = {
        'post_detail': post_detail
    }

    return render(request, 'realsa_blog/details.html', context)