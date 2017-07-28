"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from rest_framework import routers

from pagamentos.views import PagamentoViewSet, ServidorViewSet, UnidadeGestoraMunicipioViewSet, FolhaMunicipioViewSet, PagamentoPorServidor, PagamentoPorUnidadeGestora, PagamentoUnidadeGestoraInfo, PagamentoServidorInfo

router = routers.DefaultRouter()
router.register(r'pagamentos', PagamentoViewSet, base_name='pagamentos')
router.register(r'servidores', ServidorViewSet, base_name='servidores')
router.register(r'unidadesgestoras', UnidadeGestoraMunicipioViewSet, base_name='unidadesgestoras')
router.register(r'folhas', FolhaMunicipioViewSet, base_name='folhas')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pagamentos/servidor/(?P<servidor_id>[0-9]+)$', PagamentoPorServidor.as_view({'get': 'list'})),
    url(r'^pagamentos/unidade/(?P<unidade_id>[0-9]+)$', PagamentoPorUnidadeGestora.as_view({'get': 'list'})),
    url(r'^pagamentos_info/unidade/(?P<unidade_id>[0-9]+)$', PagamentoUnidadeGestoraInfo.as_view()),
    url(r'^pagamentos_info/servidor/(?P<servidor_id>[0-9]+)$', PagamentoServidorInfo.as_view())
]

