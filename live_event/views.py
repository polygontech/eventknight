from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Event, User


# Views Definitions
# index
def index(request):
    event_list = Event.objects.all()
    context = {
        'event_list': event_list,
    }
    template = 'live_event/index.html'
    return render(request, template, context)


# live
def live(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event,
    }
    template = 'live_event/live.html'
    return render(request, template, context)


def submit(request):
    template = 'live_event/index.html'
    try:
        e_name = request.POST['txt_event_name']
        e_tags = request.POST['txt_event_tags']
        tmp = Event(event_name=e_name, event_tags=e_tags)
        tmp.save()
    except:
        return render(request, template, {
            'error_msg': "unexpected error!.",
        })
    else:
        #event_list = Event.objects.all()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
