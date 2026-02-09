from django.urls import path
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path('contact/',ContactList.as_view()),
    path('contact/create/',ContactCreate.as_view()),
    path('contact/<int:pk>/',ContactDetail.as_view()),
    path('contact/<int:pk>/delete/',ContactDelete.as_view()),
    path('contact/<int:pk>/update/',ContactUpdate.as_view()),
    path('fbv/contact/', contact_list_fbv),
    path('fbv/contact/create',contact_create_fbv),
    path('fbv/contact/<int:pk>/update',contact_update_fbv),
    path('fbv/contact/<int:pk>/delete',contact_delete_fbv),
    path('generic/contacts/',ContactListCreate.as_view()),
    path('generic/contacts/<int:pk>/',ContactDetailUpdate.as_view()),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh',TokenRefreshView.as_view()),
]
