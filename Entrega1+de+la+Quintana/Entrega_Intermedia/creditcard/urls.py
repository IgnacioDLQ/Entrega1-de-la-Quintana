from django.urls import path

from creditcard import views

app_name = "creditcard"
urlpatterns = [
    path("creditcard/", views.creditcardListView.as_view(), name="creditcard-list"),
    path("creditcard/add/", views.creditcardCreateView.as_view(), name="creditcard-add"),
    path("creditcard/<int:pk>/detail/", views.creditcardDetailView.as_view(), name="creditcard-detail"),
    path("creditcard/<int:pk>/update/", views.creditcardUpdateView.as_view(), name="creditcard-update"),
    path("creditcard/<int:pk>/delete/", views.creditcardDeleteView.as_view(), name="creditcard-delete"),
]