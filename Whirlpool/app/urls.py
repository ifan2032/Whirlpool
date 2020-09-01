from django.urls import path
from . import views

urlpatterns = [
	path("", views.index),
	path("main", views.main, name="main"),
	path("update/<str:url_path>/", views.update, name="update"),
	path("delete/<int:item_id>", views.delete, name="delete")
]

#,	