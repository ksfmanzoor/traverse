from django.shortcuts import render
import os
from django.views.generic import ListView, DetailView, CreateView
from .models import Experience, Category
from django.conf import settings
from django.shortcuts import get_list_or_404


class ExperienceListView(ListView):
    model = Experience
    template_name = 'experiences/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['category_list'] = Category.objects.all()
        return context


class ExperienceDetailView(DetailView):
    model = Experience
    template_name = 'experiences/exp_page.html'
    context_object_name = 'experience'


class CategoryDetailView(DetailView, ListView):
    model = Category
    template_name = 'experiences/cat_exp_page.html'

    def get_context_data(self, **kwargs):
        context = super.get_context_data(**kwargs)
        context['experience_list'] = Experience.objects.all()


class ExperienceCreateView(CreateView):
    model = Experience
    template_name = 'experiences/experience-create.html'
    fields = ['title', 'name', 'content', 'image', 'date_posted']

    def get_queryset(self):
        categories = get_list_or_404(Category, name=self.kwargs.get('title'))
        return Experience.objects.filter(Category=categories)

