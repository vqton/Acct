from django.db import models


class Account(models.Model):
    account_code = models.IntegerField()
    account_name = models.CharField(max_length=50)
    account_type = models.IntegerField()
    account_group = models.IntegerField()
    account_content = models.CharField(max_length=255)
    accounting_method = models.CharField(max_length=255)

    def __str__(self):
        return self.account_name

   