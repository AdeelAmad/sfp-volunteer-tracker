from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from tracker.models import volunteer_hour


# Create your views here.
@permission_required('tracker.add_volunteer_hour', raise_exception=True)
def staff_dash(request):
    return render(request, template_name='staff/staff_dash.html')

class review(PermissionRequiredMixin, ListView):
    permission_required = 'tracker.add_volunteer_hour'
    raise_exception = True
    template_name = 'staff/review.html'
    context_object_name = 'hours'

    def get_queryset(self):
        resultList = []

        for o in volunteer_hour.objects.all().filter(verified=False).order_by('date'):

            date = o.date
            start = o.start
            end = o.end
            total = datetime.combine(date, o.end) - datetime.combine(date, o.start)
            name = "{} {}".format(o.volunteer.first_name, o.volunteer.last_name)

            resultList.append({"name": name, "date": date,"start": start,"end": end,"total": total, "id": o.id})

        return resultList

@permission_required('tracker.add_volunteer_hour', raise_exception=True)
def approvehour(request, pk):
    hour = get_object_or_404(volunteer_hour, pk=pk)
    hour.verified = True
    hour.save()
    messages.success(request, 'Hour Approved')
    return redirect(reverse_lazy('review'))

@permission_required('tracker.add_volunteer_hour', raise_exception=True)
def denyhour(request, pk):
    hour = get_object_or_404(volunteer_hour, pk=pk)
    hour.delete()
    messages.success(request, 'Hour Denied')
    return redirect(reverse_lazy('review'))

class allhours(PermissionRequiredMixin, ListView):
    permission_required = 'tracker.add_volunteer_hour'
    raise_exception = True
    template_name = 'staff/allhours.html'
    context_object_name = 'hours'
    paginate_by = 10

    def get_queryset(self):

        filter = self.request.GET.get('filter')

        resultList = []
        if filter:
            for o in volunteer_hour.objects.all().filter(volunteer__first_name=filter).order_by('date'):
                date = o.date
                start = o.start
                end = o.end
                total = datetime.combine(date, o.end) - datetime.combine(date, o.start)
                name = "{} {}".format(o.volunteer.first_name, o.volunteer.last_name)

                resultList.append({"name": name, "date": date, "start": start, "end": end, "total": total, "id": o.id, "verified": o.verified})
        else:
            for o in volunteer_hour.objects.all().order_by('date'):
                date = o.date
                start = o.start
                end = o.end
                total = datetime.combine(date, o.end) - datetime.combine(date, o.start)
                name = "{} {}".format(o.volunteer.first_name, o.volunteer.last_name)

                resultList.append({"name": name, "date": date, "start": start, "end": end, "total": total, "id": o.id, "verified": o.verified})

        return resultList

class edithours(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'tracker.add_volunteer_hour'
    raise_exception = True
    model = volunteer_hour
    fields = ['date', 'start', 'end', 'verified']
    template_name = 'staff/edithours.html'
    context_object_name = 'hours'
    success_url = reverse_lazy('volunteers')
    success_message = "Hour updated successfully"

class deletehours(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'tracker.add_volunteer_hour'
    raise_exception = True
    model = volunteer_hour
    template_name = 'staff/deletehours.html'
    success_url = reverse_lazy('volunteers')
    success_message = "Hour deleted successfully"