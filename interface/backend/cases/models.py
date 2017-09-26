from enum import IntEnum, unique

from backend.images.models import ImageSeriesSerializer, ImageLocationSerializer
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)
from django.db import models
from django.utils import timezone
from rest_framework import serializers


class Case(models.Model):
    """
    An analysis session on an image series.
    """
    created = models.DateTimeField(default=timezone.now)

    series = models.ForeignKey('images.ImageSeries', related_name='cases')


class Candidate(models.Model):
    """
    Predicted location of a possible nodule.
    """
    created = models.DateTimeField(default=timezone.now)

    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='candidates')

    centroid = models.OneToOneField('images.ImageLocation', on_delete=models.CASCADE)

    probability_concerning = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])


def django_enum(cls):
    # decorator needed to enable enums in django templates
    cls.do_not_call_in_templates = True
    return cls


class Nodule(models.Model):
    """
    Actual nodule, either confirmed as concerning from prediction or manually added.
    """

    @unique  # ensures all variables are unique
    @django_enum
    class LungOrientation(IntEnum):
        NONE = 0
        LEFT = 1
        RIGHT = 2

    created = models.DateTimeField(default=timezone.now)

    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='nodules')

    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, null=True)

    centroid = models.OneToOneField('images.ImageLocation', on_delete=models.CASCADE)

    lung_orientation = models.IntegerField(
        choices=[(choice.value, choice.name.replace("_", " ")) for choice in LungOrientation],
        default=LungOrientation.NONE.value)


class CandidateSerializer(serializers.ModelSerializer):
    centroid = ImageLocationSerializer(read_only=True)

    class Meta:
        model = Candidate
        fields = ('id', 'created', 'centroid', 'case_id', 'probability_concerning')


class NoduleSerializer(serializers.ModelSerializer):
    candidates = CandidateSerializer(read_only=True, many=True)
    centroid = ImageLocationSerializer(read_only=True)

    class Meta:
        model = Case
        fields = ('id', 'created', 'candidates', 'centroid')


class CaseSerializer(serializers.ModelSerializer):
    series = ImageSeriesSerializer()
    candidates = CandidateSerializer(read_only=True, many=True)
    nodules = NoduleSerializer(read_only=True, many=True)

    class Meta:
        model = Case
        fields = ('id', 'created', 'series', 'candidates', 'nodules')
