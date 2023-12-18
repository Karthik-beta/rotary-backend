from rest_framework import serializers
from . import models

class MaterialTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.materialTransactions
        fields = '__all__'