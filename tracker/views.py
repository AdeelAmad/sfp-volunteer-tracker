import collections
import datetime as dt
from datetime import datetime, date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from .models import volunteer_hour

# Create your views here.
@login_required
def hours(request):
    context = {}

    context['hours'] = []

    verified_hours = dt.timedelta(0)

    for o in volunteer_hour.objects.all().filter(volunteer=request.user.volunteer, verified=True):
        date = o.date
        hour = datetime.combine(date, o.end) - datetime.combine(date, o.start)
        verified_hours = verified_hours + hour

    context['verified_hours'] = verified_hours.seconds/3600

    for o in volunteer_hour.objects.all().filter(volunteer=request.user.volunteer).order_by('date'):
        date = o.date
        start = o.start
        end = o.end
        try:
            total = datetime.combine(date, o.end) - datetime.combine(date, o.start)
        except:
            total = "Null"
        verified = o.verified

        context['hours'].append({"date": date, "start": start, "end": end, "total": total, "verified": verified})

    return render(request, template_name='tracker/hours.html', context=context)



class createHour(LoginRequiredMixin, CreateView):
    model = volunteer_hour
    fields = ['date','start','end']

    def form_valid(self, form):
        form.instance.volunteer = self.request.user.volunteer
        messages.add_message(self.request, messages.INFO, 'Hours have been logged. They will be verified soon.')
        return super().form_valid(form)
