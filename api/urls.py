from django.urls import path
from .views import listar_professores, ProfessoresView

urlpatterns = [
    path('professores', listar_professores),
    path('prof', ProfessoresView.as_view()),
]