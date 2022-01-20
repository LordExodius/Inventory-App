from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item_id>/", views.itemView, name="itemView"),
    path("exportCSV/", views.exportCSV, name="exportCSV"),
]