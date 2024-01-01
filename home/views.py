from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginated_by = 3

class Index(TemplateView):
    template_name = 'home/index.html'

# class About(View):
#     def about(request):
#         return render(request, 'about.html')