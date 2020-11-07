from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
# messages framework
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# class-based generic views
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# import models
from django.contrib.auth.models import User
from ..models import Post, Comment, Postlike 
from ..forms import CommentForm


################## posts crud views ################## 
class PostList(ListView): # retrieve all posts
    model = Post
    template_name = 'blog/post/post_list.html'
    context_object_name = 'post_list'
    paginate_by = 5


class PostDetail(DetailView): # retrieve post detail
    model = Post
    template_name = 'blog/post/post_detail.html'
    context_object_name = 'post'


class PostCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView): # create post 
    model = Post
    template_name = 'blog/post/post_form_create.html' 
    fields = ['title', 'body']
    success_message = "Post was created successfully"

    def form_valid(self, form):
        form.instance.owner = self.request.user # add post owner manually
        return super().form_valid(form)


class PostUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView): # update post 
    model = Post
    template_name = 'blog/post/post_form_update.html' 
    fields = ['title', 'body']
    success_message = "Post was updated successfully"

    def form_valid(self, form):
        # user should be the post owner 
        if form.instance.owner == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse('You are not post owner')

# delete post 
class PostDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post/post_confirm_delete.html' 
    success_message = "Post was deleted successfully"
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        # user should be the post owner 
        if form.instance.publisher == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse('You are not post owner')


