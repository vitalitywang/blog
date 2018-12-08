from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from .forms import ContactForm
import markdown
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 4

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args , **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):

        post = super().get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        post.content = md.convert(post.content)
        post.toc = md.toc
        return post

class ArchivesView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year, created_time__month=month)

class CategoryView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk = self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

class TagView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk = self.kwargs.get('pk'))
        return super().get_queryset().filter(tags=tag)

def about(request):
    return render(request, 'blog/about.html')

def post_contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request,'blog/post_contact.html')
        else:
            return render(request, 'blog/contact.html',{'form': form})
    return render(request, 'blog/contact.html')

def contact(request):
    form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})

def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'blog/index.html', {'error_msg':error_msg})

    post_list = Post.objects.filter(Q(title__icontains = q )|Q(content__icontains=q))
    return render(request, 'blog/index.html', {'error_msg':error_msg,'post_list':post_list})
