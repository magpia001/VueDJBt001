import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView, ListView

from blog.models import Post, Category, Tag


class HomeView(ListView):

    model = Post
    ordering = '-pk'
    template_name = 'home.html'

class VueTest(TemplateView):
    template_name = 'vue_test.html'
    # template_name = 'vue_test1.html'
