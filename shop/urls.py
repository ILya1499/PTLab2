from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('promocode/', views.PromocodeGet.as_view(), name='promocode'),
    path('buy/<int:product_id>/', views.PurchaseCreate.as_view(), name='buy'),
]
