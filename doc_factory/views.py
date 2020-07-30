from django.shortcuts import render
from django.views.generic.base import View
from .models import EntryModel
from .utils.factory import Factory
from .forms import AddEntryForm
import os
from django.conf import settings

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, JSONParser, MultiPartParser
from .serializers import EntryModelSerializer

# view for DRF API
class EntryView(APIView):
    parser_classes = (JSONParser, MultiPartParser, FileUploadParser )

    def get(self, request, *args, **kwargs):
        entrys = EntryModel.objects.all()
        serializer = EntryModelSerializer(entrys, many=True)
        return Response({ "entrys": serializer.data })

    def post(self, request, format=None):

        files = request.data.getlist('files')
        # получение валидных данных
        for file in files:
            path = file.temporary_file_path()
            bf = Factory(path)
            entry = EntryModel(
                title = bf.find_title(),
                tu = bf.find_tu(),
                length = bf.find_length(),
                res = bf.find_res(),
                type = bf.find_type(),
                adress = bf.find_adress(),
            )
            entry.save()

        entrys = EntryModel.objects.all()
        serializer = EntryModelSerializer(entrys, many=True)
        return Response({ "entrys": serializer.data, "message": "Объекты добавлены в работу" })
        # entry = request.data.get('entry')
        # serializer = EntryModelSerializer(data=entry)
        # if serializer.is_valid(raise_exception=True):
        #     entry_saved = serializer.save()


    def put(self, request, pk):
        print(pk)
        saved_entry = get_object_or_404(EntryModel.objects.all(), pk=pk)
        data = request.data.get("entry")
        serializer = EntryModelSerializer(instance=saved_entry, data=data, partial=True)
        print(data)
        if serializer.is_valid(raise_exception=True):
            entry_saved = serializer.save()
        return Response({
            "success": "Запись {} была обновлена".format(entry_saved.adress)
        })

    def delete(self, request, pk):
        entry = get_object_or_404(EntryModel.objects.all(), pk=pk)
        entry.delete()
        return Response({
            "message": "Запись с id `{}` была удалена".format(pk)
        }, status=204)
