from django.db.models import F, Avg
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from bewertung_app.forms import ProductForm, VotingForm
from bewertung_app.models import Product, Voting


# Create your views here.

def home(request):
    return HttpResponse("Hallo")



class ProductView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "products.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(stars=Avg("voting__stars"))

class VotingView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "votings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["votings"] = Voting.objects.filter(product=self.object)
        return context

class AddProduct(CreateView):
    form_class = ProductForm
    success_url = "/"
    template_name = "add_product.html"

def add_voting(request, pk: int):
    product = get_object_or_404(Product, id=pk)
    if request.method == "POST":
        form = VotingForm(request.POST)
        if form.is_valid():
            new_voting = form.save(commit=False)
            new_voting.product = product
            new_voting.save()
        else:
            # Todo error Handling
            pass
    form = VotingForm()
    return render(request, "add_voting.html", {"form": form, "product": product})

class DeleteProduct(DeleteView):
    model = Product
    template_name = "delete_product.html"
    success_url = "/"

class DeleteVoting(DeleteView):
    model = Voting
    template_name = "delete_voting.html"

    def get_success_url(self):
        pk = self.object.product.pk
        return reverse("votings", kwargs={"pk": pk})