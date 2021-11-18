from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from datetime import date,timedelta

import os

import json
import razorpay

def pre_payment(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            amount = request.POST['amount']
            duration = "month" if amount=="99" else "year"
            order_amount = int(amount) * 100
            order_currency = 'INR'
            client = razorpay.Client(
                auth=("rzp_test_pv07EKOwEETIks", "hVU87m5vI5xxFBBs0kUdSRTg")
            )
            payment = client.order.create({"amount":order_amount, "currency":order_currency})
            response = {"payment":payment,"name":user.name,"email":user.email,"mobile":user.mobile,"duration":duration}
            return render(request, 'payment/payment.html', response)
        else:
            active_subscriber = True if user.due_date is not None and date.today() <= user.due_date else False
            days_left = (user.due_date - date.today()).days if user.due_date is not None else None
            
            response = {"active_subscriber":active_subscriber,"days_left":days_left}
            return render(request, 'payment/payment.html', response)
    else:
        messages.info(request, "Login to continue!")
        return redirect('/accounts/signin')

def post_payment(request, duration):
    if request.method == "POST":
        user =request.user

        due_date = date.today()+timedelta(days=30) if duration=="month" else date.today()+timedelta(days=365)
        user.is_subscriber = True
        user.due_date = due_date
        user.save()

        messages.info(request, "payment successful!!")
        return redirect('/enrollment/mybooks')