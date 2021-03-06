from market.celery import app
from django.core.mail import send_mail
from .models import Order


@app.task
def order_created(order_id):
    """ Задача отправки мейла уведомлений при успешном оформлении заказа"""
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Dear {}, \n\n You have successfully  placed an order. Your order id is {}'.format(order.first_name,
                                                                                                 order_id)
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent
