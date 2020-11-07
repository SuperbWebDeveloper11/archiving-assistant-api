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



# render comment list template
def render_comment_list_temp(request, *args, **kwargs): 
    data = dict()
    data['form_is_valid'] = True
    current_post = get_object_or_404(Post, pk=kwargs['pk'])
    comment_list = Comment.objects.filter(post=current_post)
    context = {'comment_list': comment_list}
    data['list_temp'] = render_to_string('blog/comment/comment_list.html', context, request=request)
    return JsonResponse(data)
 

# render comment create template
def render_comment_create_temp(request, *args, **kwargs): 
    data = dict()
    comment_create_temp = 'blog/comment/comment_create.html'
    comment_form = CommentForm()
    context = {'form': comment_form, 'post_pk': kwargs['pk']}
    data['temp'] = render_to_string(comment_create_temp, context, request=request)
    return JsonResponse(data)


# render comment update template
def render_comment_update_temp(request, *args, **kwargs): 
    data = dict()
    comment_instance = get_object_or_404(Comment, pk=kwargs['comment_pk'])
    comment_form = CommentForm(instance=comment_instance)
    context = {'form': comment_form, 'post_pk': kwargs['pk']}
    data['temp'] = render_to_string('blog/comment/comment_update.html', context, request=request)
    return JsonResponse(data)


# render comment delete template
def render_comment_delete_temp(request, *args, **kwargs): 
    data = dict()
    comment_instance = get_object_or_404(Comment, pk=kwargs['comment_pk'])
    comment_form = CommentForm(instance=comment_instance)
    context = {'form': comment_form, 'post_pk': kwargs['pk'], 'comment_pk': kwargs['comment_pk']}
    data['temp'] = render_to_string('blog/comment/comment_delete.html', context, request=request)
    return JsonResponse(data)


################## comments crud views ################## 

class CommentList(View):
    def get(self, request, *args, **kwargs): 
        return render_comment_list_temp(request, *args, **kwargs)
    

class CommentCreate(LoginRequiredMixin, View):
    data = dict()
    def get(self, request, *args, **kwargs): 
        return render_comment_create_temp(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid(): # create new comment
            current_post = get_object_or_404(Post, pk=kwargs['pk'])
            form.instance.post = current_post
            form.instance.owner = request.user
            form.save()
            # render comment list template
            return render_comment_list_temp(request, *args, **kwargs)
        else:
            # rerender comment_create.html for user with errors
            self.data['form_is_valid'] = False
            context = {'form': comment_form, 'post_pk': kwargs['pk']}
            self.data['temp'] = render_to_string('blog/comment/comment_create.html', context, request=request)
            return JsonResponse(self.data)


class CommentUpdate(LoginRequiredMixin, View):
    data = dict()
    def get(self, request, *args, **kwargs): # render comment_create.html for user
        return render_comment_update_temp(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        current_post = get_object_or_404(Post, pk=kwargs['pk'])
        comment_instance = Comment.objects.get(post=current_post, pk=kwargs['comment_pk'])
        form = CommentForm(request.POST, instance=comment_instance)
        if form.is_valid():
            if not request.user == comment_instance.owner:
                return HttpResponse('You can not edit this comment')
            # update comment
            form.save()
            # render comment list template
            return render_comment_list_temp(request, *args, **kwargs)
        else:
            # rerender comment_update.html for user with errors
            self.data['form_is_valid'] = False
            context = {'form': comment_form, 'post_pk': kwargs['pk'], 'comment_pk': kwargs['comment_pk']}
            self.data['temp'] = render_to_string('blog/comment/comment_update.html', context, request=request)
            return JsonResponse(self.data)


class CommentDelete(LoginRequiredMixin, View):
    data = dict()
    def get(self, request, *args, **kwargs): 
        return render_comment_delete_temp(request, *args, **kwargs)
    def post(self, request, *args, **kwargs): # delete comment and render partial_comment_list.html if success
        comment_instance = get_object_or_404(Comment, pk=kwargs['comment_pk'])
        if not request.user == comment_instance.owner:
            return HttpResponse('You can not delete this comment')
        # delete comment
        comment_instance.delete()
        # render comment list template
        return render_comment_list_temp(request, *args, **kwargs)

