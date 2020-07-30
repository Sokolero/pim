from django.urls import path
from . import views

app_name = 'doc_factory'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('add_entry/', views.AddEntryView.as_view(), name='add_entry'),
    path('doc_factory/', views.EntryView.as_view()),
    path('doc_factory/<int:pk>/', views.EntryView.as_view())
]
