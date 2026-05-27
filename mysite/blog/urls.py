from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("api/articoli", views.ArticoloViewSet)


urlpatterns = [
    path("articoli/", views.lista_articoli, name="lista"),
]

urlpatterns += router.urls
