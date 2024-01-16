from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Post

class LandingView(generic.TemplateView):
    template_name = "blog/landing.html"
    context_object_name = "landing"

class PostView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "latest_blog_post_list"

    def get_queryset(self):
        return Post.objects.order_by("-pub_date")[:5]

