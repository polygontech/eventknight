from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_tags = models.CharField(max_length=200)

    def __str__(self):
        return self.event_name


class User(models.Model):
    event = models.ForeignKey(Event)
    tw_user = models.CharField(max_length=200)
    tw_user_token = models.CharField(max_length=400)
    tw_user_token_secret = models.CharField(max_length=400)

    def __str__(self):
        return self.tw_user
