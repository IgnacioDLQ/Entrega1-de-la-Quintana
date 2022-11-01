from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from profesor.models import Person
from person.forms import PersonForm


class PersonListView(ListView):
    model = Person
    paginate_by = 3


class PersonDetailView(DetailView):
    model = Person
    fields = ["name", "last_name", "email", "birth_date"]


class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Person
    success_url = reverse_lazy("person:person-list")

    form_class = PersonForm

    def form_valid(self, form):
        """Filter to avoid duplicate persons"""
        data = form.cleaned_data
        actual_objects = Person.objects.filter(
            name=data["name"],
            last_name=data["last_name"],
            email=data["email"],
            birth_date=["birth_date"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La persona {data['name']} {data['last_name']} | {data['email']} | {data['birth_date']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Person: {data['name']} - {data['last_name']}. Creado exitosamente!",
            )
            return super().form_valid(form)


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ["name", "last_name", "email", "birth_date"]

    def get_success_url(self):
        person_id = self.kwargs["pk"]
        return reverse_lazy("person:person-detail", kwargs={"pk": person_id})


class PersonDeleteView(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy("person:person-list")
