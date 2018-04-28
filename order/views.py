from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from io import BytesIO
from reportlab.pdfgen import canvas
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from account.models import Profile

def order_create(request):
	cart = Cart(request)
	if request.user.is_authenticated():
		user_id = request.user.id
		current_user_object = User.objects.get(id=user_id)
		form = OrderCreateForm(request.POST)
			
		if form.is_valid():
			order = form.save(commit=False)
			order.user = current_user_object
			order = form.save()
			for item in cart:
				OrderItem.objects.create(order=order,
                                         book=item['book'],
                                         price=item['price'],
                                         quantity=item['quantity'])
			cart.clear()
			return render(request, 'order/order/created.html',{'order':order})
		else:
			return render(request, 'order/order/create.html',{'form': form})			
	else:
		return render(request, 'order/order/create-login.html')


def pdf(request, order_id=None):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="shipping_label.pdf"'

    order = Order.objects.filter(id=order_id)[0]
    user = User.objects.filter(id=order.user_id)[0]
    if user != request.user:
    	return HttpResponseRedirect("/")
    profile = Profile.objects.filter(user_id=user.id)[0]

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Start writing the PDF here
    p.drawString(100, 175, "SHIP TO:")
    p.drawString(175, 175, str(user.first_name).upper() + " " + str(user.last_name).upper())
    p.drawString(175, 150, str(profile.address).upper())
    p.drawString(175, 125, str(profile.city).upper())
    p.drawString(175, 100, str(profile.postcode).upper())
    # End writing

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response