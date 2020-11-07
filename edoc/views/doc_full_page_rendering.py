from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# messages framework
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# class-based generic views
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# import models
from django.contrib.auth.models import User
from ..models import Doc


################## docs crud views ################## 
class DocList(ListView): 
    model = Doc
    template_name = 'edoc/doc/doc_list.html'
    context_object_name = 'doc_list'
    paginate_by = 5


class DocDetail(DetailView): 
    model = Doc
    template_name = 'edoc/doc/doc_detail.html'
    context_object_name = 'doc'


class DocCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView): # create doc 
    model = Doc
    template_name = 'edoc/doc/doc_form_create.html' 
    fields = ['title', 'doc_file', 'source', 'destinations']
    success_message = "Doc was created successfully"


class DocUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView): # update doc 
    model = Doc
    template_name = 'edoc/doc/doc_form_update.html' 
    fields = ['title', 'doc_file', 'source', 'destinations']
    success_message = "Doc was updated successfully"


class DocDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Doc
    template_name = 'edoc/doc/doc_confirm_delete.html' 
    success_message = "Doc was deleted successfully"
    success_url = reverse_lazy('edoc:doc_list')


