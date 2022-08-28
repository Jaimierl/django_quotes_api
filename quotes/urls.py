from django.urls import path
from .views import QuoteList, QuoteDetail

urlpatterns = [
    path('', QuoteList.as_view(), name = "quote_list"),
    path('<int:pk>/', QuoteDetail.as_view(), name = 'quote_detail'),
]