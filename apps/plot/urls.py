from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='upload_file'),
    path('plot/', views.plot, name='plot')
]

if settings.DEBUG:
	print(settings.STATIC_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)