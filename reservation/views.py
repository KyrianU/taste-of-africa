from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ReservationForm
from .models import Reservation
from django.contrib.auth.models import user 
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormView
# Create your views here.


class ReservationFormView(FormView):
    template_name = ''
    form_class = ReservationForm
    successful_url = ''

    def form_valid(self, form):
        form = form.save(commit=false)
        user = User.objects.get(username=self.request.user.username)
        form.user = user

        form.save()
        return super().form_valid(form)


class ReservationRequestView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = ''
    reservation_confirmation = ''
    reservation_message = ''


class ManageReservation(ListView):
    model = Reservation
    template_name = ''

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs,filter(user=self.request.user)

    
class EditReservation(SuccessMessageMixin, ListView):
    model = Reservation 
    form_class = ReservationForm
    template_name = ''
    success_url = reverse_lazy('')
    reservation_message = 'Reservation Updated!'


class DeleteReservation(SuccessMessageMixin, DeleteView):
    model = Reservation
    template_name = ''
    success_url = reverse_lazy('')