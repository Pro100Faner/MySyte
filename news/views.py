from django.shortcuts import render, get_object_or_404, redirect
from .forms import TagForm
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailsMixin

# Create your views here.


def news_list(request):
    post = reversed(Post.objects.all())
    return render(request, 'news/index.html', context={'posts': post})


class NewsDetail(ObjectDetailsMixin, View):
    model = Post
    templates = 'news/new_detail.html'


class TagsDetail(ObjectDetailsMixin,View):
    model = Tag
    templates = 'news/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        form = TagForm
        return render(request, 'news/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            news_tag = bound_form.save()
            return redirect(news_tag)
        return render(request, 'news/tag_create.html', context={'form': bound_form})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'news/tags_list.html', context={'tags': tags})
