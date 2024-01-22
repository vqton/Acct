from django.db import models

class AccountType(models.Model):
    type_id = models.CharField(max_length=1, primary_key=True)
    type_name = models.CharField(max_length=255)

class AccountGroup(models.Model):
    group_id = models.CharField(max_length=1, primary_key=True)
    group_name = models.CharField(max_length=255)

class Account(models.Model):
    account_id = models.CharField(max_length=4, primary_key=True)
    account_name = models.CharField(max_length=255)
    type_id = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    group_id = models.ForeignKey(AccountGroup, on_delete=models.CASCADE)
    parent_account_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
