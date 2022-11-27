from datetime import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Max, Min
from django.shortcuts import render
from tracker.models import volunteer_hour


@login_required
def individual_report(request):
    context = {}
    total_hours = 0
    context['entries'] = []
    for o in volunteer_hour.objects.all().filter(volunteer=request.user, verified=True).order_by("date"):
        date = o.date
        hours = datetime.combine(date, o.end) - datetime.combine(date, o.start)
        total_hours += hours.total_seconds() / 3600
        hours = hours.total_seconds() / 3600

        context['entries'].append(
            {'date': date, 'start_time': o.start, 'end_time': o.end, "hours": hours, 'verified': o.verified})
    context['total_hours'] = total_hours

    context['start_date'] = \
        volunteer_hour.objects.all().filter(volunteer=request.user, verified=True).aggregate(Min('date'))['date__min']
    context['end_date'] = \
        volunteer_hour.objects.all().filter(volunteer=request.user, verified=True).aggregate(Max('date'))['date__max']
    context['now'] = datetime.now()

    return render(request, template_name='reports/individual_report.html', context=context)


@login_required
def individual_report_printable(request):
    context = {}
    total_hours = 0
    context['entries'] = []
    for o in volunteer_hour.objects.all().filter(volunteer=request.user, verified=True).order_by("date"):
        date = o.date
        hours = datetime.combine(date, o.end) - datetime.combine(date, o.start)
        total_hours += hours.total_seconds() / 3600
        hours = hours.total_seconds() / 3600

        context['entries'].append(
            {'date': date, 'start_time': o.start, 'end_time': o.end, "hours": hours, 'verified': o.verified})
    context['total_hours'] = total_hours

    context['start_date'] = \
        volunteer_hour.objects.all().filter(volunteer=request.user, verified=True).aggregate(Min('date'))['date__min']
    context['end_date'] = \
        volunteer_hour.objects.all().filter(volunteer=request.user, verified=True).aggregate(Max('date'))['date__max']
    context['now'] = datetime.now()

    return render(request, template_name='reports/individual_report_printable.html', context=context)


@permission_required('tracker.can_view_all_hours', raise_exception=True)
def day_report_request(request):
    context = {}
    total_hours = 0
    context['entries'] = []
    for o in volunteer_hour.objects.all().filter(volunteer=request.user, verified=True).order_by("date"):
        date = o.date
        hours = datetime.combine(date, o.end) - datetime.combine(date, o.start)
        total_hours += hours.total_seconds() / 3600
        hours = hours.total_seconds() / 3600

        context['entries'].append(
            {'date': date, 'start_time': o.start, 'end_time': o.end, "hours": hours, 'verified': o.verified})
    context['total_hours'] = total_hours

    context['start_date'] = \
        volunteer_hour.objects.all().filter(volunteer=request.user, verified=True).aggregate(Min('date'))['date__min']
    context['end_date'] = \
        volunteer_hour.objects.all().filter(volunteer=request.user, verified=True).aggregate(Max('date'))['date__max']

    return render(request, template_name='reports/day_report_request.html', context=context)


@permission_required('tracker.can_view_all_hours',  raise_exception=True)
def day_report(request):
    context = {}
    context['entries'] = []
    total_hours = 0
    day = None
    month = None
    year = None

    try:
        day = request.GET.get('date')[8:10]
        month = request.GET.get('date')[5:7]
        year = request.GET.get('date')[0:4]
    except:
        pass

    if not day or not month or not year:
        day = None
        month = None
        year = None

    for o in volunteer_hour.objects.all().filter(date__day=day, date__month=month, date__year=year):
        date = o.date
        hours = datetime.combine(date, o.end) - datetime.combine(date, o.start)
        total_hours += hours.total_seconds() / 3600
        hours = hours.total_seconds() / 3600

        name = "{} {}".format(o.volunteer.first_name, o.volunteer.last_name)

        context['date'] = date
        context['entries'].append({'name': name, 'start_time': o.start, 'end_time': o.end, "hours": hours, 'verified': o.verified})

    context['now'] = datetime.now()
    context['total_hours'] = total_hours

    return render(request, template_name='reports/day_report.html', context=context)

@login_required
def day_report_printable(request):
    context = {}
    context['entries'] = []
    total_hours = 0

    day = None
    month = None
    year = None

    try:
        day = request.GET.get('date')[8:10]
        month = request.GET.get('date')[5:7]
        year = request.GET.get('date')[0:4]
    except:
        pass

    if not day or not month or not year:
        day = None
        month = None
        year = None

    for o in volunteer_hour.objects.all().filter(date__day=day, date__month=month, date__year=year):
        date = o.date
        hours = datetime.combine(date, o.end) - datetime.combine(date, o.start)
        total_hours += hours.total_seconds() / 3600
        hours = hours.total_seconds() / 3600

        name = "{} {}".format(o.volunteer.first_name, o.volunteer.last_name)

        context['date'] = date
        context['entries'].append({'name': name, 'start_time': o.start, 'end_time': o.end, "hours": hours, 'verified': o.verified})

    context['now'] = datetime.now()
    context['total_hours'] = total_hours

    return render(request, template_name='reports/day_report_printable.html', context=context)