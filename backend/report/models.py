from django.db import models



class materialTransactions(models.Model):
    department = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    input = models.CharField(max_length=755)
    output = models.IntegerField()
    percentage = models.CharField(max_length=255)

    class Meta:
        db_table = 'material_transaction'