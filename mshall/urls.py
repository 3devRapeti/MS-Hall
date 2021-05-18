from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home'),
    path('gallery/',views.gallery, name='gallery'),
    path('noticehn/',views.halln, name='halln'),
    path('noticegc/',views.gcn, name='gcn'),
    path('noticemn/',views.messn, name='messn'),
    path('noticegn/',views.genn, name='genn'),
    path('hall_of_fame/',views.hof, name='hof')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)