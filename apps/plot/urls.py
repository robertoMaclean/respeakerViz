from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='upload_file'),
    path('plot/', views.plot, name='plot'),
    path('plot/interactions', views.interactions, name='interactions'),
    path('plot/interv', views.interv, name='interv'),
    path('plot/barGraph', views.bar_graph, name='bar_graph'),
    path('plot/lineGraph', views.line_graph, name='line_graph'),
    path('plot/donutGraph', views.donut_graph, name='donut_graph'),
    path('plot/flare.json', views.flare_json, name=''),

]

if settings.DEBUG:
	print(settings.MEDIA_ROOT, settings.STATIC_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)