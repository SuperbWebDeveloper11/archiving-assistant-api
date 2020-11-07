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
from ..models import Company


################## companys crud views ################## 
class CompanyList(ListView): 
    model = Company
    template_name = 'edoc/company/company_list.html'
    context_object_name = 'company_list'
    paginate_by = 5


class CompanyDetail(DetailView): 
    model = Company
    template_name = 'edoc/company/company_detail.html'
    context_object_name = 'company'


class CompanyCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView): # create company 
    model = Company
    template_name = 'edoc/company/company_form_create.html' 
    fields = ['name', 'abbreviation']
    success_message = "Company was created successfully"


class CompanyUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView): # update company 
    model = Company
    template_name = 'edoc/company/company_form_update.html' 
    fields = ['name', 'abbreviation']
    success_message = "Company was updated successfully"


class CompanyDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Company
    template_name = 'edoc/company/company_confirm_delete.html' 
    success_message = "Company was deleted successfully"
    success_url = reverse_lazy('edoc:company_list')


