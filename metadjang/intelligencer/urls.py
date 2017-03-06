from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from api import views as api_views
router = routers.DefaultRouter()
router.register(r'log', api_views.LogEntryViewSet, base_name="log")
class AccessUser:
    has_module_perms = has_perm = __getattr__ = lambda s,*a,**kw: True
admin.site.has_permission = lambda r: setattr(r, 'user', AccessUser()) or True
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
]
