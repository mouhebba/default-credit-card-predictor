from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults
import pickle
import os
from catboost import CatBoostClassifier
from catboost import Pool


def predict(request):
    return render(request, 'predict.html')


def encode_pay(pay):
    return pay + 2


def bin_age(age):
    if 20 <= age <= 50:
        return 0
    elif 25 < age <= 30:
        return 1
    elif 30 < age <= 35:
        return 2
    elif 35 < age <= 40:
        return 3
    elif 40 < age <= 50:
        return 4
    elif 50 < age <= 60:
        return 5
    elif 60 < age <= 80:
        return 6


def bin_limit(limit):
    if 5000 <= limit <= 50000:
        return 0
    elif 50000 < limit <= 100000:
        return 1
    elif 150000 < limit <= 200000:
        return 2
    elif 200000 < limit <= 300000:
        return 3
    elif 300000 < limit <= 400000:
        return 4
    elif 400000 < limit <= 500000:
        return 5
    else:
        return 6


def bin_bill_amt(bill_amt):
    if bill_amt < 0:
        return 0
    elif bill_amt == 0:
        return 1
    elif 0 < bill_amt <= 25000:
        return 2
    elif 25000 < bill_amt <= 75000:
        return 3
    elif 75000 < bill_amt <= 200000:
        return 4
    else:
        return 5


def bin_pay_amt(pay_amt):
    if -1 <= pay_amt <= 0:
        return 0
    elif 0 < pay_amt <= 25000:
        return 1
    elif 25000 < pay_amt <= 50000:
        return 2
    elif 50000 < pay_amt <= 100000:
        return 3
    else:
        return 4


def predict_chances(request):
    if request.POST.get('action') == 'post':
        # Receive data from client
        sex = int(request.POST.get('sex'))
        education = int(request.POST.get('education'))
        marriage = int(request.POST.get('marriage'))
        pay_1 = int(request.POST.get('pay_1'))
        pay_2 = int(request.POST.get('pay_2'))
        pay_3 = int(request.POST.get('pay_3'))
        pay_4 = int(request.POST.get('pay_4'))
        pay_5 = int(request.POST.get('pay_5'))
        pay_6 = int(request.POST.get('pay_6'))
        bill_amt1 = float(request.POST.get('bill_amt1'))
        bill_amt2 = float(request.POST.get('bill_amt2'))
        bill_amt3 = float(request.POST.get('bill_amt3'))
        bill_amt4 = float(request.POST.get('bill_amt4'))
        bill_amt5 = float(request.POST.get('bill_amt5'))
        bill_amt6 = float(request.POST.get('bill_amt6'))
        pay_amt1 = float(request.POST.get('pay_amt1'))
        pay_amt2 = float(request.POST.get('pay_amt2'))
        pay_amt3 = float(request.POST.get('pay_amt3'))
        pay_amt4 = float(request.POST.get('pay_amt4'))
        pay_amt5 = float(request.POST.get('pay_amt5'))
        pay_amt6 = float(request.POST.get('pay_amt6'))
        age = int(request.POST.get('age'))
        limit_bal = float(request.POST.get('limit_bal'))

        # Read model
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        model = pickle.load(open(os.path.join(__location__, 'finalized_model.sav'), 'rb'))
        # Make prediction
        result = model.predict([[sex, education, marriage,
                                 encode_pay(pay_1), encode_pay(pay_2), encode_pay(pay_3),
                                 encode_pay(pay_4), encode_pay(pay_5), encode_pay(pay_6),
                                 bin_bill_amt(bill_amt1), bin_bill_amt(bill_amt2), bin_bill_amt(bill_amt3),
                                 bin_bill_amt(bill_amt4), bin_bill_amt(bill_amt5), bin_bill_amt(bill_amt6),
                                 bin_pay_amt(pay_amt1), bin_pay_amt(pay_amt2), bin_pay_amt(pay_amt3),
                                 bin_pay_amt(pay_amt4), bin_pay_amt(pay_amt5), bin_pay_amt(pay_amt6),
                                 bin_age(age), bin_limit(limit_bal)]])

        classification = result[0]

        classTxt = '0 (No Default)'
        if (classification == 1):
            classTxt = '1 (Default)'
        sexTxt = 'Male'
        if (sex == 2):
            sexTxt = 'Female'
        educationTxt = 'Graduate School'
        if (education == 2):
            educationTxt = 'University'
        elif (education == 3):
            educationTxt = 'High School'
        elif (education == 4):
            educationTxt = 'Others'
        marriageTxt = 'Married'
        if (marriage == 2):
            marriageTxt = 'Single'
        elif (marriage == 3):
            marriageTxt = 'Others'

        PredResults.objects.create(sex=sex, education=education, marriage=marriage,
                                   pay_1=pay_1, pay_2=pay_2, pay_3=pay_3,
                                   pay_4=pay_4, pay_5=pay_5, pay_6=pay_6,
                                   bill_amt1=bill_amt1, bill_amt2=bill_amt2, bill_amt3=bill_amt3,
                                   bill_amt4=bill_amt4, bill_amt5=bill_amt5, bill_amt6=bill_amt6,
                                   pay_amt1=pay_amt1, pay_amt2=pay_amt2, pay_amt3=pay_amt3,
                                   pay_amt4=pay_amt4, pay_amt5=pay_amt5, pay_amt6=pay_amt6,
                                   age=age, limit_bal=limit_bal, classification=classification)

        return JsonResponse({'result': classTxt,
                             'sex': sexTxt, 'education': educationTxt, 'marriage': marriageTxt,
                             'pay_1': pay_1, 'pay_2': pay_2, 'pay_3': pay_3,
                             'pay_4': pay_4, 'pay_5': pay_5, 'pay_6': pay_6,
                             'bill_amt1': bill_amt1, 'bill_amt2': bill_amt2, 'bill_amt3': bill_amt3,
                             'bill_amt4': bill_amt4, 'bill_amt5': bill_amt5, 'bill_amt6': bill_amt6,
                             'pay_amt1': pay_amt1, 'pay_amt2': pay_amt2, 'pay_amt3': pay_amt3,
                             'pay_amt4': pay_amt4, 'pay_amt5': pay_amt5, 'pay_amt6': pay_amt6,
                             'limit_bal': limit_bal, 'age': age},
                            safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
