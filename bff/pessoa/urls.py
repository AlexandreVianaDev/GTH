from django.urls import path
from .views import PessoaView, PessoaDetailView

urlpatterns = [
    path("pessoa/", PessoaView.as_view(), name="pessoa"),
    path("pessoa/<int:id>/", PessoaDetailView.as_view(), name="pessoa_detail"),
]
