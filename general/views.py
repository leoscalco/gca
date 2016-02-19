from django.shortcuts import render
from django.http import HttpResponseRedirect
from gestao.models import *
from django.views import generic
# Create your views here.

def index(request):
    context = ''
    news = New.objects.all().order_by('-post_date')[:10]
    context = {'news':news}
    return render(request, 'general/index.html', context)

def tips(request):
    context = ''
    return render(request, 'general/tips.html', context)

class ListDoc(generic.ListView):
    template_name = "general/doc/list.html"
    context_object_name = 'docs'
    paginate_by = 24

    def get_queryset(self):
        return Document.objects.all().order_by("-post_date")

class ListClassified(generic.ListView):
    template_name = "general/class/list.html"
    context_object_name = 'classifieds'
    paginate_by = 20

    def get_queryset(self):
        return Classified.objects.all().order_by("-id")

class ListProduct(generic.ListView):
    template_name = "general/store/list.html"
    context_object_name = 'products'
    paginate_by = 20

    def get_queryset(self):
        return Product.objects.all()