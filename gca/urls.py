"""gca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from gca_ws import views
from django.conf import settings
from django.conf.urls.static import static
from general import views as viewsG

router = routers.DefaultRouter()
router.register(r'estudantes', views.UserViewSet)
router.register(r'professores', views.TeacherViewSet)
router.register(r'eventos', views.EventViewSet)
router.register(r'provas', views.TestViewSet)
router.register(r'disciplinas', views.DisciplineViewSet)
router.register(r'materias', views.SubjectViewSet)
router.register(r'classes', views.ClassViewSet)

urlpatterns = [
    url(r'^$', viewsG.index, name='index'),
    url(r'^gestao/', include('gestao.urls')),
    url(r'^geral/', include('general.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^gestao/ws/', include(router.urls)),
    url(r'^gestao/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
