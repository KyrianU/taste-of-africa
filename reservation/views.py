from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReservationForm
from .models import Reservation


class ReservationFormView(LoginRequiredMixin, FormView):
    template_name = 'reservation.html'
    form_class = ReservationForm
    success_url = '/reservation/manage_reservations'

    def get_initial(self):
        initial = super().get_initial()
        # Pre-fill the "name" field with the user's username
        initial['name'] = self.request.user.username
        return initial

    def form_valid(self, form):
        form = form.save(commit=False)
        user = User.objects.get(username=self.request.user.username)
        form.user = user

        form.save()
        return super().form_valid(form)


class ReservationRequestView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation.html'
    reservation_confirmation = '/manage_reservations'
    reservation_message = 'Booking Confirmed'
    success_url = reverse_lazy('manage_reservations')


class ManageReservation(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'manage_reservations.html'
    context_object_name = "object_list"

    def get_queryset(self):

        return super().get_queryset().filter(user=self.request.user)


class EditReservation(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'edit_reservation.html'
    success_url = reverse_lazy('manage_reservations')
    reservation_message = 'Reservation Updated!'

    def get_queryset(self):
        # Only allow the logged-in user to fetch their own reservations
        return Reservation.objects.filter(user=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            messages.error(
                request,
                "You don't have access to this reservation"
            )
            return redirect('manage_reservations')


class DeleteReservation(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Reservation
    template_name = 'delete_reservation.html'
    success_url = reverse_lazy('manage_reservations')

    def get_queryset(self):
        # Only allow the logged-in user to fetch their own reservations
        return Reservation.objects.filter(user=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Http404:
            messages.error(
                request,
                "You don't have access to this reservation"
            )
            return redirect('manage_reservations')
