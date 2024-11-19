from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.models import User 
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormView
# Create your views here.


class ReservationFormView(FormView):
    template_name = 'reservation.html'
    form_class = ReservationForm
    success_url = '/reservation/manage_reservations'

    def form_valid(self, form):
        form = form.save(commit=False)
        user = User.objects.get(username=self.request.user.username)
        form.user = user

        form.save()
        return super().form_valid(form)


class ReservationRequestView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation.html'
    reservation_confirmation = '/manage_reservations'
    reservation_message = 'Booking Confirmed'
    success_url = reverse_lazy('manage_reservations')


class ManageReservation(ListView):
    model = Reservation
    template_name = 'manage_reservations.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(user=self.request.user)
        context_object_name = "object_list"
        
        return queryset

        



    
class EditReservation(SuccessMessageMixin, ListView):
    model = Reservation 
    form_class = ReservationForm
    template_name = 'edit_reservation.html'
    success_url = reverse_lazy('manage_reservation')
    reservation_message = 'Reservation Updated!'


class DeleteReservation(SuccessMessageMixin, DeleteView):
    model = Reservation
    template_name = 'delete_reservation.html'
    success_url = reverse_lazy('manage_reservations')