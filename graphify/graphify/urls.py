from django.conf.urls import handler404, handler500, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('graph.urls')), # redirect to app
]

handler404 = v.error_404
handler500 = v.error_500
