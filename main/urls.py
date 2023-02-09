from django.urls import path
from main.views import HomeView, SuccessView, CancelView, buy, DetailItemView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('item/<int:pk>/', DetailItemView.as_view(), name='item'),
    path('buy/<int:pk>/', buy, name='buy'),
    path('success_page/', SuccessView.as_view(), name='success'),
    path('cancel_page/', CancelView.as_view(), name='cancel'),
]
