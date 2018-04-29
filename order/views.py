# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
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


def shipping_pdf(request, order_id=None):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="shipping_label.pdf"'

    order = Order.objects.filter(id=order_id)[0]
    user = User.objects.filter(id=order.user_id)[0]
    if user != request.user:
        return HttpResponseRedirect("/")
    profile = Profile.objects.filter(user_id=user.id)[0]

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.setDash(2,2)
    p.line(30,375,565,375)
    p.setDash(0)
    p.rect(30,30,535,785)
    p.drawString(85, 350, "ORDER DATE:")
    p.drawString(175, 350, str(order.created.strftime("%d-%m-%Y")))
    p.drawString(85, 300, "SHIP TO:")
    p.drawString(175, 300, "COMPUTER SCIENCE DEPARTMENT")
    p.drawString(175, 275, "5 THE PARADE")
    p.drawString(175, 250, "CARDIFF")
    p.drawString(175, 225, "CF24 3AA")
    p.drawString(85, 175, "RETURN TO:")
    p.drawString(175, 175, str(user.first_name).upper() + " " + str(user.last_name).upper())
    p.drawString(175, 150, str(profile.address).upper())
    p.drawString(175, 125, str(profile.city).upper())
    p.drawString(175, 100, str(profile.postcode).upper())

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


def invoice_pdf(request, order_id=None):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="invoice.pdf"'

    order = Order.objects.filter(id=order_id)[0]
    order_items = OrderItem.objects.filter(order_id=order_id)
    user = User.objects.filter(id=order.user_id)[0]
    if user != request.user:
        return HttpResponseRedirect("/")
    profile = Profile.objects.filter(user_id=user.id)[0]

    buffer = BytesIO()
    styles = getSampleStyleSheet()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
 
    p.drawString(70, height - 85, "Order ID: #" + order_id)
    p.drawString(70, height - 100, "Ordered: " + order.created.strftime("%d-%m-%Y"))
    data= [['Item', 'Book Title', 'Price (£)', 'Quantity', 'Total Price (£)']]
    for i, order_item in enumerate(order_items):
        data += [[str(i + 1), Paragraph(str(order_item.book.title), styles["Normal"]), order_item.price, order_item.quantity, order_item.quantity * order_item.price]]

    t=Table(data, colWidths=[2*cm,7*cm,2*cm,2*cm,3*cm])
    t.setStyle(TableStyle([('LINEABOVE', (0,0), (-1,0), 2, colors.black),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('LINEBELOW', (0,-1), (-1,-1), 2, colors.black)]))

    t.wrapOn(p, width, height)
    t.wrapOn(p, width, height)
    t.drawOn(p, 70, height - (25 * len(order_items)) - 125)

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

