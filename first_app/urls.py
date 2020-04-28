from django.conf.urls import url
from first_app import views

urlpatterns = [
    url("helps/", views.helps, name="helps")
]
