from django.urls import path
from .import views
from django.contrib.auth.models import User


urlpatterns = [
    path('', views.ReservationFormView.as_view(), name='reservation'),
    path('manage_reservations/', views.ManageReservation.as_view(),
         name='manage_reservations'),
    path('update/<int:pk>', views.EditReservation.as_view(),
         name='edit_reservation'),
    path('delete_reservation/<int:pk>', views.DeleteReservation.as_view(),
         name='delete_reservation'),
]
