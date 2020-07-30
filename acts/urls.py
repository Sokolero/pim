from django.urls import path
from .views import ActView

app_name = 'acts'

urlpatterns = [
    path('create/', ActView.as_view(), name='act')
]
