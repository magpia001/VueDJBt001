
from django.views.generic import DetailView
from django.shortcuts import render

from blog.models import Post, Category, Tag


class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDV, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context

    
def category_page(request, slug):
    if slug == "no_category":
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'home.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_cnt': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(
        request,
        'home.html',
        {
            'post_list': post_list,
            'tag': tag,
            'categories': Category.objects.all(),
            'no_category_post_cnt': Post.objects.filter(category=None).count(),
        }
    )