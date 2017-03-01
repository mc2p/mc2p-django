from django.views.generic import View
from django.http import HttpResponse

import json

from . import MC2PClient
from .signals import notification_received


class MC2PNotifyView(View):
    """
    View to receive notification
    """
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        json_body = json.loads(request.body)

        mc2p = MC2PClient()
        notification_data = mc2p.NotificationData(json_body)
        notification_received.send(sender=notification_data)

        return HttpResponse('OK')
