from decimal import Decimal

import unicodecsv as csv
from django.db import IntegrityError, connection
from django.db import models
from django.http import HttpResponse


# Create your models here.
class Account(models.Model):
    code = models.CharField(max_length=10, primary_key=True, )
    name = models.CharField(max_length=255)
    level = models.PositiveSmallIntegerField(default=0)
    account_type = models.CharField(max_length=20)
    description = models.CharField(
        max_length=255, default=None, null=True, blank=True)
    opening_balance = models.DecimalField(
        max_digits=19, decimal_places=4, default=0)
    debit_only = models.BooleanField(default=True)
    parent_account = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True)
    notes = models.CharField(
        max_length=255, blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.code} - {self.name}'

    @staticmethod
    def export_to_csv():
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="account_data.csv"'

        writer = csv.writer(response, encoding='utf-8-sig')
        writer.writerow(
            ['Code', 'Name', 'Level', 'Account Type', 'Description', 'Opening Balance', 'Debit Only', 'Parent Account',
             'Notes'])

        accounts = Account.objects.all()
        for account in accounts:
            row = [
                account.code,
                account.name,
                account.level,
                account.account_type,
                account.description if account.description else '',
                account.opening_balance,
                account.debit_only,
                account.parent_account_id if account.parent_account else '',
                account.notes,
            ]
            writer.writerow(
                [str(value) if value is not None else '' for value in row])

        return response

    @staticmethod
    def import_from_csv(file):
        # file_data = file.read().decode('utf-8-sig')
        file_data = file.read()
        lines = csv.reader(file_data.splitlines())
        # Skip the header row
        next(lines)
        with connection.cursor() as cursor:
            for fields in lines:
                account_data = dict(
                    code=fields[0],
                    name=fields[1],
                    level=int(fields[2]),
                    account_type=fields[3],
                    description=fields[4] if fields[4] != '\\N' else None,
                    opening_balance=Decimal(fields[5]),
                    debit_only=bool(fields[6]),
                    parent_account_id=fields[7] if fields[7] != '\\N' else None,
                    notes=fields[8] if fields[8] != '\\N' else None,
                )

                query = """
                INSERT INTO coa_account (CODE, NAME, LEVEL, account_type, description, opening_balance, debit_only, parent_account_id, notes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                params = [account_data['code'], account_data['name'], account_data['level'],
                          account_data['account_type'], account_data['description'], account_data['opening_balance'],
                          account_data['debit_only'], account_data['parent_account_id'], account_data['notes']]

                # Print the complete query
                print("Executing query:", cursor.mogrify(query, params))

                try:
                    cursor.execute(query, params)
                # Catch the duplicate key error
                except IntegrityError as e:
                    # Rollback the transaction
                    connection.rollback()
                    # Print the error message
                    print("Error:", e)
                # Skip or update the row as needed
                # For example, you can use cursor.execute("UPDATE ...") to update the existing row
                # Or you can use continue to skip the row and move on to the next one
                continue


class Transaction(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    opening_balance = models.DecimalField(max_digits=19, decimal_places=4)
    debit_only = models.BooleanField()
    debit_amount = models.DecimalField(max_digits=19, decimal_places=4)
    credit_amount = models.DecimalField(max_digits=19, decimal_places=4)
    closing_balance = models.DecimalField(max_digits=19, decimal_places=4)

    def __str__(self):
        return f"{self.account.name} - {self.debit_amount}/{self.credit_amount}"
