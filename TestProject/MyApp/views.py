import json

from django.core import serializers
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Fenotipos


@api_view(["GET"])
def FindPhenotypes(genedata):
    try:
        genename = json.loads(genedata.body)
        qs = Fenotipos.objects.filter(gene_name=genename) #SELECT * FROM Fenotipos WHERE gene_name = XPTO
        qs_json = serializers.serialize('json', qs)

        return HttpResponse(qs_json, content_type='application/json')
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
