from django.urls import path

from student import views

app_name = "student"
urlpatterns = [
    path("banks", views.BankListView.as_view(), name="bank-list"),
    path("bank/add/", views.BankCreateView.as_view(), name="bank-add"),
    path("bank/<int:pk>/detail/", views.BankDetailView.as_view(), name="bank-detail"),
    path("bank/<int:pk>/update/", views.BankUpdateView.as_view(), name="bank-update"),
    path("bank/<int:pk>/delete/", views.BankDeleteView.as_view(), name="bank-delete"),
]
