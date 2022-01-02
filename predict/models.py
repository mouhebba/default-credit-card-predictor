from django.db import models


class PredResults(models.Model):

    sex = models.IntegerField()
    education = models.IntegerField()
    marriage = models.IntegerField()
    pay_1 = models.IntegerField()
    pay_2 = models.IntegerField()
    pay_3 = models.IntegerField()
    pay_4 = models.IntegerField()
    pay_5 = models.IntegerField()
    pay_6 = models.IntegerField()
    bill_amt1 = models.FloatField()
    bill_amt2 = models.FloatField()
    bill_amt3 = models.FloatField()
    bill_amt4 = models.FloatField()
    bill_amt5 = models.FloatField()
    bill_amt6 = models.FloatField()
    pay_amt1 = models.FloatField()
    pay_amt2 = models.FloatField()
    pay_amt3 = models.FloatField()
    pay_amt4 = models.FloatField()
    pay_amt5 = models.FloatField()
    pay_amt6 = models.FloatField()
    age = models.IntegerField()
    limit_bal = models.FloatField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification
