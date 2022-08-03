from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import *


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = questions
        fields = ['question', 'right_answer','quize']


class answe(serializers.ModelSerializer):
    class Meta:
        model = answers
        fields = ['answer', 'question_id']


class relat(serializers.ModelSerializer):

    class Meta:
        model = relation
        fields = ['name_quize', 'major']
