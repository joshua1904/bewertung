from django.forms import ModelForm

from bewertung_app.models import Product, Voting, User


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class VotingForm(ModelForm):
    class Meta:
        model = Voting
        exclude = ["product"]

class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ["product"]