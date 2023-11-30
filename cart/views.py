from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.exceptions import ValidationError

from account.models import Address
from cart.models import Order, OrderItem, DiscountCode
from product.models import Book
from cart.cart_module import Cart

from django.conf import settings
import requests
import json
import ghasedakpack


# sms= ghasedakpack.Ghasedak('1cc40b202af546332b8f4d8a73b686160f675dc90591784d3b5ffd3d5ee0e819')




class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart_detail.html', context={'cart': cart})


class CartAddView(View):
    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        quantity = request.POST.get('quantity')
        # print(quantity, book)
        cart = Cart(request)
        cart.add(book, quantity)
        return redirect('cart:cart_detail')


class CartDeleteView(View):
    def get(self, request, id):
        # print(id)
        cart = Cart(request)
        cart.delete(id)
        return redirect('cart:cart_detail')


class OrderDetailView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        return render(request, 'cart/order_detail.html', context={'order': order})


class OrderCreationView(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total())
        for item in cart:
            OrderItem.objects.create(order=order, book=item['book'], quantity=item['quantity'], price=item['price'])

        cart.remove_cart()
        return redirect('cart:order_detail', order.pk)


class ApplyDiscountView(View):
    def post(self, request, pk):
        code = request.POST.get('discount_code')
        order = get_object_or_404(Order, id=pk)
        discount_code = get_object_or_404(DiscountCode, name=code)
        if discount_code.quantity == 0:
            return redirect('cart:order_detail', order.id)
            # raise ValidationError('The discount code has expired')

        order.total_price -= order.total_price * discount_code.discount / 100
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return redirect('cart:order_detail', order.id)


ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/"

# Optional Data
metadata = {
	"mobile": "09123456789",  # Buyer phone number Must start with 09
	"email": "example@example.com",  # Buyer Email
	"order_id": "1234",  # Order Id
}
currency = "IRT"  # or "IRT"

# کد مرچنت خود را در فایل settings وارد کنید

# Required Data
amount = 2000  # Based on your currency
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"
CallbackURL = 'http://127.0.0.1:8000/cart/verify/'


# Important: need to edit for a real server.

class SendRequestView(View):
    def post(self,request,pk):
        order = get_object_or_404(Order,id=pk, user=request.user)
        # print(request.POST.get('address'))
        # return HttpResponse(request.POST.get('address'))
        address = get_object_or_404(Address, id=request.POST.get('address'))
        # return HttpResponse(address.address)
        order.address =f"{address.address} - {address.phone} - {address.email}"
        order.save()
        request.session['order_id'] = str(order.id)

        data = {
            "merchant_id": settings.MERCHANT,
            "amount": order.total_price,
            "currency": currency,
            "description": description,
            "callback_url": CallbackURL,
            "metadata": {"mobile":request.user.phone }
        }
        data = json.dumps(data)
        # set content length by data
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        try:
            response = requests.post(
                ZP_API_REQUEST, data=data, headers=headers, timeout=10)

            if response.status_code == 200:
                response = response.json()
                if response['data']['code'] == 100:
                    url = ZP_API_STARTPAY + str(response['data']['authority'])
                    return redirect(url)
                else:
                    data = json.dumps({'status': False, 'code': str(response['data']['code'])})
                    return HttpResponse(data)
            return response

        except requests.exceptions.Timeout:
            data = json.dumps({'status': False, 'code': 'timeout'})
            return HttpResponse(data)
        except requests.exceptions.ConnectionError:
            data = json.dumps({'status': False, 'code': 'اتصال برقرار نشد'})
            return HttpResponse(data)

    # def sendmessage(self):
    #     message='سفارش جدید ثبت شد به پنل مدیریت مراجعه کنید'
    #     sms.verification({'receptor': '09374826259', 'type': '1', 'template': 'ispaid', 'param1': message})



class VerifyView(View):
    def get(self,request):
        authority = request.GET.get('Authority')
        status = request.GET.get('Status')
        order_id = request.session['order_id']
        order = Order.objects.get(id=int(order_id))
        if status == "NOK":
            return HttpResponse(json.dumps({'status': "پرداخت ناموفق"}))
        data = {
            "merchant_id": settings.MERCHANT,
            "amount": order.total_price,
            "authority": authority,
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'accept': 'application/json'}
        try:
            response = requests.post(ZP_API_VERIFY, data=data, headers=headers)
            response = response.json()
            err = response["errors"]
            if err:
                return JsonResponse(err, content_type="application/json", safe=False)
            if response['data']['code'] == 100:
                order.is_paid = True
                order.save()
                data = json.dumps({'status': True, 'first_time_verify': True, 'ref_id': response['data']['ref_id']})
                return redirect('home:main')
            else:
                data = json.dumps({'status': False, 'data': response})
            return JsonResponse(data, safe=False)

        except requests.exceptions.ConnectionError:
            data = json.dumps({'status': False, 'code': 'اتصال برقرار نشد'})
            return HttpResponse(data)


