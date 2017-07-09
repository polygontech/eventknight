from channels import Group
from .models import Event
from django.core.exceptions import ObjectDoesNotExist


def ws_connect(message):
    prefix, event_id = message['path'].strip('/').split('/')
    try:
        event = Event.objects.get(pk=event_id)
    except ObjectDoesNotExist:
        print('Event does not exist')
    else:
        if prefix == "live":
            Group('live-' + str(event.id)).add(message.reply_channel)
            message.reply_channel.send({"accept": True})
        else:
            message.reply_channel.send({"close": True})


def ws_disconnect(message):
    prefix, event_id = message['path'].strip('/').split('/')
    Group('live-' + str(event_id)).discard(message.reply_channel)


def ws_receive(message):
    # print(message.content['text'])
    prefix, event_id = message['path'].strip('/').split('/')
    if prefix == "live":
        try:
            event = Event.objects.get(pk=event_id)
        except ObjectDoesNotExist:
            print('Event does not exist')
        else:
            Group("live-"+ str(event.id)).send({
                "text": "[stream] %s" % message.content['text'],
            })
    else:
        print('Unknown message')
