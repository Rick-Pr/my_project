from django.urls import path, include
# from . import

urlpatterns = [
    path('', include("tts.urls"), name="home"),
    path('admin/', include("tts.urls"), name="admin"),
    path('download/', include("tts.urls"), name="download"),
]
