from django.urls import path
from .views import *
urlpatterns = [
    path("cv/",cview),
    path("sv/",sview),
    path("hv/",hview),
    path("uv/<int:pk>/",uview),
    path("dv/<int:k>/",dview)

]