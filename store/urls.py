from django.urls import path
from .views import *

urlpatterns = [
    path('product', ProductView.as_view()),
    path('product-details', ProductDetails.as_view())
]