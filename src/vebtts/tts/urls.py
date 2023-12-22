from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

                  path('download/', views.down_audio, name='download'),
                  path('admin/', admin.site.urls),
                  path('', views.index, name='home')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
