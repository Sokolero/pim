from django.shortcuts import render
from .utils.act import Act
from doc_factory.models import EntryModel
# from .models import ActsModel
import json
from django.conf import settings

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

from datetime import datetime

# Create your views here.
class ActView(APIView):

    def post(self, request, *args, **kwargs):
        ids = request.data.get("checked_ids")
        numb = 1
        # for id in ids:
        print(ids)
        id = ids[0]

        entry = get_object_or_404(EntryModel.objects.all(), pk=id)
        # entry = get_object_or_404(EntryModel.objects.all(), pk=pk)
        template = settings.BASE_DIR + '/acts/utils/act.xls'
        path = settings.BASE_DIR + '/acts/static/acts/act_{}.xls'.format(numb)
        date = datetime.today()
        contract = (entry.contractNumber, entry.contractDate.day,
                    entry.contractDate.month, entry.contractDate.year)
        adress = entry.title
        cost = entry.cost
        print(entry.cost)

        act = Act(template, path, numb, date, contract, adress, cost)
        act.create_act()
        href = "/static/acts/act_{}.xls".format(numb)

        return Response({"href": href})
