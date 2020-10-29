from django.shortcuts import render, get_object_or_404
from .models import *


class ObjectDetailsMixin:
    model = None
    templates = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.templates, context={self.model.__name__.lower(): obj})
