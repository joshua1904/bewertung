from django.urls import path
from .views import home, ProductView, VotingView, AddProduct, add_voting, DeleteProduct, DeleteVoting

urlpatterns = [
    path('', ProductView.as_view(), name="products"),
    path("<int:pk>/", VotingView.as_view(), name="votings"),
    path("add-product/", AddProduct.as_view(), name="add_product"),
    path("add-voting/<int:pk>/", add_voting, name="add_voting"),
    path("delete-product/<int:pk>/", DeleteProduct.as_view(), name="delete_product"),
    path("delete-voting/<int:pk>/", DeleteVoting.as_view(), name="delete_voting")
]
