from django.urls import path
from apps.plot import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from apps.accounts import views as accounts_views

urlpatterns = [
    # path('', views.index, name='upload_file'),
    path('', views.save_file, name='save_file'),
    path('plot/', views.plot, name='plot'),
    path('plot/interactions', views.interactions, name='interactions'),
    path('plot/interv', views.interv, name='interv'),
    path('plot/barGraph', views.bar_graph, name='bar_graph'),
    path('plot/lineGraph', views.line_graph, name='line_graph'),
    path('plot/donutGraph', views.donut_graph, name='donut_graph'),
    path('plot/<str:user>/flare.json', views.flare_json, name='flare_json'),
    path('plot/<str:user>/relations', views.relations, name='relations'),
    path('plot/usersActivity', views.usersActivity, name='users_activity'),  
    path('plot/get_files', views.get_files, name='get_files'),
    path('plot/show_graphs/<str:filename>', views.show_graphs, name='show_graphs'),
    path('plot/delete_files/<str:name>', views.delete_files, name='delete_files'),
    path('plot/<str:user>/force.csv', views.force_csv, name='force_csv'),
    path('plot/group_plots', views.group_plots, name='group_plots'),
    path('plot/group_plots/<str:user>/flare.json', views.group_flare_json, name='group_flare_json'),
    path('plot/group_plots/<str:user>/intdur.json', views.intdur_json, name='intdur_json'),
    path('plot/group_plots/<str:user>/volume.json', views.volume_json, name='volume_json'),
    path('plot/group_plots/<str:user>/interv.json', views.interv_json, name='interv_json')
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)