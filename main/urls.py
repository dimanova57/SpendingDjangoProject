from django.urls import path
from .views import MainView, HistoryViev, CreateTransactionView, SearchTransactionsView, DeleteTransactionView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('history/', HistoryViev.as_view(), name='history'),
    path('create_transaction/', CreateTransactionView.as_view()),
    path('search/', SearchTransactionsView.as_view()),
    path('delete_transaction/', DeleteTransactionView.as_view()),
]

