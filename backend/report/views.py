from rest_framework import generics
from django.db import connection
from django.db.utils import OperationalError
from django.http.response import JsonResponse


from report import models
from report import serializers



