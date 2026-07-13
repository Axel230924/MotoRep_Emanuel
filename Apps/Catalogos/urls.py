from django.urls import path, include

urlpatterns = [
    path('Caja/', include ('Apps.Catalogos.Caja.urls')),
]