# Generated by Django 4.0 on 2022-01-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.IntegerField()),
                ('education', models.IntegerField()),
                ('marriage', models.IntegerField()),
                ('pay_1', models.IntegerField()),
                ('pay_2', models.IntegerField()),
                ('pay_3', models.IntegerField()),
                ('pay_4', models.IntegerField()),
                ('pay_5', models.IntegerField()),
                ('pay_6', models.IntegerField()),
                ('bill_amt_1', models.FloatField()),
                ('bill_amt_2', models.FloatField()),
                ('bill_amt_3', models.FloatField()),
                ('bill_amt_4', models.FloatField()),
                ('bill_amt_5', models.FloatField()),
                ('bill_amt_6', models.FloatField()),
                ('pay_amt_1', models.FloatField()),
                ('pay_amt_2', models.FloatField()),
                ('pay_amt_3', models.FloatField()),
                ('pay_amt_4', models.FloatField()),
                ('pay_amt_5', models.FloatField()),
                ('pay_amt_6', models.FloatField()),
                ('age', models.IntegerField()),
                ('limit_bal', models.FloatField()),
                ('classification', models.CharField(max_length=30)),
            ],
        ),
    ]
