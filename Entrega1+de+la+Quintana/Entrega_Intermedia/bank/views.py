from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from student.models import Student
from student.forms import StudentForm


class BankListView(ListView):
    model = Bank
    paginate_by = 3


class BankDetailView(DetailView):
    model = Student
    fields = ["entity"]


class BankCreateView(LoginRequiredMixin, CreateView):
    model = Bank
    success_url = reverse_lazy("bank:bank-list")

    form_class = BankForm

    def form_valid(self, form):
        """Filter to avoid duplicate banks"""
        data = form.cleaned_data
        actual_objects = Bank.objects.filter(
            name=data["entity"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El Banco {data['entity']} ya está registrado",
            )
            form.add_error("entity", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"¡Banco: {data['entity']}. Creado correctamente!",
            )
            return super().form_valid(form)


class BankUpdateView(LoginRequiredMixin, UpdateView):
    model = Bank
    fields = ["entity"]

    def get_success_url(self):
        bank_id = self.kwargs["pk"]
        return reverse_lazy("bank:bank-detail", kwargs={"pk": bank_id})


class BankDeleteView(LoginRequiredMixin, DeleteView):
    model = Bank
    success_url = reverse_lazy("bank:bank-list")
