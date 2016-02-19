# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from django.http import HttpResponse


def index(request):
    context = ''
    return render(request, 'gestao/index.html', context)


def scenario(request):
    context = ''
    message = 'Testar message'
    if request.user.is_authenticated():
        events = Event.objects.all().order_by('-date')[:6]
        disciplines = Discipline.objects.all()
        tests = Test.objects.all().order_by('-date')[:10]
        context = {'events': events, 'disciplines': disciplines, 'tests':tests}
        return render(request, 'gestao/scenario.html', context)
    else:
        message = "Login necessário"
        return HttpResponseRedirect('/gestao', message)


class ListTeacher(LoginRequiredMixin, generic.ListView):
    login_url = "/gestao/"
    redirect_field_name = 'redirect_to'
    template_name = "gestao/teacher/list.html"
    context_object_name = 'teachers'
    paginate_by = 20

    def get_queryset(self):
        return Teacher.objects.all()

class ListStudent(LoginRequiredMixin, generic.ListView):
    login_url = "/gestao/"
    redirect_field_name = 'redirect_to'
    template_name = "gestao/student/list.html"
    context_object_name = 'students'
    paginate_by = 20

    def get_queryset(self):
        return Student.objects.all()

class ListDiscipline(LoginRequiredMixin, generic.ListView):
    login_url = "/gestao/"
    redirect_field_name = 'redirect_to'
    template_name = "gestao/discipline/list.html"
    context_object_name = 'disciplines'
    paginate_by = 20

    def get_queryset(self):
        return Discipline.objects.all()

class ListClass(LoginRequiredMixin, generic.ListView):
    login_url = "/gestao/"
    redirect_field_name = 'redirect_to'
    template_name = "gestao/class/list.html"
    context_object_name = 'classes'
    paginate_by = 20

    def get_queryset(self):
        return Class.objects.all()

class ListTest(LoginRequiredMixin, generic.ListView):
    login_url = "/gestao/"
    redirect_field_name = 'redirect_to'
    template_name = "gestao/test/list.html"
    context_object_name = 'tests'
    paginate_by = 20

    def get_queryset(self):
        return Test.objects.all()

class DetailClass(LoginRequiredMixin, generic.DetailView):
    login_url = "/gestao/"
    redirect_field_name = 'redirect_to'
    model = Class
    template_name = "gestao/class/detalhe.html"

    def get_context_data(self, **kwargs):
        object = self.model.objects.get(id=self.kwargs.get("pk"))
        tests = Test.objects.filter(discipline=object.discipline.id, teacher=object.teacher.id)
        context = {
                    'object':object,
                    'tests':tests,
                   }
        return context

class DetailStudent(LoginRequiredMixin, generic.DetailView):
    login_url = "/gestao/"
    redirect_field_name = 'redirect_to'
    model = Student
    template_name = "gestao/student/detalhe.html"

    def get_context_data(self, **kwargs):
        context = super(DetailStudent, self).get_context_data(**kwargs)
        return context

class DetailDiscipline(LoginRequiredMixin, generic.DetailView):
    login_url = "/gestao/"
    redirect_field_name = 'redirect_to'
    model = Discipline
    template_name = "gestao/discipline/detalhe.html"
    pk_url_kwarg = 'post_id'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        tests = Test.objects.filter(discipline=self.kwargs.get("post_id"))
        object = self.model.objects.get(id=self.kwargs.get("post_id"))
        context = {
                    'object':object,
                    'tests':tests,
                   }
        return context

class DetailTeacher(LoginRequiredMixin, generic.DetailView):
    login_url = "/gestao/"
    redirect_field_name = 'redirect_to'
    model = Teacher
    template_name = "gestao/teacher/detalhe.html"

    def get_context_data(self, **kwargs):
        context = super(DetailTeacher, self).get_context_data(**kwargs)
        return context

class DetailTest(LoginRequiredMixin, generic.DetailView):
    login_url = "/gestao/"
    redirect_field_name = 'redirect_to'
    model = Test
    template_name = "gestao/test/detalhe.html"

    def get_context_data(self, **kwargs):
        context = super(DetailTest, self).get_context_data(**kwargs)
        return context

def test_download(request, pk):
    test = Test.objects.get(id=pk)
    fsock = open(test.file.path, 'r')
    response = HttpResponse(fsock, content_type='application/zip')
    response['Content-Disposition'] = "attachment; filename=%s.zip" % test.name
    return response

def edit(request):
    context = {'user': request.user}
    return render(request, 'gestao/user/change_pass.html', context)