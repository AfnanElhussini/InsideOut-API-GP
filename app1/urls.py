from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # ex: /polls/
    path('Emotion/', views.Get_Emotion, name='Emotion'),
    path('apiroot2/', views.api_root2, name='apiroot2'),
    path('file/', views.simple_upload, name='file'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        