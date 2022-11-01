from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from creditcard.forms import CommentForm
from creditcard.forms import CreditCardForm
from creditcard.models import CreditCard


class CreditCardListView(ListView):
    model = creditcard
    paginate_by = 3


class CreditCardDetailView(DetailView):
    model = CreditCard
    template_name = "creditcard/creditcard_detail.html"
    fields = ["name", "code", "description"]

    def get(self, request, pk):
        creditcard = creditcard.objects.get(id=pk)
        comments = Comment.objects.filter(creditcard=creditcard).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "creditcard": creditcard,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)


class CreditCardCreateView(LoginRequiredMixin, CreateView):
    model = CreditCard
    success_url = reverse_lazy("creditcard:creditcard-list")

    form_class = CreditCardForm
    
    def form_valid(self, form):
        """Filter to avoid duplicate creditcards"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = CreditCard.objects.filter(
            name=data["name"], code=data["code"], expire_date=data["expire_date"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La Tarjeta de credito {data['name']} - {data['code']} - {data['expire_date']} ya está en la base de datos",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"La tarjeta de credito {data['name']} - {data['code']} a sido subida exitosamente!",
            )
            return super().form_valid(form)


class CreditCardUpdateView(LoginRequiredMixin, UpdateView):
    model = CreditCard
    fields = ["name", "code", "description"]

    def get_success_url(self):
        creditcard_id = self.kwargs["pk"]
        return reverse_lazy("creditcard:creditcard-detail", kwargs={"pk": creditcard_id})


class CreditCardDeleteView(LoginRequiredMixin, DeleteView):
    model = CreditCard
    success_url = reverse_lazy("creditcard:creditcard-list")
