from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # ex: /polls/
    path('apiroot/', views.api_root, name='apiroot'),
    path('apiroot2/', views.api_root2, name='apiroot2'),
    path('file/', views.simple_upload, name='file'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        