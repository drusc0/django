from django.shortcuts import reverse, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from django_tables2 import RequestConfig

from .models import Tags, Note
from .forms import NoteForm, TagForm
from .table import TagsTable


@method_decorator(staff_member_required, name='dispatch')
class NoteHomepageView(ListView):
    template_name = 'notes/homepage.html'
    model = Note

    def get_queryset(self):
        qs = Note.objects.all()
        qs = Note.filters_data(self.request, qs)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_form'] = NoteForm()
        context['pinned_qs'] = self.object_list.filter(pinned=True)
        context['qs'] = self.object_list.filter(pinned=False)[:30]

        return context

