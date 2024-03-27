from django.contrib import admin
from django.urls import path, include

from celula.views import usuarios

urlpatterns = [

    path('cftdc/', include('cftdc.urls')),
    # path('celula/', include('celula.urls')),
    path('admin/', admin.site.urls),

]
