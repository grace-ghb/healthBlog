from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Post


# class PostList(generic.ListView):
    # model = Post
    # queryset = Post.objects.filter(status=1).order_by('created_on')
    # template_name = 'about.html'
    # paginated_by = 3


# class Index(TemplateView):
    # template_name = 'about/about.html'

def about(request):
    return render(request, '/home/about.html')
