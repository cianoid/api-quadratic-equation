from django.urls import include, path

from api.views import SolutionView

app_name = 'api'

equation_pattern = [path('equation/', SolutionView.as_view(), name='equation')]


urlpatterns = [
    path('v1.0/', include(equation_pattern)),
]
