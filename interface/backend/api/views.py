from backend.api import serializers
from backend.cases.models import (
    Case,
    Candidate,
    Nodule,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.images.models import ImageSeries
from django.http import JsonResponse
from rest_framework import viewsets


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = serializers.CaseSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = serializers.CandidateSerializer


class NoduleViewSet(viewsets.ModelViewSet):
    queryset = Nodule.objects.all()
    serializer_class = serializers.NoduleSerializer


class ImageSeriesViewSet(viewsets.ModelViewSet):
    queryset = ImageSeries.objects.all()
    serializer_class = serializers.ImageSeriesSerializer


class ImageAvailableApiView(APIView):
    """
    View list of images from dataset directory
    """
    def get(self, request):
        """
        Return a list of files and folders in dataset
        TODO implement directory retrieval method
        """
        return Response([])


def candidate_mark(request, candidate_id):
    return JsonResponse({'response': "Candidate {} was marked".format(candidate_id)})


def candidate_dismiss(request, candidate_id):
    return JsonResponse({'response': "Candidate {} was dismissed".format(candidate_id)})
