from django.urls import path

from person import views

app_name = "person"
urlpatterns = [
    path("persons", views.personListView.as_view(), name="person-list"),
    path("person/add/", views.PersonCreateView.as_view(), name="person-add"),
    path("person/<int:pk>/detail/", views.PersonDetailView.as_view(), name="person-detail"),
    path("person/<int:pk>/update/", views.PersonUpdateView.as_view(), name="person-update"),
    path("person/<int:pk>/delete/", views.PersonDeleteView.as_view(), name="person-delete"),
]
