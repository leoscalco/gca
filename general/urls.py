from django.conf.urls import url
from general import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^documentos/$', views.ListDoc.as_view(), name='docs'),
    url(r'^classificados/$', views.ListClassified.as_view(), name='class'),
    url(r'^loja/$', views.ListProduct.as_view(), name='products'),
    url(r'^dicas/$', views.tips, name='tips')
]