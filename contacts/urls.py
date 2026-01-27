from django.urls import path
from .views import *

urlpatterns = [
    path('hello/',Hello.as_view()),#as
    path('goodbye/',Goodbye.as_view()),
    path('hi/',Hi.as_view()),
    path('stud/',Stud.as_view()),
    path('info/',Info.as_view()),
    path('contact/',ContactList.as_view()),
    path('contacts/create/',ContactCreate.as_view()),
    path('contact/<int:pk>/',ContactDetail.as_view()),
    path('contact/<int:pk>/delete/',ContactDelete.as_view()),
]
