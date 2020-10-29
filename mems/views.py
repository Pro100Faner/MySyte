from django.shortcuts import render, get_object_or_404, redirect
from .models import MemPost
from django.views.generic import View
from .forms import MemForm


def mems_list(request):
    mems = reversed(MemPost.objects.all())
    return render(request, 'mems/main.html', context={'mems': mems})


class MemsDetail(View):
    def get(self, request, slug):
        mem = get_object_or_404(MemPost, slug__iexact=slug)
        return render(request, 'mems/mem_detail.html', context={'mem': mem})


class MemCreate(View):
    def get(self, request):
        form = MemForm
        return render(request, 'mems/mem_create.html', context={'form': form})

    def post(self, request):
        bound_form = MemForm(request.POST)
        if bound_form.is_valid():
            new_mem = bound_form.save()
            return redirect(new_mem)
        return render(request, 'mems/mem_create.html', context={'form': bound_form})
