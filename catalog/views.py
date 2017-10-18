# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Item
# Create your views here.


class ItemList(APIView):
    def get(self, request, format=None):
        items = Item.objects.all()
        return Response(items)
