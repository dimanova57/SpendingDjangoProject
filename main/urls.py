from django.urls import path
from .views import MainView, HistoryViev, CreateTransactionView, SearchTransactionsView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('history/', HistoryViev.as_view(), name='history'),
    path('create_transaction/', CreateTransactionView.as_view()),
    path('search/', SearchTransactionsView.as_view())
]

