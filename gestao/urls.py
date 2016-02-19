from django.conf.urls import url
from views import *
from . import views, auth

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^scenario/$', views.scenario, name='scenario'),
    url(r'^professores/$', ListTeacher.as_view(), name='teachers'),
    url(r'^alunos/$', ListStudent.as_view(), name='students'),
    url(r'^disciplinas/$', ListDiscipline.as_view(), name='disciplines'),
    url(r'^turmas/$', ListClass.as_view(), name='classes'),
    url(r'^turmas/(?P<pk>\d+)/$', DetailClass.as_view(), name='detail_class'),
     url(r'^provas/$', ListTest.as_view(), name='tests'),
    url(r'^provas/(?P<pk>\d+)/$', DetailTest.as_view(), name='detail_class'),
    url(r'^provas/(?P<pk>\d+)/download/$', views.test_download, name='test_download'),
    url(r'^alunos/(?P<pk>\d+)/$', DetailStudent.as_view(), name='detail_student'),
    url(r'^disciplinas/(?P<post_id>\d+)/$', DetailDiscipline.as_view(), name='detail_discipline'),
    url(r'^professores/(?P<pk>\d+)/$', DetailTeacher.as_view(), name='detail_teacher'),
    url(r'^login/$', auth.get_in, name='login'),
    url(r'^logout/$', auth.get_out, name='logout'),
    url(r'^change_pass/$', auth.change_pass, name='change_pass'),
    url(r'^editar/$', views.edit, name='edit'),
]