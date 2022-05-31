from django.conf import settings
from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('', views.indexView.as_view(), name= 'index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)