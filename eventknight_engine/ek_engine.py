from channels import Group
from .models import Event, User


def ek_send():
    Group("live-1").send({
        "text": "[stream] --> from ek_engine",
    })
