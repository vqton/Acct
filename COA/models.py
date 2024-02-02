from django.db import models

# Create your models here.
class Account(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    level = models.PositiveSmallIntegerField()
    account_type = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    opening_balance = models.DecimalField(max_digits=19, decimal_places=4)
    debit_only = models.BooleanField()
    parent_account = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    notes = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    opening_balance = models.DecimalField(max_digits=19, decimal_places=4)
    debit_only = models.BooleanField()
    debit_amount = models.DecimalField(max_digits=19, decimal_places=4)
    credit_amount = models.DecimalField(max_digits=19, decimal_places=4)
    closing_balance = models.DecimalField(max_digits=19, decimal_places=4)

    def __str__(self):
        return f"{self.account.name} - {self.debit_amount}/{self.credit_amount}"
