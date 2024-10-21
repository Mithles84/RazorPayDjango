import razorpay
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Tea

def buy_tea(request):
    tea = Tea.objects.first()  # Assume one tea product for sale
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # Create a payment order
    payment = client.order.create({
        'amount': int(tea.price * 100),  # amount in paise (Razorpay expects the amount in INR paise)
        'currency': 'INR',
        'payment_capture': '1'
    })

    context = {
        'tea': tea,
        'razorpay_order_id': payment['id'],
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'amount': tea.price,
    }
    return render(request, 'payment/buy_tea.html', context)

def payment_success(request):
    # Handle post-payment success
    return render(request, 'payment/success.html')
