from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpRequest
from django.core.paginator import Paginator
from .models import Blog, IpModel
# Create your views here.


def blogList(request):
    blogList = Blog.objects.all().order_by("-blogDate")
    paginator = Paginator(blogList, 6)
    page_number = request.GET.get("page")
    page_blogList = paginator.get_page(page_number)
    return render(request, 'tr/blog/blogList.html', {"page_blogList": page_blogList})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = "blogSingle"
    template_name = "tr/blog/blogSingle.html"
    slug_field = 'blogSlug'
    slug_url_kwarg = 'blogSlug'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        ip = get_client_ip(self.request)
        print(ip)
        if IpModel.objects.filter(ip=ip).exists():
            blog_slug = request.GET.get('blog-slug')
            blog = Blog.objects.get(blogSlug=blog_slug)
            blog.views.add(IpModel.objects.get(ip=ip))
        else:
            IpModel.objects.create(ip=ip)
            blog_slug = request.GET.get('blog-slug')
            blog = Blog.objects.get(blogSlug=blog_slug)
            blog.views.add(IpModel.objects.get(ip=ip))
        return self.render_to_response(context)


def blogPartial(request):
    blogPartial = Blog.objects.all().order_by("-blogDate")[:11]
    return render(request, 'tr/blog/blogPartial.html', {"blogPartial": blogPartial})
