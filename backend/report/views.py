from rest_framework import generics
from itertools import groupby
from operator import itemgetter
from rest_framework.response import Response

from django.db import connection
from django.db.utils import OperationalError
from django.http.response import JsonResponse


from report import models
from report import serializers





# Database Connection Check Function
def check_database_connection(request):
    try:
        with connection.cursor():
            # Try to execute a simple query to check the database connection
            pass
        return JsonResponse({'message': 'Database Connected.'})
    except OperationalError as e:
        # Handle the database connection error
        error_message = str(e)
        return JsonResponse({'error': 'Database connection error', 'message': error_message}, status=500)
    
    

class MaterialTransactionsViewAll(generics.ListAPIView):
    queryset = models.materialTransactions.objects.all()
    serializer_class = serializers.MaterialTransactionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().values()  # Convert queryset to a list of dictionaries
        grouped_data = []

        # Group by department
        grouped_by_department = groupby(queryset, key=itemgetter('department'))

        for department, transactions in grouped_by_department:
            transactions_data = list(transactions)
            grouped_data.append({
                'department': department,
                'transactions': self.serializer_class(transactions_data, many=True).data
            })

        return Response(grouped_data)
